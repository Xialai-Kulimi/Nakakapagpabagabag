import os
import hashlib
import struct as st

list(st.pack("B", 0))
def sha256(str):
    sha_signature = hashlib.sha256(str.encode()).hexdigest()
    return sha_signature


def hextoten(n):
    try:
        return int(n)
    except:
        return ord(n)-87


key = ''
real_key = key
inp_text = '我是大帥哥'
str_text = []

for i in range(len(bytes(inp_text, 'utf8'))):
    str_text.append(bytes(inp_text, 'utf8')[i])

# for i in range(len(inp_text)):
#     str_text.append(ord(inp_text[i]))
print()
print(str_text)
print('Orin:')

for i in str_text:
    print(st.pack('h', i), end='')

print()
print()


secret_text = []
# print(chr(str_text[0]))
print(str_text)
key_model = []
for n in range(32):
    key_model.append(16 * hextoten(sha256(key)[2 * n]) + hextoten(sha256(key)[(2 * n) + 1]))
print(key_model)

for i in range(int((len(str_text)/32)+1)):

    key = sha256(key)
    key_model = []
    for n in range(32):
        key_model.append(16 * hextoten(key[2 * n]) + hextoten(key[(2 * n) + 1]))

    for j in range(32):
        try:
            secret_text.append((key_model[j] + str_text[(i*32)+j]) % 256)
        except:
            secret_text.append(key_model[j] % 256)
print(secret_text)

print('Encode:')

ans_text = []
for i in secret_text:
    print(chr(i), end='')
    ans_text.append(i)

# print(ans_text+'\n')
print()

print(ans_text)

key = real_key
key_model = []

for n in range(32):
    key_model.append(16 * hextoten(sha256(key)[2 * n]) + hextoten(sha256(key)[(2 * n) + 1]))
print(key_model)
orin_text = []

for i in range(int(len(ans_text)/32)):
    key = sha256(key)
    key_model = []

    for n in range(32):  # generate the dynamic key
        key_model.append(16 * hextoten(key[2 * n]) + hextoten(key[(2 * n) + 1]))

    for j in range(32):
        orin_text.append((ans_text[(i*32) + j] - key_model[j]) % 256)


print(orin_text)

ans_text = b''

print('Decode:')

for i in orin_text:
    print(bytes(i), end='')
    ans_text = ans_text + bytes(i)
print()
print(str(ans_text, 'utf8'))