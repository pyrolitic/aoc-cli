# Advent of code CLI

Python3 based CLI client for [Advent of Code](https://adventofcode.com).
Authenticate, then use `get.py text <day>` and `get.py input <day>` to print the problem description or input data, respectively, to stdout.
Use `put.py <day> [part=1] <answer>` to try to submit and answer attempt.

Currently, only github authentication is implemented.
Use `github_login.py` to login and store a `.cookies` file. This will save a session key for Advent of Code, not Github. Even if it is stolen, it should only grant temporary access to you account on AOC. I haven't tested what happens when the session expires - it can most likely be fixed by logging in again.

The cookies are stored as pickle of a `requests.Session.cookies` object. In theory any login method should work as long as it generates the session cookie as done by a browser.
