import sys


class PatternMatching:
    """
    Create redact methods to sanitize logs lines from emails and ips

    """

    def needs_email_redacting(self, email: str) -> bool:

        if " " in email or email.count("@") != 1:
            return False
        local, domain = email.split("@")
        if not local or not domain or "." not in domain:
            return False
        if domain.startswith(".") or domain.endswith("."):
            return False
        return True

    def needs_ip_redacting(self, field: str) -> bool:
        import ipaddress
        field = self.normalize_ip_token(field)
        try:
            return isinstance(ipaddress.ip_address(field), ipaddress.IPv4Address)
        except ValueError:
            return False

    def normalize_ip_token(self, token: str) -> str:
        # keep only digits and dots
        return "".join(ch for ch in token if ch.isdigit() or ch == ".")

    def apply_redact(self, field: str):
        """
        Go over fields Redact email if found
        """
        if self.needs_email_redacting(field):
            return "[REDACTED_EMAIL]"
        if self.needs_ip_redacting(field):
            return "[REDACTED_IP]"
        return field


def main():
    pattern_matching_toolset = PatternMatching()
    try: # handles files errors, wrong path, bad permissions
        with open('../data/sendmail_sample.log', 'r', encoding='utf-8', errors="replace") as log_file:

            for line in log_file:
                line = line.strip()  # removes leading/trailing whitespace and the newline
                if not line:  # skips blank lines
                    continue

                # break line into fields
                event_fields = line.split()
                sanitized_fields = []
                for item in event_fields:
                    item = pattern_matching_toolset.apply_redact(item)
                    sanitized_fields.append(item)
                reviewed_line = " ".join(sanitized_fields)
                print(f'line: {line}')
                print(f'sanitized line: {reviewed_line}')
    except OSError as e:
        print(f"error: failed to open input file: {e}", file=sys.stderr)
        return 2

if __name__ == "__main__":
    main()




#TODO separate process output (pipe errors to sdterr)
#TODO at the moment if a bad line could blow the run. Improve per-line error handling
