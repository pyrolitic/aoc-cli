import pickle, getpass, sys
import requests
import pyquery

def putAnswer(session, day, answer):
    data = {
        "level": str(day),
        "answer": answer
    }
    r = session.post("https://adventofcode.com/2018/day/" + str(day) + "/answer", data = data)
    pq = pyquery.PyQuery(r.content)
    outcome = pq('article')[0].text_content()
    print outcome

def usage():
    print >>sys.stderr, "Usage: put.py <day> <answer>"
    print >>sys.stderr, "day must be in range [1..25]"

if __name__ == "__main__":
    if len(sys.argv) == 3:
        day = int(sys.argv[1])
        answer = sys.argv[2]

        opts = ("text", "input",)
        if not 1 <= day <= 25:
            usage()
        else:
            with open(".cookies", "rb") as f:
                s = requests.session()
                cookies = pickle.load(f)
                s.cookies.update(cookies)
                putAnswer(s, day, answer)
    else:
        usage()
