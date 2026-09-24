# Tool Notes — Burp Suite Community Edition

---

## What Burp Suite Does

Burp Suite is an HTTP interception proxy. It sits between
the browser and the server, capturing every request and
response in real time. This allows us to:
- Read raw HTTP requests including headers, cookies, and body
- Identify authentication tokens and session identifiers
- Modify requests before they reach the server
- Replay captured requests in different contexts

---

## Setup Used in SecChkLab

**Proxy listener:** 127.0.0.1:8080 (default)
**Browser:** Burp Suite built-in Chromium browser
**Certificate:** Not required when using built-in browser
**Intercept:** Set to OFF during passive observation
              Set to ON only when actively modifying requests

The built-in browser is the cleanest workflow for local testing —
all traffic is automatically routed through Burp without
touching system proxy settings.

---

## Key Tabs Used

### Proxy → HTTP History
Every request made through the Burp browser appears here.
Used to:
- Find specific requests by method (POST, GET) and URL path
- Extract cookie values from authenticated sessions
- Identify parameters sent in form submissions

### Proxy → Intercept
When ON — requests are paused for manual review and modification
before being forwarded to the server.
When OFF — requests pass through and are logged only.

---

## Finding the Login Request — SCL-001

Filter HTTP History by:
- Method: POST
- URL containing: /login/index.php

Request body captured:
anchor=&logintoken=EzqAfHpv8xTbKQ3mNXcNydCjPvR0urcF
&username=admin&password=Admin%401234

Note: %40 is URL encoding for the @ character.
Note: logintoken is Moodle's CSRF protection on the login form.

---

## Key Commands and Shortcuts

| Action | How |
|--------|-----|
| Open built-in browser | Proxy → Intercept → Open Browser |
| View all captured requests | Proxy → HTTP History |
| Copy request as curl | Right-click request → Copy as curl command |
| Send request to Repeater | Right-click → Send to Repeater |
| Search history by term | HTTP History → Filter → search string |

---

## Notes for Future Tests

- Repeater tab: resend any captured request with modifications
  useful for SCL-002 (IDOR) URL parameter tampering
- Intruder tab: automated parameter fuzzing
  useful for SCL-003 (SQL Injection) payload testing
- Scanner (Pro only): automated vulnerability detection
  not available in Community Edition
