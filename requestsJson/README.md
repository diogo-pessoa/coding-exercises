PLaying with HTTP json responses
---

* Simplest form for an http server, serving files from current dir.
* Client hits localhost:8080/data/response.json, parses Json

### Walkthrough the client.py

Sure — here’s the “student-friendly” walkthrough.

### `Enum` (`ServiceStatus`)

```py
class ServiceStatus(str, Enum):
    OK = "ok"
    NOT_OK = "not_ok"
```

An `Enum` is a controlled set of allowed values. Instead of letting `status` be *any* string (typos, unexpected values),
we force it to be either `"ok"` or `"not_ok"`.

Why `str, Enum`?

* It makes enum values behave like strings when needed (nice for printing/logging), but still gives you validation and
  safety.

So if the JSON contains `"status": "okay"` → we treat that as invalid and raise an error.

---

### `@dataclass(frozen=True)` (`HealthStatus`)

```py
@dataclass(frozen=True)
class HealthStatus:
    service: str
    status: ServiceStatus
    latency_ms: int
    tags: tuple[str, ...]
```

A `dataclass` is a shortcut for “this class mostly stores data”. Python automatically generates:

* an `__init__` (constructor)
* a helpful `repr` (nice printing)
* comparisons (optional benefit)

`frozen=True` means the object is **immutable**: once created, you can’t accidentally change fields. That’s great for
“parsed data” objects because it prevents bugs like “someone changed latency later”.

Also notice types:

* `latency_ms` is always an `int`
* `tags` is stored as a `tuple` (immutable), not a list

---

### `from_dict()` (the parser / validator)

```py
@classmethod
def from_dict(cls, raw: Mapping[str, Any]) -> "HealthStatus":
```

This is a “factory” method: it takes the raw JSON dict and **builds** a valid `HealthStatus`.

Inside it we:

* confirm the payload is actually a JSON object (`Mapping`)
* validate/convert fields:

    * `service` → string
    * `status` → must be a `ServiceStatus` enum (or error)
    * `latency_ms` → must be convertible to int (or error)
    * `tags` → must be a list-like thing, then converted into `tuple[str, ...]`

Key idea: **all contract rules live in one place**. After parsing, the rest of your code can trust the object.

---

### The “query” methods (simple, predictable behavior)

```py
def is_healthy(self) -> bool:
    return self.status is ServiceStatus.OK
```

Returns a boolean: healthy or not.

```py
def has_tags(self) -> bool:
    return bool(self.tags)
```

If tuple is empty → `False`, otherwise `True`.

```py
def tags_csv(self) -> str:
    return ", ".join(self.tags)
```

Just formats tags nicely for output/logging.

```py
def has_tag(self, tag: str) -> bool:
    return tag in self.tags
```

Checks membership, returns boolean.

```py
def latency_bucket(self) -> str:
    ...
```

Turns a number into a category (`fast/ok/slow`). This keeps your “business logic” out of `main()`.

---

### `main()` (I/O + boundaries)

`main()` does **HTTP + JSON parsing + error handling**, then hands the payload to `HealthStatus.from_dict()`.

We catch:

* `requests.exceptions.RequestException` → network / HTTP problems
* `ValueError / TypeError / JSONDecodeError` → bad JSON or contract mismatch

And we return `0` or `2` so the script has proper exit codes.

---

That’s the overall structure:
**`main()` talks to the outside world** → **`HealthStatus` enforces the contract and provides clean methods**.
