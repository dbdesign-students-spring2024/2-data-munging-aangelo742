# Place code below to do the munging part of this assignment.
import re
file = open('data\GLB.Ts+dSST.txt', 'r')

lines_seen_so_far = set()

for line in file:
    line = line.strip()
    if len(line) != 0 and line not in lines_seen_so_far:
        #print(line)
        new_line = re.sub("\s+", ",", line)
        print(new_line)
        lines_seen_so_far.add(line)