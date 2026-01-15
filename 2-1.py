#!/usr/bin/env python
import sys
def repeater(s):
    # Concatenate string with itself, then find the first occurrence
    # of the original string starting from index 1
    doubled_s = s + s
    # We slice [1:-1] in some implementations to ensure we don't just find
    # the original string at the original position or at the very end
    # A cleaner approach uses index directly:
    try:
        # Check if original string is found in the middle portion of doubled string
        i = doubled_s.index(s, 1, len(s) + 1)
        # If found, the length of the period is 'i', and s[:i] is the pattern
        return s[:i]
    except ValueError:
        # If not found, the entire string is the pattern
        return s

        #pass

print(repeater(sys.argv[1:]))
#print(repeater('abab'))  # Output: ab
#print(repeater('abcabcabc')) # Output: abc
#print(repeater('aba'))   # Output: aba
