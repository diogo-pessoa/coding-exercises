from __future__ import annotations
import sys
from metrics import Metrics
from redactor import Redactor
from rules import EmailRule, IpRule


def build_default_redactor() -> Redactor:
    # Simple factory: central place for rule ordering/config.
    return Redactor([EmailRule(), IpRule()])


def run(input_path: str) -> int:
    redactor = build_default_redactor()
    metrics = Metrics()

    try:
        with open(input_path, "r", encoding="utf-8", errors="replace") as f:
            for raw in f:
                metrics.total_lines += 1

                line = raw.strip()
                if not line:
                    metrics.blank_lines += 1
                    continue

                sanitized = redactor.redact_line(line, metrics)
                metrics.processed_lines += 1
                print(sanitized)

    except OSError as e:
        print(f"error: failed to open/read file {input_path}: {e}", file=sys.stderr)
        return 2

    # Keep stdout as "sanitized stream"; send summary to stderr.
    print(
        "=== metrics ===\n"
        f"total_lines={metrics.total_lines}\n"
        f"blank_lines={metrics.blank_lines}\n"
        f"processed_lines={metrics.processed_lines}\n"
        f"tokens_seen={metrics.tokens_seen}\n"
        f"email_redactions={metrics.email_redactions}\n"
        f"ip_redactions={metrics.ip_redactions}\n"
        f"lines_with_redactions={metrics.lines_with_redactions}",
        file=sys.stderr,
    )
    return 0


if __name__ == "__main__":
    # Example: python -m log_sanitizer.main ../data/sendmail_sample.log
    path = sys.argv[1] if len(sys.argv) > 1 else "../data/sendmail_sample.log"
    raise SystemExit(run(path))
