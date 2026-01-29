from dataclasses import dataclass

@dataclass
class Metrics:
    total_lines: int = 0
    blank_lines: int = 0
    processed_lines: int = 0

    tokens_seen: int = 0
    email_redactions: int = 0
    ip_redactions: int = 0
    lines_with_redactions: int = 0
