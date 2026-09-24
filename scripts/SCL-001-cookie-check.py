"""
SCL-001 — Session Cookie Inspector
SecChkLab Security Research

Purpose:
Parses a raw HTTP request captured from Burp Suite and
extracts all cookie values for documentation and analysis.

Usage:
Paste your captured HTTP request between the triple quotes
in the raw_request variable and run the script.
Output will display all cookies with their values clearly labeled.
"""

def parse_cookies(raw_request):
    cookies = {}
    lines = raw_request.strip().split('\n')
    
    for line in lines:
        if line.lower().startswith('cookie:'):
            cookie_string = line[7:].strip()
            pairs = cookie_string.split(';')
            for pair in pairs:
                pair = pair.strip()
                if '=' in pair:
                    name, value = pair.split('=', 1)
                    cookies[name.strip()] = value.strip()
    return cookies

def analyze_cookies(cookies):
    print("=" * 60)
    print("SCL-001 — Cookie Analysis Report")
    print("=" * 60)
    
    for name, value in cookies.items():
        print(f"\nCookie Name: {name}")
        print(f"Value:       {value}")
        
        if name == 'MoodleSession':
            print("Type:        Primary session token")
            print("Risk:        High if stolen — grants full session access")
            print("Length:      {} characters".format(len(value)))
            
        elif name == 'MOODLEID1_':
            print("Type:        Persistent browser identifier")
            print("Encoding:    sodium encrypted (libsodium)")
            print("Persists:    Survives logout — changes on re-authentication")
            print("Risk:        Informational — no direct access risk")
            
        elif name == '_xsrf':
            print("Type:        CSRF protection token")
            print("Note:        Relevant to SCL-006 testing")
            
        else:
            print("Type:        Unknown — investigate further")
        
        print("-" * 40)


# Paste your raw Burp Suite HTTP request here
raw_request = """
GET /moodle/my/ HTTP/1.1
Host: localhost
Cookie: MoodleSession=v5q80d86bt74rq7fl2; MOODLEID1_=sodium%3AZpmNwbLi0L4HY; _xsrf=2|94794f96|19181937
"""

cookies = parse_cookies(raw_request)
analyze_cookies(cookies)

print("\nTotal cookies found:", len(cookies))
print("=" * 60)
