#!/usr/bin/env python

import sys


# When the parent dies we are seeing continual newlines, so we only access so many before stopping
counter = 0

if True:
    while True:
        try:
            line = sys.stdin.readline().strip()
            if line == "":
                counter += 1
                if counter > 100:
                    break
                continue
            #raise Exception(line)
            counter = 0
            with open("/tmp/exabgproutes", "a+") as myfile:
                myfile.write(line)
                myfile.write("\n")
        except KeyboardInterrupt:
            pass
        except IOError:
            # most likely a signal during readline
            pass
