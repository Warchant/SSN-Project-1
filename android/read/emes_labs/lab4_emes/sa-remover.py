#!/usr/bin/python
import struct
import sys

f = open('se-nand.bin', 'rb')
w = file('new-nand.bin', 'wb')
n = file('spare.bin', 'wb')

inputfile  = sys.argv[1]
sectorsize = int(sys.argv[2])
sparearea = int(sys.argv[3])
#header = int(sys.argv[4])
#footer = int(sys.argv[5])

print sectorsize
print sparearea
print header
print footer

with open(inputfile, 'rb') as a_file:
	nn = a_file.read(sectorsize)
	while nn != "":
		w.write(nn)
		sa = a_file.read(sparearea)
		n.write(sa)
		nn = a_file.read(sectorsize)
w.close()
n.close()
