# SCL-002 — IDOR and Information Disclosure Analysis

**Target:** Moodle 5.1.6+ (Build: 20260818)
**Date:** October 2026
**Tester:** Yubin — SecChkLab Research
**Status:** ✅ Complete
**Overall Verdict:** Partially Mitigated + Information Disclosure Confirmed

---

## Summary

| Test | Verdict |
|---|---|
| User ID enumeration | ℹ️ Informational |
| Quiz attempt IDOR — content access | ✅ Not Vulnerable |
| Quiz attempt enumeration via error messages | ⚠️ Finding Confirmed |
| Unauthenticated attempt access | ✅ Not Vulnerable |

---

## Test 1 — User ID Enumeration

Navigated to sequential user profile URLs as admin:

| URL | Response |
|---|---|
| /user/profile.php?id=1 | Guest account profile loaded |
| /user/profile.php?id=2 | Admin account profile loaded |
| /user/profile.php?id=3 | "Invalid user" error |
| /user/profile.php?id=4+ | "Invalid user" error |

**Finding:** Sequential user IDs are predictable.
Valid and invalid IDs return visually different responses
revealing which accounts exist without requiring any
special privilege to probe.

**Verdict:** ℹ️ Informational — partially by design in
Moodle's open educational context but represents a
user enumeration surface in sensitive deployments.

---

## Test 2 — Quiz Attempt Content Access (IDOR)

**Setup:**
Three quiz attempts were generated across three accounts:

| Attempt ID | Owner |
|---|---|
| attempt=1 | Admin |
| attempt=2 | teststudent |
| attempt=3 | Second test account |

**Test:** Logged in as teststudent. Attempted to access
admin's quiz attempt directly via URL manipulation:
/mod/quiz/review.php?attempt=1&cmid=3
/mod/quiz/attempt.php?attempt=1&cmid=3


**Response:** "This is not your attempt!"

Admin's quiz answers, score, and submission were not served.
Moodle validated attempt ownership before serving any content.

**Verdict:** ✅ Not Vulnerable — ownership validation
prevents unauthorized content access via attempt ID manipulation.

---

## Test 3 — Attempt Enumeration via Error Message Differentiation

**This is the confirmed finding.**

By observing error message differences across attempt IDs,
an attacker can map the entire quiz attempt space without
ever accessing protected content:

| Scenario | Response | Information Leaked |
|---|---|---|
| Valid attempt, wrong owner | "This is not your attempt!" | Attempt exists, owned by another user |
| Valid attempt, correct owner | Quiz content served | Attempt exists, you own it |
| Invalid attempt ID | "This quiz attempt no longer exists" | No attempt at this ID |
| Not authenticated | Redirect to login | System requires authentication |

**Impact:** An attacker can cycle through attempt IDs
and use error message differences to:
- Determine exactly how many quiz attempts exist system-wide
- Identify which attempt IDs are active and owned by other users
- Infer system usage patterns and user activity volume
- Build a complete map of attempt ownership without viewing content

**Severity:** LOW
No quiz content, answers, or grades are exposed.
Only metadata about attempt existence is leaked.

**Verdict:** ⚠️ Finding Confirmed — Information disclosure
through inconsistent error message responses.

---

## Remediation Recommendation

Moodle should return a single unified error response
regardless of whether an attempt exists or belongs
to another user. Recommended response:

> "You do not have permission to view this attempt."

This makes valid and invalid attempt IDs indistinguishable
to unauthorized requesters and eliminates the enumeration surface.

---

## References

- OWASP Top 10: A01:2021 — Broken Access Control
- OWASP Top 10: A05:2021 — Security Misconfiguration
- CWE-200: Exposure of Sensitive Information to Unauthorized Actor
- CWE-284: Improper Access Control
