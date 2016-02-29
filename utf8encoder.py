_author_ = 'weiwei'
import sys
import codecs
import struct

inputfile = open(sys.argv[1],'rb')
data = inputfile.read()
in_num = []
count = 0
for line in data:
    if count == 0:
        temp = hex(ord(line))[2:]
        if len(temp) < 2:
            temp = (2-len(temp))*'0' + temp
        count += 1
    elif count == 1:
        if len(hex(ord(line))[2:]) < 2:
            ttemp = (2-len(hex(ord(line))[2:]))*'0' + hex(ord(line))[2:]
            temp += ttemp

        else:
            temp += hex(ord(line))[2:]
        count = 0
        in_num.append(temp)


base = [str(x) for x in range(10)] + [chr(x) for x in range(ord('A'),ord('A')+6)]

'''dec2hex'''
def dec2hex(string):
    num = int(string)
    mid = []
    while True:
        if num == 0:
            break
        num,rem = divmod(num,16)
        mid.append((base[rem]))
    temp = ''.join([str(x) for x in mid[::-1]])
    return '0x'+temp

'''bin2dec'''
def bin2dec(string):
    return str(int(string,2))

'''bin2hex'''
def bin2hex(string):
    return dec2hex(bin2dec(string))

'''hex2dec'''
def hex2dec(string):
    return str(int(string.upper(),16))

'''dec2bin'''
def dec2bin(string_num):
    num = int(string_num)
    mid = []
    while True:
        if num == 0: break
        num,rem = divmod(num, 2)
        mid.append(base[rem])

    return ''.join([str(x) for x in mid[::-1]])


'''hex2bin'''
def hex2bin(string):
    return dec2bin(hex2dec(string.upper()))

# hex_num = []
# for line in ascii_num:
#     hex_num.append(dec2hex(line))
#
# hex_num_clean = []
# for i in hex_num:
#     if i != '0x':
#         hex_num_clean.append(i)


'''utf16 to utf8'''
def utf16Toutf8(i):
    if int(hex2dec(i)) <= int(hex2dec('7F')):
        # if len(i) < 4:
        #     i = '0x0' + i[2:]
        temp_1 = hex2bin(i)
        num = 7 - len(temp_1)
        temp_1 = num*'0' + temp_1
        utf ='0'+temp_1
    elif int(hex2dec('80')) <= int(hex2dec(i)) <= int(hex2dec('7FF')):
        # if len(i) == 4:
        #     i = '0x0' + i[2:4]
        temp_1 = hex2bin(i)
        num = 11 - len(temp_1)
        temp_1 = num*'0' + temp_1
        temp_2 = '110' + temp_1[0:5] + '10' + temp_1[5:]
        utf = temp_2
    elif int(hex2dec('800')) <= int(hex2dec(i)) <= int(hex2dec('FFFF')):
        # if len(i) == 5:
        #     i = '0x0' + i[2:]
        temp_1 = hex2bin(i)
        num = 16 - len(temp_1)
        temp_1 = num*'0' + temp_1
        temp_2 = '1110' + temp_1[0:4] + '10' + temp_1[4:10] + '10' +temp_1[10:]
        utf = temp_2
    return utf

out_num = []

for i in in_num:
    out_num.append(utf16Toutf8(i))


res = open('utf8encoder_out.txt','wb')
for word in out_num:
    if len(word) == 16:
        tmp1 = struct.pack('c',chr(int(word[0:8],2)))
        tmp2 = struct.pack('c',chr(int(word[8:16],2)))
        res.write(tmp1)
        res.write(tmp2)
    elif len(word) == 24:
        tmp1 = struct.pack('c',chr(int(word[0:8],2)))
        tmp2 = struct.pack('c',chr(int(word[8:16],2)))
        tmp3 = struct.pack('c',chr(int(word[16:24],2)))
        res.write(tmp1)
        res.write(tmp2)
        res.write(tmp3)
    else:
        tmp1 = struct.pack('c',chr(int(word,2)))
        res.write(tmp1)
res.close()

# print utf8list[0]
# utf8text = ''
# for i in utf8list:
#     utf8text += i
# print utf8text

# a = utf8text.decode('utf-8').encode('ascii')
# print az