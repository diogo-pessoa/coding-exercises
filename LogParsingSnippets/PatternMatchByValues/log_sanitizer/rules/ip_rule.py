from __future__ import annotations
from typing import Tuple
import ipaddress

class IpRule:
    """
    SRP: Detect + redact IPv4 substrings inside a token, preserving punctuation.
    """

    name = "ip"

    def normalize_ip_token(self, token: str) -> str:
        return "".join(ch for ch in token if ch.isdigit() or ch == ".")

    def needs_ip_redacting(self, token: str) -> bool:
        candidate = self.normalize_ip_token(token)
        if not candidate:
            return False
        try:
            return isinstance(ipaddress.ip_address(candidate), ipaddress.IPv4Address)
        except ValueError:
            return False

    def apply(self, token: str) -> Tuple[str, int]:
        candidate = self.normalize_ip_token(token)
        if candidate and self.needs_ip_redacting(token):
            return token.replace(candidate, "REDACTED_IP"), 1
        return token, 0
