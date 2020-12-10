#!/usr/bin/python3

import sys
import os
import os.path
import pickle
import datetime
import requests

def current_year():
    return datetime.datetime.now().year

def cookies_path():
    return os.path.expanduser("~/.aoc.cookies")

def restore_session():
    path = cookies_path()
    if os.path.isfile(path):
        try:
            with open(path, "rb") as cookies_file:
                session = requests.session()
                cookies = pickle.load(cookies_file)
                session.cookies.update(cookies)
                return session
        except Exception as ex:
            print("Failed to restore saved session from", path, file=sys.stderr)
            print(ex, file=sys.stderr)
    else:
        print("No saved session found at", path, file=sys.stderr)
        print("Run github_login.py first", file=sys.stderr)
        return None
