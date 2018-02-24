#!/usr/bin/env python2
import sys
import r2pipe
from colored import fg, bg, attr
import os

print fg(240)
r2 = r2pipe.open("./guessme")
r2.cmd("ood nmlkjihgfedcba")
r2.cmd("db 0x00400ff3")
dc = r2.cmd("dc")

i = 0
key = ""

while "type=dead" not in r2.cmd("di"):
    print fg(172) + attr("bold") + "===== LOOP", i, "=====" + attr(0) + fg(240)
    print dc
    eax = r2.cmd("dr eax")
    ebx = r2.cmd("dr ebx")
    print fg(154) + "EAX:", eax + fg(240)
    print fg(154) + "EBX:", ebx + fg(240)
    r2.cmd("dr ebx=" + eax)
    print fg(228) + "EBX set to", eax + fg(240)
    ebx = r2.cmd("dr eax")
    print fg(154) + "EBX:", ebx + fg(240)
    try:
         key += chr(int(ebx, 0) + 0x61)
    except ValueError:
        pass
    i += 1
    dc = r2.cmd("dc")

print fg(46) + "KEY={" + key + "}" + fg(240)
print fg(202) + attr("bold") + "\n" + "===== TESTING =====" + "\n" + attr(0)
print fg(245) + "./guessme", key + attr(0)
os.system("./guessme " + key)
