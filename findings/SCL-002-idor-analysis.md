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
