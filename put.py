#!/usr/bin/python3

import sys
import pyquery

import lib

def put_answer(session, day, part, answer):
    data = {
        "level": part,
        "answer": answer
    }
    url = "https://adventofcode.com/%d/day/%d/answer" % (lib.current_year(), day)
    req = session.post(url, data=data)
    query = pyquery.PyQuery(req.content)
    outcome = query('article')[0].text_content()
    print(outcome)

def usage():
    print("Usage: put.py <day> [part=1] <answer>", file=sys.stderr)
    print("day must be in range [1..25]", file=sys.stderr)

def main():
    if 3 <= len(sys.argv) <= 4:
        day = int(sys.argv[1])
        if len(sys.argv) == 3:
            part = 1
            answer = sys.argv[2]
        else:
            part = int(sys.argv[2])
            answer = sys.argv[3]

        if not 1 <= day <= 25:
            usage()
        else:
            session = lib.restore_session()
            if session:
                put_answer(session, day, part, answer)
    else:
        usage()

if __name__ == "__main__":
    main()
