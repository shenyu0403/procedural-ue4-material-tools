from os import system
import sys
s="0123456789ABCDEFGHIJKLMNOPQSRTUVWXYZ-"
for i in s:
	system("./msdfgen -size 128 128 -scale 6 -font %s %i -o %s_%i.png"%(sys.argv[1],ord(i),sys.argv[1],ord(i)))
