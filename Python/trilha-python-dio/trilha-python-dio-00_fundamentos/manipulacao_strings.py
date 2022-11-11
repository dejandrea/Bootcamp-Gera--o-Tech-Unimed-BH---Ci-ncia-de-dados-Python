from ctypes import create_unicode_buffer
from itertools import count


curso = '   Curso de PyThon    '

print(curso)
print(len(curso))

#fatiamento

print(curso[9])
print(curso[9:13])
print(curso[9:21:2])
print(curso[:5])
print(curso[12:])
print(curso[9::3])

print(curso.count('o'))
print(curso.count('o',0,13))
print(curso.find('Curso'))
print(curso.find('oi'))
print('Curso' in curso)


#transformação

print(curso.replace('Curso','Aulas'))
print(curso.upper())
print(curso.lower())
print(curso.capitalize())
print(curso.title())
print(curso.strip())
print(curso.rstrip())
print(curso.lstrip())
#divisão
print(curso.split())

#Junção
print('.'.join(curso))

#centralização

print(curso.center(30,"#"))

