__author__ = 'weiweiduan'
import sys


inputfile = open('arabic_in.txt','rb')
data = inputfile.read()
in_num = []
count = 0
for line in data:
    if count == 0:
        temp = hex(ord(line))[2:]
        count += 1
    elif count == 1:
        temp += hex(ord(line))[2:]
        count = 0
        in_num.append(temp)
for i in in_num:
    print i


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
print "after"
for i in in_num:
    out_num.append(utf16Toutf8(i))
for i in out_num:
    print i
# print utf8list[0]
# utf8text = ''
# for i in utf8list:
#     utf8text += i
# print utf8text

# a = utf8text.decode('utf-8').encode('ascii')
# print a