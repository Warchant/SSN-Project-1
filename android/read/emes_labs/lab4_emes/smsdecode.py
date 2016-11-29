#
# Python code to decode SMS PDU, some code from
# http://www.monkeysandrobots.com/archives/207
#

# Reading binary file in Python
# http://stackoverflow.com/questions/1035340/reading-binary-file-in-python
#
# Convert string to hex
# http://code.activestate.com/recipes/496969/
#
# Modules (definitions and statements) are imported by the import statement
from binascii import unhexlify, hexlify
from cStringIO import StringIO
from itertools import cycle  # *
from math import ceil
import os
import sys  # for argv etc.


# The following table will map GSM character codes to their latin1 equivalent:
gsm_to_latin1 = [64, 163, 36, 165, 232, 233, 249, 236, 242, 199, 10, 216, 248, 13, 
                 197, 229, 16, 95, 32, 32, 32, 32, 32, 32, 32, 32, 32, 27, 198, 230, 
                 223, 201, 32, 33, 34, 35, 164, 37, 38, 39, 40, 41, 42, 43, 44, 45, 
                 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 
                 63, 161, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 
                 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 196, 214, 209, 220, 167, 
                 191, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 
                 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 228, 246, 
                 241, 252, 224, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 
                 32, 32, 32, 32, 32, 32, 94, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 
                 32, 32, 32, 32, 32, 32, 32, 32, 123, 125, 32, 32, 32, 32, 32, 92, 32, 32, 
                 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 91, 126, 93, 32, 124, 32, 32, 32, 
                 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 
                 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 
                 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 
                 32, 32, 32, 32, 32, 32]

# This is suitable for SE W800i
class PDU(object):
    def decode(self, s, status):
        s = unhexlify(s)
        d = StringIO(s)

        # parse SMSC information
        p = {}
#The very first byte of a standards-based SMS is the status of the message which could 
#be 00 (deleted), 01 (read), 03 (unread), 05 (sent) or 07 (unsent).
        if status == "01": # received SMS
            p['sms_status'] = d.read(1)
            p['smsc_len'] = d.read(1)
            p['type_of_address'] = d.read(1)
            p['sc_num'] = self.unsemi(d.read(ord(p['smsc_len'])-1))
            
            p['msg_type'] = d.read(1)
            p['address_len'] = d.read(1)
            p['type_of_address'] = d.read(1)
            
            p['sender_num'] = self.unsemi(d.read(int(ceil(ord(p['address_len'])/2.0))))
            p['pid'] = d.read(1)
            p['dcs'] = d.read(1)
            p['ts'] = d.read(7)
            p['udl'] = d.read(1)
            p['user_data'] = d.read(ord(p['udl']))
            if p['dcs'] == '\x00':    # gsm 7bit
                p['user_data'] = self.decode_user_data(p['user_data'])
            
        elif status == "05": # sent SMS
            p['sms_status'] = d.read(1)
            p['smsc_len'] = d.read(1)
            p['type_of_address'] = d.read(1)
            p['sc_num'] = self.unsemi(d.read(ord(p['smsc_len'])-1))
            
            p['msg_type'] = d.read(1)
            p['msg_reference'] = d.read(1)
            p['address_len'] = d.read(1)
            p['type_of_address'] = d.read(1)
            
            p['sender_num'] = self.unsemi(d.read(int(ceil(ord(p['address_len'])/2.0))))
            p['pid'] = d.read(1)
            p['dcs'] = d.read(1)
            p['validity_period'] = d.read(1)
            p['udl'] = d.read(1)
            p['user_data'] = d.read(ord(p['udl']))
            if p['dcs'] == '\x00':    # gsm 7bit
                p['user_data'] = self.decode_user_data(p['user_data'])
        
        return p

    def decode_user_data(self, s):
        """PDU user data is stored in a strange 7-bit packed format"""
        bytes = map(ord, s)
        strips = cycle(range(1,9))
        out = ""
        c = 0    # carry
        clen = 0 # carry length in bits
        while len(bytes):
            strip = strips.next()
            if strip == 8:
                byte = 0
                ms = 0
                ls = 0
            else:
                byte = bytes.pop(0)
                # take strip bytes off the top
                ms = byte >> (8-strip)
                ls = byte & (0xff >> strip)
                #print "%d byte %x ms %x ls %x" % (strip, byte, ms, ls)
                
            # append the previous
            byte = ((ls << clen) | c) & 0xff
            # out += chr(byte)
            out += chr(gsm_to_latin1[byte]) # changed Colm O'Shea

            c = ms
            clen = strip % 8

        if strip == 7:
            out += chr(ls) # changed 6/11/09 to incorporate Carl's suggestion in comments'
            
        return out

    def unsemi(self, s):
        """turn PDU semi-octets into a string"""
        l = list(hexlify(s))
        out = ""
        while len(l):
            out += l.pop(1)
            out += l.pop(0)
        return out

# end class PDU

def byteSwap(byte):
    """
    Swap the first and second digit position inside a hex byte
    """
    return "%c%c" % (byte[1], byte[0])

def parseTimeStamp(hextime):
    # put every nibble in a byte
    time = hexlify(hextime)
    """
    Convert the time from PDU format to some common format
    """
    y = byteSwap(time[0:2])
    m = byteSwap(time[2:4])
    d = byteSwap(time[4:6])

    hour = byteSwap(time[6:8])
    min = byteSwap(time[8:10])
    sec = byteSwap(time[10:12])

    if int(y) < 70:
        y = "20" + y

    return "%s.%s.%s %s:%s" % (y, m, d, hour, min)

# test decoding of full PDU including message status from a phone image
# status 01
s = "0107916407058099f9040b916407158906f50000013040013090402b5474d8bd9e83da6177089404ddd36c36885c36a7dd697a999d078dd1e5f11a94a683de75ba0b"
# status 05
#s = "0507916407058099f911510a8170203234700000ff09c8b21a847ec3e121"

status = s[:2]
pdu = PDU()
sms = pdu.decode(s, status)
print sms

if status == "01":
    print "\nFrom: " + sms.get('sender_num') + ", Timestamp: " + parseTimeStamp(sms.get('ts')) + ", Message: " + sms.get('user_data')
elif status == "05":
    print "\nBy: " + sms.get('sender_num') + ", Message: " + sms.get('user_data')
 