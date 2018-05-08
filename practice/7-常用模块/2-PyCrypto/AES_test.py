# -*- coding:utf-8 -*-
'''
AES 是 Advanced Encryption Standard 的缩写，高级加密标准，是目前非常流行的加密算法之一
'''

from Crypto.Cipher import AES
from Crypto.Random import random


# 加密

# “This is a key123”为 key，长度有着严格的要求，必须为 16、24 或 32 位，否则会报错
# “This is an IV456”为 VI，长度要求更加严格，只能为 16 位，否则会报错
obj = AES.new('This is a key123', AES.MODE_CBC, 'This is an IV456')
message = "The answer is no"
ciphertext = obj.encrypt(message)
print(ciphertext)


# 解密

# 如果 key 和 VI 错误将无法得到正确的字符串。例如，把 key 修改为:'This is a key888'，解密失败，会得到另一个加密字符串
obj2 = AES.new('This is a key123', AES.MODE_CBC, 'This is an IV456')
s = obj2.decrypt(ciphertext)
print(s)


# 随机算法
r = random.choice(['dogs', 'cats', 'bears'])
print(r)