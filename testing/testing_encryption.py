from base64 import b64decode, b64encode

string = b"naivedyakhare"
x = b64encode(string)
y = b64decode(x)
print(y)

x = {"password": "abc"}
password = bytes(x["password"], encoding="utf-8")
print(b64encode(password))

from hashlib import blake2s

key1 = b"abcd"
key2 = b"abc"
data = b"naivedyakhare"
hashed1 = blake2s(data, key = key1).digest()
hashed2 = blake2s(data, key = key2).digest()

print(hashed1 == hashed2)

print(hashed1)

from hashlib import blake2s

x = bytes("abcd", encoding="utf-8")
print(x)