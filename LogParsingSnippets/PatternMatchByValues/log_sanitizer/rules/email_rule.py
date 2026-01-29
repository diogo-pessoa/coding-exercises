from __future__ import annotations
from typing import Optional, Tuple

class EmailRule:
    """
    SRP: Detect + redact email substrings inside a token, preserving punctuation.
    """

    name = "email"
    EMAIL_CHARS = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789._%+-")

    def needs_email_redacting(self, email: str) -> bool:
        if " " in email or email.count("@") != 1:
            return False
        local, domain = email.split("@")
        if not local or not domain or "." not in domain:
            return False
        if domain.startswith(".") or domain.endswith("."):
            return False
        if local.startswith(".") or local.endswith("."):
            return False
        return True

    def _extract_email_candidate(self, token: str) -> Optional[str]:
        at = token.find("@")
        if at == -1:
            return None

        # Expand left from '@'
        i = at - 1
        while i >= 0 and token[i] in self.EMAIL_CHARS:
            i -= 1
        start = i + 1

        # Expand right from '@' (domain chars + '-')
        j = at + 1
        while j < len(token) and (token[j] in self.EMAIL_CHARS or token[j] == "-"):
            j += 1

        candidate = token[start:j]
        if self.needs_email_redacting(candidate):
            return candidate
        return None

    def apply(self, token: str) -> Tuple[str, int]:
        """
        Return (new_token, redaction_count).
        """
        candidate = self._extract_email_candidate(token)
        if not candidate:
            return token, 0

        return token.replace(candidate, "REDACTED_EMAIL"), 1
