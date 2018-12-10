#!/usr/bin/python2
import pickle, getpass
import requests, urlparse
import pyquery

import lib

def auth_session(username, password):
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
            return s
        else:
            print "Github auth failed"
    else:
        print "Github login attempt failed (bad request)"
    return None

if __name__ == "__main__":
    try:
        fp = lib.cookies_path()
        f = open(fp, "wb")
    except OSError as e:
        print >>sys.stderr, "Failed to open", fp, "as writable"

    if f:
        username = raw_input("Username:")
        password = getpass.getpass( "Password:")
        session = auth_session(username, password)
        if session:
            pickle.dump(session.cookies, f)
            print "Wrote sesison cookies ", fp, "for", username
            print "This file cannot be used to authenticate with Github, but do not make it public"
        f.close()

