#!/usr/bin/env python3
import json
import sys
from typing import Any, Dict


class LogRedactor:
    ALLOWED_REGIONS = {"eu-west-1", "eu-west-2", "eu-central-1", "eu-north-1"}

    SENSITIVE_KEYS = {
        "email": "[REDACTED_EMAIL]",
        "ip": "[REDACTED_IP]",
        "account_id": "[REDACTED_ACCOUNT]",
        "token": "[REDACTED_TOKEN]",
    }

    def is_region_allowed(self, event_region: Any) -> bool:
        # region must exist and be one of the allowlisted strings
        return isinstance(event_region, str) and event_region in self.ALLOWED_REGIONS

    def redact_obj(self, obj: Any, redaction_counts: Dict[str, int]) -> Any:
        """
        Recursively traverse obj (dict/list) and redact values for sensitive keys.
        Returns a sanitized copy (does not mutate input).
        """
        if isinstance(obj, dict):
            sanitized: Dict[str, Any] = {}
            for k, v in obj.items():
                if k in self.SENSITIVE_KEYS:
                    sanitized[k] = self.SENSITIVE_KEYS[k]
                    redaction_counts[k] = redaction_counts.get(k, 0) + 1
                else:
                    sanitized[k] = self.redact_obj(v, redaction_counts)
            return sanitized

        if isinstance(obj, list):
            return [self.redact_obj(item, redaction_counts) for item in obj]

        # scalar (str/int/float/bool/None) -> unchanged
        return obj


def main() -> int:
    redactor = LogRedactor()

    # Metrics
    total_lines = 0
    parsed_ok = 0
    parsed_failed = 0
    allowed_count = 0
    quarantined_count = 0
    redactions_by_field: Dict[str, int] = {}

    # Open quarantine output once
    quarantine_path = "quarantine.jsonl"
    try:
        qf = open(quarantine_path, "a", encoding="utf-8")
    except OSError as e:
        print(f"ERROR - cannot open quarantine file '{quarantine_path}': {e}", file=sys.stderr)
        return 2

    with qf:
        for raw_line in sys.stdin:
            total_lines += 1
            line = raw_line.strip()
            if not line:
                # Treat empty lines as parse failures (or skip); here we count as failed.
                parsed_failed += 1
                continue

            try:
                event = json.loads(line)
            except json.JSONDecodeError:
                parsed_failed += 1
                continue

            # Only accept JSON objects as "events"
            if not isinstance(event, dict):
                parsed_failed += 1
                continue

            parsed_ok += 1

            # Sanitize first (so quarantine also gets redacted)
            sanitized = redactor.redact_obj(event, redactions_by_field)

            region = sanitized.get("region")
            if redactor.is_region_allowed(region):
                allowed_count += 1
                sys.stdout.write(json.dumps(sanitized, ensure_ascii=False) + "\n")
            else:
                quarantined_count += 1
                qf.write(json.dumps(sanitized, ensure_ascii=False) + "\n")

    summary = {
        "total_lines": total_lines,
        "parsed_ok": parsed_ok,
        "parsed_failed": parsed_failed,
        "allowed_count": allowed_count,
        "quarantined_count": quarantined_count,
        "redactions_by_field": redactions_by_field,
    }
    print(json.dumps(summary, ensure_ascii=False), file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
