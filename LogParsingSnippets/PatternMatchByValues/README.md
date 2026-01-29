Redact email and ip from sendmail sample log
---

[sendmail_sample.log](../data/sendmail_sample.log)


output: 

    line: sm-mta[11761]: k79IaGJL011761: ruleset=check_mail, arg1=<direto@mkt.submarino.com.br>, relay=mkt1.submarino.com.br [1.2.3.4], reject=553 5.3.0 <direto@mkt.submarino.com.br>... SPAM REJECT
    sanitized line: sm-mta[11761]: k79IaGJL011761: ruleset=check_mail, [REDACTED_EMAIL] relay=mkt1.submarino.com.br [REDACTED_IP] reject=553 5.3.0 <direto@mkt.submarino.com.br>... SPAM REJECT


## The same as the log_sanitizer rules in bash commands

### Redact IPv4 addresses (anywhere)

```bash
sed -E 's/([0-9]{1,3}\.){3}[0-9]{1,3}/REDACTED_IP/g' sendmail_sample.log
```

<WIP>