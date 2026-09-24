## Test 3 — MOODLEID1_ Persistence Analysis

Observation: MOODLEID1_ cookie persists through logout unchanged
             Value only regenerates on fresh authentication
             Persistent value does not grant access alone
             
Timeline:
- Pre-login:  sodium:ZpmNwb... [value A]
- Logged in:  sodium:ZpmNwb... [value A — unchanged]  
- Logged out: sodium:ZpmNwb... [value A — unchanged]
- Re-login:   sodium:jlznXy... [value B — NEW]

Finding: MOODLEID1_ is a persistent browser identifier that 
         survives logout. It changes only on fresh authentication.
         Possession alone does not grant session access.
         
Potential Risk: Persistent identifier could be used to track 
                users across sessions or correlate browsing 
                patterns even after logout.
                
Verdict: INFORMATIONAL — Not directly exploitable but 
         worth noting for privacy implications.
