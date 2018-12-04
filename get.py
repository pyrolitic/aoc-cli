import pickle, getpass, sys
import requests
import pyquery

opts = ("text", "input",)

def printInput(session, day, opt):
    if opt == "text":
        r = session.get("https://adventofcode.com/2018/day/" + str(day))
        pq = pyquery.PyQuery(r.content)
        text = pq('article')[0].text_content()
        print text
    elif opt == "input":
        r = session.get("https://adventofcode.com/2018/day/" + str(day) + "/input")
        print r.content

def usage():
    print >>sys.stderr, "Usage: {" + ','.join(opts) + "} <day>"
    print >>sys.stderr, "day must be in range [1..25]"

if __name__ == "__main__":
    if len(sys.argv) == 3:
        opt = sys.argv[1].lower()
        day = int(sys.argv[2])

        if not ( opt in opts and 1 <= day <= 25 ):
            usage()
        else:
            with open(".cookies", "rb") as f:
                s = requests.session()
                cookies = pickle.load(f)
                s.cookies.update(cookies)
                printInput(s, day, opt)
    else:
        usage()
