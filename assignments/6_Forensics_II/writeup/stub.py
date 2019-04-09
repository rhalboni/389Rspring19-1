#!/usr/bin/env python2

import sys
import struct
import datetime 

# You can use this method to exit on failure conditions.
def bork(msg):
    sys.exit(msg)


# Some constants. You shouldn't need to change these.
MAGIC = 0x8badf00d
VERSION = 1

if len(sys.argv) < 2:
    sys.exit("Usage: python stub.py input_file.fpff")

# Normally we'd parse a stream to save memory, but the FPFF files in this
# assignment are relatively small.
with open(sys.argv[1], 'rb') as fpff:
    data = fpff.read()

# Hint: struct.unpack will be VERY useful.
# Hint: you might find it easier to use an index/offset variable than
# hardcoding ranges like 0:8
magic, version = struct.unpack("<LL", data[0:8])
time,_ = struct.unpack("<LL", data[8:16])
author= struct.unpack("<8s", data[12:20])
sec_count,_ = struct.unpack("<LL", data[20: 28])
timestamp = datetime.datetime.fromtimestamp(time)
i = 0
if magic != MAGIC:
    bork("Bad magic! Got %s, expected %s" % (hex(magic), hex(MAGIC)))

if version != VERSION:
    bork("Bad version! Got %d, expected %d" % (int(version), int(VERSION)))

print("------- HEADER -------")
print("MAGIC: %s" % hex(magic))
print("VERSION: %d" % int(version))
print("Time: %s" % str(timestamp))
print("Author: %s" % author )
print("Num of Sections: %d" % int(sec_count))
# We've parsed the magic and version out for you, but you're responsible for
# the rest of the header and the actual FPFF body. Good luck!
offset = 24
print("-------  BODY  -------")
while i < int(sec_count):
	stype, slen = struct.unpack("<LL", data[offset:offset+8])
	print("------- Section %d: --------" % (i+1))
	print("Section Type: %s" % hex(stype))
	print("Section Length: %s" % (slen))
	if stype == 0x1:
		sval = struct.unpack("<" + str(slen) + "s", data[offset+8:offset+8+slen])
		print("Section Value: %s" % sval[0])
	elif stype == 0x2:
		sval = struct.unpack("<" + str(slen) + "s", data[offset+8:offset+8+slen])
		print("Section Value: %s" % sval[0])
	elif stype == 0x3:
		length = slen / 4
		sval = struct.unpack("<" + str(length) + "L", data[offset+8:offset+8+length])
		print("Section Value: %d" % sval)
	elif stype == 0x4:
		length = slen / 8
		sval = struct.unpack("<" + str(length) + "Q", data[offset+8:offset+8+length])
		print("Section Value: %d" % sval[0])
	elif stype == 0x5:
		length = slen / 8
		sval = struct.unpack("<" + str(length) + "Q", data[offset+8:offset+8+length])
		print("Section Value: %d" % sval[0])
	elif stype == 0x6:
		if slen == 16:
			sval = struct.unpack("<QQ", data[offset+8:offset+8 + slen])
			print("Section Value: " + str(sval) )
		else:		
			bork("Bad slen! Got %d, expected %d" % (int(slen), int(16)))
	elif stype == 0x7:
		if slen == 4:
			sval = struct.unpack("<L", data[offset+8:offset+8 + slen])
			if sval < 0 or sval > sec_count:
				bork("Bad sval! Got %d, expected 0 to %d" % (int(sval), int(sec_count -1)))
			print("Section Value" + sval)
		else:		
			bork("Bad slen! Got %d, expected %d" % (int(slen), int(4)))
	elif stype == 0x8:
		sval = struct.unpack("<" + str(slen) + "s", data[offset+8:offset+8+slen])
		code = struct.pack('8L', 137,80,78,71,13,10,26,10)
		png = code + data
	elif stype == 0x9:
		sval = struct.unpack("<" + str(slen) + "s", data[offset+8:offset+8+slen])
		code = struct.pack('6L', 'G','I','F','8','7','a')
		GIF = code + data
	elif stype == 0xA:
		sval = struct.unpack("<" + str(slen) + "s", data[offset+8:offset+8+slen])
		code = struct.pack('6L', 'G','I','F','8','9','a')
		GIF = code + data
	else:
		bork("Bad stype! Got %d, expected %d" % (int(slen) ))
	offset += 8 + slen 	
	i+=1
