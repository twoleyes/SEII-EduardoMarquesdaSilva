#!/usr/bin/python3

import urllib.request

ex1 = 'http://www.blankwebsite.com/'
ex2 = 'http://www.python.org/'

print('Conteudo da pagina:\n\n')

with urllib.request.urlopen(ex1) as f:
	print(f.read(1000).decode('utf-8')) #primeiros 1000 bytes

print('\n')







