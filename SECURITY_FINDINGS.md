# Seeded Security Examples

These are training examples, not claims about a deployed system.

| ID | Category | Vulnerable example | Safer direction |
|---|---|---|---|
| DEMO-01 | Hardcoded secret | `app/credentials.py` contains a fake API key | Read secrets from a secret manager or environment; rotate exposed secrets |
| DEMO-02 | SQL injection | `app/db_legacy.py` builds SQL using string formatting | Use parameterized queries |
| DEMO-03 | Command injection | `app/ops_legacy.py` passes user-controlled text to a shell | Avoid shell execution; use fixed executable and argument arrays with validation |
| DEMO-04 | Debug mode | `app/web_legacy.py` enables debug mode | Disable debug mode outside local development |
| DEMO-05 | Path traversal | `app/files_legacy.py` joins untrusted paths without containment checks | Canonicalize and enforce a trusted base directory |
| DEMO-06 | Unsafe deserialization | `app/cache_legacy.py` uses pickle on untrusted bytes | Use a safe data format and validate schema |
| DEMO-07 | Weak cryptography | `app/crypto_legacy.py` uses MD5 for password-like data | Use a password hashing function such as Argon2id, scrypt, or bcrypt |
| DEMO-08 | Insecure temporary file | `app/temp_legacy.py` uses a predictable temp filename | Use secure temporary-file APIs |
| DEMO-09 | Missing authorization check | `app/reports_legacy.py` returns a report by identifier without ownership validation | Enforce object-level authorization on the server |
| DEMO-10 | Sensitive logging | `app/logging_legacy.py` logs a supplied token | Redact credentials and sensitive data from logs |

The vulnerable examples are deliberately isolated and must not be deployed.
