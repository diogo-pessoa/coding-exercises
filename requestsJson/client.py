import json
import logging
import sys
from dataclasses import dataclass
from enum import Enum
from typing import Any, Mapping, Sequence

import requests


class ServiceStatus(str, Enum):
    OK = "ok"
    NOT_OK = "not_ok"


@dataclass(frozen=True)
class HealthStatus:
    service: str
    status: ServiceStatus
    latency_ms: int
    tags: tuple[str, ...]

    @classmethod
    def from_dict(cls, raw: Mapping[str, Any]) -> "HealthStatus":
        if not isinstance(raw, Mapping):
            raise TypeError("healthcheck payload must be a JSON object")

        service = str(raw.get("service", ""))
        status_raw = raw.get("status", "")
        try:
            status = ServiceStatus(status_raw)
        except ValueError:
            raise ValueError(f"invalid status: {status_raw!r}")

        latency_raw = raw.get("latency_ms", 0)
        try:
            latency_ms = int(latency_raw)
        except (TypeError, ValueError):
            raise ValueError(f"invalid latency_ms: {latency_raw!r}")

        tags_raw: Sequence[Any] = raw.get("tags", [])
        if not isinstance(tags_raw, Sequence) or isinstance(tags_raw, (str, bytes)):
            raise ValueError("tags must be a list")
        tags = tuple(str(t) for t in tags_raw)

        return cls(service=service, status=status, latency_ms=latency_ms, tags=tags)

    def is_healthy(self) -> bool:
        return self.status is ServiceStatus.OK

    def has_tags(self) -> bool:
        return bool(self.tags)

    def tags_csv(self) -> str:
        return ", ".join(self.tags)

    def has_tag(self, tag: str) -> bool:
        return tag in self.tags

    def latency_bucket(self) -> str:
        if self.latency_ms < 50:
            return "fast"
        if self.latency_ms < 200:
            return "ok"
        return "slow"


def main() -> int:
    log = logging.getLogger(__name__)
    url = "http://localhost:8080/data/response.json"

    try:
        r = requests.get(url, timeout=5)
        r.raise_for_status()
        payload = r.json()

        hs = HealthStatus.from_dict(payload)

        log.info("service=%s healthy=%s bucket=%s tags=%s",
                 hs.service, hs.is_healthy(), hs.latency_bucket(), hs.tags_csv())

        return 0

    except requests.exceptions.RequestException as e:
        log.exception("HTTP request failed: %s", e)
        return 2
    except (ValueError, TypeError, json.JSONDecodeError) as e:
        log.exception("Invalid healthcheck payload: %s", e)
        return 2


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    raise SystemExit(main())
