#!/usr/bin/python3

import sys
import pyquery

import lib

OPTS = ("text", "input",)

def print_input(session, day, opt):
    if opt == "text":
        req = session.get("https://adventofcode.com/%d/day/%d" % (lib.current_year(), day))
        query = pyquery.PyQuery(req.content)
        parts = query('article.day-desc')
        for i, part in enumerate(parts):
            print(">>>>>>>>>>>>>>>>>> Part %d <<<<<<<<<<<<<<<<<" % (i + 1))
            text = part.text_content()
            print(text)
    elif opt == "input":
        # seems to be one input for all parts
        req = session.get("https://adventofcode.com/%d/day/%d/input" % (lib.current_year(), day))
        text = req.content.decode('utf8').rstrip('\n')
        print(text)

def usage():
    print("Usage: {" + ','.join(OPTS) + "} <day>", file=sys.stderr)
    print("day must be in range [1..25]", file=sys.stderr)

def main():
    if len(sys.argv) == 3:
        opt = sys.argv[1].lower()
        day = int(sys.argv[2])

        if not (opt in OPTS and 1 <= day <= 25):
            usage()
        else:
            session = lib.restore_session()
            if session:
                print_input(session, day, opt)
    else:
        usage()

if __name__ == "__main__":
    main()
