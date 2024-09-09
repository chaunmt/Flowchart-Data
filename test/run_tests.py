"""
This is just a test file.
"""

s = "[(csci 1913 or csci 1933) and csci 2011] or instr consent or grad standing"
s = s.replace('(', '[')
s = s.replace(')', ']')
print(s)