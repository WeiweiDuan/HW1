import codecs
import struct
data = open("arabic_in.txt",'rb').read()
result = data
#result = data.decode("utf-8")
print hex(ord(result[0]))
print hex(ord(result[1]))
print hex(ord(result[2]))
print hex(ord(result[3]))
print hex(ord(result[3]))
print hex(ord(result[3]))
print hex(ord(result[3]))

print ord(data[1])
