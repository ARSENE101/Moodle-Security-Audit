# SCL-002 — Tools Used

---

## Primary Tool — Browser URL Manipulation

**What it is:** Direct manual modification of URL parameters
in the browser address bar.

**Why it works for IDOR:** IDOR vulnerabilities exist at
the application logic level — no special tool is needed
to test them. Simply changing ?id=2 to ?id=1 in the URL
is sufficient to probe whether access controls are enforced.

**What we looked for:**
- Different page content loading for different IDs
- Different error messages for different scenarios
- Any data belonging to other users being served

---

## Secondary Tool — Burp Suite Community Edition

**Role in SCL-002:** Passive observation and parameter mapping.

**Specifically used for:**
- Identifying all URL parameters containing numeric IDs
  across Moodle's page navigation
- Observing raw HTTP responses to document exact error
  message text returned by the server
- Mapping the full set of ID-bearing endpoints for future testing

**Key observation from HTTP History:**
Quiz attempt URLs follow a predictable pattern:
/mod/quiz/attempt.php?attempt=N&cmid=M
/mod/quiz/review.php?attempt=N&cmid=M
/mod/quiz/summary.php?attempt=N&cmid=M

Both `attempt` and `cmid` parameters are numeric and sequential.

---

## Custom Script — SCL-002-attempt-enumerator.py

**Purpose:** Automates the manual enumeration process to
demonstrate the information disclosure finding at scale.

**What it does:** Probes sequential attempt IDs and classifies
responses based on error message content — proving that
different messages reveal different system states.

**Language:** Python 3 — no external libraries required.
Uses only Python standard library urllib module.

**See:** scripts/SCL-002-attempt-enumerator.py

---

## Tools Not Needed For This Test

**SQLmap** — not applicable, no SQL injection tested here
**OWASP ZAP** — automated scanning not required for IDOR
**Semgrep** — source code analysis not required for this test

These tools become relevant in SCL-003 onwards.
