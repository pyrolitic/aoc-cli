# AOC CLI

Python based CLI client for [Advent of Code](https://adventofcode.com)

Currently, only github authentication is implemented.
Use `github_login.py` to login and store a `.cookies` file. I haven't tested what happens when the session expires - it can most likely be fixed by logging in again.

The cookies are stored as pickle of a `requests.Session.cookies` object. In theory any login method should work as long as they all generate the session cookie that the web browser uses.
