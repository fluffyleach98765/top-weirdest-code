import codecs

code = '''
cevag("Uryyb jbeyq yby")
'''

rot13_decoded = codecs.decode(code, 'rot13')
eval(rot13_decoded)
