import pickle, getpass
import requests, urlparse
import pyquery

CHECK = u'\u2713'.encode('utf8')

def loginGetCookies(username, password):
    s = requests.Session()
    lg = s.get("https://adventofcode.com/auth/github")

    pq = pyquery.PyQuery(lg.content)
    has_utf8 = pq('input[name=utf8]')[0].value
    auth_token = pq('input[name=authenticity_token]')[0].value

    data = {
        "authenticity_token": auth_token,
        "utf8": has_utf8,
        "commit:": "Sign+in",
        "login": username,
        "password": password,
    }

    r = s.post("https://github.com/session", data=data)
    if r.status_code == 200:
        if r.url.lower().find("adventofcode.com") >= 0:
            print "Success"
            return s.cookies
        else:
            print "Auth failed"
    else:
        print "Github login attempt failed (bad request)"
    return None

if __name__ == "__main__":
    username = raw_input("Username:")
    password = getpass.getpass( "Password:")
    with open(".cookies", "wb") as f:
        cookies = loginGetCookies(username, password)
        if cookies:
            pickle.dump( cookies, f)
            print "Wrote .cookies for %s" % username
