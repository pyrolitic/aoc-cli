#!/usr/bin/python3

import sys
import pickle
import getpass
import requests
import pyquery

import lib

def auth_session(username, password):
    session = requests.Session()
    login_page = session.get("https://adventofcode.com/auth/github")

    query = pyquery.PyQuery(login_page.content)
    #has_utf8 = query('input[name=utf8]')[0].value

    data = {
        #"utf8": has_utf8,
        "commit:": "Sign in",
        "login": username,
        "password": password,
    }

    inputs = [ "authenticity_token", "return_to", "timestamp", "timestamp_secret" ]
    for inp in inputs:
        val = query('input[name=%s]' % inp)[0].value
        data[inp] = val

    req = session.post("https://github.com/session", data=data)
    if req.status_code == 200:
        if "adventofcode.com" in req.url.lower():
            return session

        print("Github auth failed but return code was 200")
        print("Try logging in from a browser, in case 2 factor auth is required")
    else:
        print("Github login attempt failed (bad request, code", req.status_code, ")")
    return None

def main():
    try:
        path = lib.cookies_path()
        with open(path, "wb") as cookies_file:
            username = input("Username:")
            password = getpass.getpass("Password:")
            session = auth_session(username, password)
            if session:
                pickle.dump(session.cookies, cookies_file)
                print("Wrote session cookies at ", path, "for", username)
                print("This file cannot be used to authenticate with Github, but do not make it public")
    except Exception as ex:
        print(ex, "Failed to write cookies to", path, file=sys.stderr)

if __name__ == "__main__":
    main()
