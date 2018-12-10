#!/usr/bin/python2

import sys
import os
import os.path
import pickle
import requests

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
            print >>sys.stderr, "Failed to restore saved session from", fp
            print >>sys.stderr, e
    else:
        print >>sys.stderr, "No saved session found at", fp
        print >>sys.stderr, "Run github_login.py first"
        return None

