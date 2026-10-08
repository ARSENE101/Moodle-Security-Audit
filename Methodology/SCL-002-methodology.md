# SCL-002 — IDOR Testing — Methodology

---

## What Is IDOR

Insecure Direct Object Reference occurs when an application
exposes internal object identifiers — such as user IDs,
course IDs, or attempt IDs — in URLs or request parameters
without verifying that the requesting user has permission
to access that specific object.

The attack is conceptually simple: change a number in a URL
and see if you get access to someone else's data.

IDOR is consistently listed in the OWASP Top 10 under
Broken Access Control — one of the most commonly found
and most impactful vulnerability classes in web applications.

---

## Why This Matters in an LMS Context

Moodle stores highly sensitive academic data:
- Quiz answers and exam submissions
- Grade records
- Assignment submissions
- Personal student information

Unauthorized access to any of these via IDOR would
constitute a serious academic integrity violation and
potential data protection breach in a real deployment.

The core question we are answering: can a lower-privilege
user access objects owned by a higher-privilege user simply
by changing an identifier in the URL?

---

## Attack Surface Identified

Moodle exposes numeric IDs across many object types:

| Object | URL Parameter | Example |
|---|---|---|
| User profiles | ?id=N | /user/profile.php?id=2 |
| Quiz attempts | ?attempt=N | /mod/quiz/attempt.php?attempt=1 |
| Courses | ?id=N | /course/view.php?id=1 |
| Grade reports | ?userid=N | /grade/report/user/index.php?userid=2 |
| Assignments | ?id=N | /mod/assign/view.php?id=1 |

Each of these is a potential IDOR surface. Our testing
focused on user profiles and quiz attempts as the highest
value targets in an educational context.

---

## Test Design

### Phase 1 — Object Discovery
Map which IDs exist by probing sequential values.
Observe response differences between valid and invalid IDs.
Document what information each response reveals.

### Phase 2 — Cross-User Access Attempt
With two active user accounts at different privilege levels,
attempt to access objects owned by the higher-privilege user
while authenticated as the lower-privilege user.
Target: quiz attempts, grade data, profile edit functions.

### Phase 3 — Unauthenticated Access Attempt
Remove authentication entirely and attempt direct URL access
to protected objects. Verify authentication is enforced
before ownership checks are applied.

### Phase 4 — Error Message Analysis
Document all unique error messages returned across different
access scenarios. Analyze what system information each
message reveals to an unauthenticated or unauthorized requester.

---

## Accounts Used

| Account | Privilege Level | Attempt ID |
|---|---|---|
| admin | Administrator | attempt=1 |
| teststudent | Student | attempt=2 |
| Second test account | Student | attempt=3 |

---

## Tools Used

- Browser URL bar — direct ID manipulation
- Burp Suite HTTP History — request observation and parameter mapping
- Browser DevTools — response analysis

See `tools/burpsuite-notes.md` for Burp configuration details.
