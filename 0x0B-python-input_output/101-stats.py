#!/usr/bin/python3
"""the func"""
import sys


status_codes = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0
    }
file_size = 0
count = 0
try:
    for line in sys.stdin:
        if count != 0 and count % 10 == 0:
            print("File size: {:d}".format(file_size))
            for g, h in status_codes.items():
                if h != 0:
                    print("{}: {:d}".format(g, h))
        split = line.split()
        for a, b in status_codes.items():
            if str(a) == str(split[-2]):
                status_codes[a] = int(b) + 1
        file_size += int(split[-1])
        count += 1
except KeyboardInterrupt:
    print("File size: {:d}".format(file_size))
    for g, h in status_codes.items():
        if h != 0:
            print("{}: {:d}".format(g, h))
    raise
