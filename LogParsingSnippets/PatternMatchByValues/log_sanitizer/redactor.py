from __future__ import annotations
from typing import List, Protocol, Tuple

from metrics import Metrics

class Rule(Protocol):
    name: str
    def apply(self, token: str) -> Tuple[str, int]: ...

class Redactor:
    """
    SRP: Orchestrate applying rules to tokens/lines + update metrics.
    Does NOT know file I/O.
    """

    def __init__(self, rules: List[Rule]):
        self.rules = rules

    def redact_token(self, token: str, metrics: Metrics) -> str:
        for rule in self.rules:
            new_token, count = rule.apply(token)
            if count:
                if rule.name == "email":
                    metrics.email_redactions += count
                elif rule.name == "ip":
                    metrics.ip_redactions += count
                return new_token  # stop on first match
        return token

    def redact_line(self, line: str, metrics: Metrics) -> str:
        tokens = line.split()
        metrics.tokens_seen += len(tokens)

        changed = False
        out = []
        for t in tokens:
            nt = self.redact_token(t, metrics)
            if nt != t:
                changed = True
            out.append(nt)

        if changed:
            metrics.lines_with_redactions += 1

        return " ".join(out)
