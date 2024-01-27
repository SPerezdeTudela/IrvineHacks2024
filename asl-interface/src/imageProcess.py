#With help from stack overflow

import fileinput

def getData():
    try:
        for line in fileinput.input():
            image += line

    except OSError:
        print("Found OSError")


