#!usr/bin/env python3

foo = open("dracula.txt", "r")
bar = open("vampytime.txt", "w")

vamp_line_count = 0


for line in foo:
    if "vampire" in line.lower():
        vamp_line_count += 1
        bar.write(line)
        
print(vamp_line_count)
