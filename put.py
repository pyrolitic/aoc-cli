#!/usr/bin/python2
import pickle, getpass, sys
import requests
import pyquery

def putAnswer(session, day, part, answer):
    data = {
        "level": part,
        "answer": answer
    }
    url = "https://adventofcode.com/2018/day/" + str(day) + "/answer"
    req = session.post(url, data = data)
    pq = pyquery.PyQuery(req.content)
    outcome = pq('article')[0].text_content()
    print outcome.encode('utf8')

def usage():
    print >>sys.stderr, "Usage: put.py <day> [part=1] <answer>"
    print >>sys.stderr, "day must be in range [1..25]"

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
            with open(".cookies", "rb") as f:
                s = requests.session()
                cookies = pickle.load(f)
                s.cookies.update(cookies)
                putAnswer(s, day, part, answer)
    else:
        usage()
