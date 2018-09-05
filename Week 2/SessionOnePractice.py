
import binascii
import base64


# Base64 is another way of representing a value.
# Webiste uses this to transmit data as it maintains the orignal value it meant to send. For example, the '+' symbol is treated differently in web URL, and therefore if you have a 
# complex data, it would be hard to send it over the web. Using encoding such as Base64 will allow the ease of transmission for web applications.

word = "abc"
encoded = base64.b64encode(bytes(word,"utf-8"))
print(encoded.decode('utf-8'))

decoded = base64.b64decode(encoded)
print(decoded.decode('utf-8'))


text = "def"
c = ""
for i in text:
	# print(hex(ord(i)))
	c += (hex(ord(i))).split('x')[1]

print(c)

unhex = bytes.fromhex(c).decode('utf-8')

print(unhex)



# This should be simple!
flag_one = "ZmxhZ3tIM2xsb19iYXNlNjR9"

# This as well!
flag_two = "666c61677b68336c6c6f5f74686572655f6833787d"

# Now how about thinking out of the box?
flag_three = "VmpJd2VFNUhSa2RpTTNCclVqSjRZVll3VlRGak1XUkZVMjVPVGxKdFpEVlVWbEpIWVZaT1IxTnVaRnBOUjFFd1dXdGFibVZzVm5WUmJXeFhUVlp2TWxkdGVFWlBWa0pTVUZRd1BRPT0="


	#### BONUS PRACTICE ####
# 8fa14cdd754f91cc6554c9e71929cce7
# 2db95e8e1a9267b7a1188556b2013b33
# 0cc175b9c0f1b6a831c399e269772661
# b2f5ff47436671b6e533d8dc3614845d
# f95b70fdc3088560732a5ac135644506
# 2510c39011c5be704182423e3a695e91
# e1671797c52e15f763380b45e841ec32
# 2db95e8e1a9267b7a1188556b2013b33
# 2db95e8e1a9267b7a1188556b2013b33
# d95679752134a2d9eb61dbd7b91c4bcc
# b14a7b8059d9c055954c92674ce60032
# e358efa489f58062f10dd7316b65649e
# 2510c39011c5be704182423e3a695e91
# 865c0c0b4ab0e063e5caa3387c1a8741
# 03c7c0ace395d80182db07ae2c30f034
# b14a7b8059d9c055954c92674ce60032
# 865c0c0b4ab0e063e5caa3387c1a8741
# 03c7c0ace395d80182db07ae2c30f034
# b14a7b8059d9c055954c92674ce60032
# 6f8f57715090da2632453988d9a1501b
# 8277e0910d750195b448797616e091ad
# e4da3b7fbbce2345d7772b0674a318d5
# cbb184dd8e05c9709e5dcaedaa0495cf
