# SCL-001 — Session Management — Methodology

---

## Why Session Management

Session management is the backbone of web authentication.
After login, the server needs to recognise a user across
multiple requests without asking for credentials every time.
It does this through a session token stored in a cookie.

If that token can be stolen, forged, or replayed — an attacker
gains full account access without ever knowing the password.
This makes session management one of the highest priority
surfaces in any web application security audit.

---

## Why Moodle Is a High Value Target Here

Moodle is deployed by thousands of educational institutions.
A successful session attack against a real deployment would mean:
- Unauthorized access to student grades and exam results
- Access to unpublished course content and upcoming assessments
- Ability to impersonate students or teaching staff
- Potential to modify submitted work or recorded grades

---

## How Moodle Sessions Work

When a user logs in, Moodle:
1. Generates a cryptographically random session token
2. Stores that token in its database session table server-side
3. Sends the token to the browser as the MoodleSession cookie

On every subsequent request Moodle cross-checks the incoming
MoodleSession value against its database. Match found — access
granted. No match — request rejected.

This is server-side session validation. Not all applications
implement this. Some store session data entirely in the cookie
itself and trust whatever the client sends. Those systems are
directly vulnerable to the manipulation attacks tested here.

---

## Research Questions

1. Can a forged or modified session token fool the server?
2. Can a stolen valid token be replayed after the user logs out?
3. Does the MOODLEID1_ persistent identifier enable silent
   re-authentication or expose users to cross-session tracking?

---

## Test Design

### Test 1 — Token Manipulation
Capture active session token via Burp Suite.
Modify value. Inject into separate browser. Observe response.
Expected vulnerable behavior: access granted with modified token.
Expected secure behavior: rejection and redirect to login.

### Test 2 — Post-Logout Replay
Capture valid session token before logout.
Complete logout through normal interface.
Inject pre-logout token into separate browser. Observe response.
Expected vulnerable behavior: access granted post-logout.
Expected secure behavior: token rejected — session destroyed.

### Test 3 — Persistent Identifier Analysis
Track MOODLEID1_ cookie value across four states:
unauthenticated, authenticated, post-logout, re-authenticated.
Test whether identifier alone enables access without MoodleSession.

---

## Tools Used

- Burp Suite Community Edition — HTTP interception and history
- Opera Browser — secondary context for replay attempts
- Browser DevTools (Application tab) — cookie inspection and manipulation

See `tools/burpsuite-notes.md` for configuration details.
