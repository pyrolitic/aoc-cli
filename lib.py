#!/usr/bin/python2

import sys
import os
import os.path
import pickle
import requests
import datetime

def current_year():
    return datetime.datetime.now().year

def cookies_path():
    return os.path.expanduser("~/.aoc.cookies")

def restore_session():
    fp = cookies_path()
    if os.path.isfile(fp):
        try:
            f = open(fp, "rb")
            s = requests.session()
            cookies = pickle.load(f)
            s.cookies.update(cookies)
            f.close()
            return s
        except Exception as e:
            print("Failed to restore saved session from", fp, file=sys.stderr)
            print(e, file=sys.stderr)
    else:
        print("No saved session found at", fp, file=sys.stderr)
        print("Run github_login.py first", file=sys.stderr)
        return None

