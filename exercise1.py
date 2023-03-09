#!/usr/bin/env python3

from re import search
line = "May 27 11:45:40 ubuntu.local ticky: INFO: Created ticket [#1234] (username)"

print(search(r"ticky: INFO: ([\w ]*)", line))
print(search(r"ticky: ERROR: ([\w ]*)", line))
