#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    if len(sys.argv) == 1:
        print("0 arguments.")
    else:
        n = len(sys.argv) - 1
        print("{:d} arguments:".format(n))
        for x in range(1, n + 1):
            print("{}: {}".format(x, sys.argv[x]))
