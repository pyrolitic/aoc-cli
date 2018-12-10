#!/usr/bin/python2
import pickle, getpass, sys
import requests
import pyquery

import lib

opts = ("text", "input",)

def print_input(session, day, opt):
    if opt == "text":
        r = session.get("https://adventofcode.com/2018/day/" + str(day))
        pq = pyquery.PyQuery(r.content)
        parts =  pq('article.day-desc')
        for i, part in enumerate(parts):
            print ">>>>>>>>>>>>>>>>>> Part %d <<<<<<<<<<<<<<<<<" % (i + 1)
            text = part.text_content()
            print text.encode('utf8')
    elif opt == "input":
        # seems to be one input for all parts
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
            s = lib.restore_session()
            if s:
                print_input(s, day, opt)
    else:
        usage()
