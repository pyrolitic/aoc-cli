#!/usr/bin/python3
import pickle, getpass, sys
import requests
import pyquery

import lib

def put_answer(session, day, part, answer):
    data = {
        "level": part,
        "answer": answer
    }
    url = "https://adventofcode.com/%d/day/%d/answer" % (lib.current_year(), day)
    req = session.post(url, data = data)
    pq = pyquery.PyQuery(req.content)
    outcome = pq('article')[0].text_content()
    print(outcome)

def usage():
    print("Usage: put.py <day> [part=1] <answer>", file=sys.stderr)
    print("day must be in range [1..25]", file=sys.stderr)

if __name__ == "__main__":
    if 3 <= len(sys.argv) <= 4:
        day = int(sys.argv[1])
        if len(sys.argv) == 3:
            part = 1
            answer = sys.argv[2]
        else:
            part = int(sys.argv[2])
            answer = sys.argv[3]

        opts = ("text", "input",)
        if not 1 <= day <= 25:
            usage()
        else:
            s = lib.restore_session()
            if s:
                put_answer(s, day, part, answer)
    else:
        usage()
