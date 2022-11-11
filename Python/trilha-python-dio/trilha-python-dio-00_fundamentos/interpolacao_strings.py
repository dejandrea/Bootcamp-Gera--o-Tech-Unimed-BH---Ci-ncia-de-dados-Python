#método format

nome = "Andréa"
idade = 32
profissao = 'programador'
curso = 'python'

print('Olá, Me chamo {}, tenho {} anos, trabalho como {} e estou fazendo um curso de {}'.format(nome,idade,profissao,curso))

print('Olá, Me chamo {2}, tenho {0} anos, trabalho como {1} e estou fazendo um curso de {3}'.format(idade,profissao,nome,curso))

#f-string

print(f'Olá, Me chamo {nome}, tenho {idade} anos, trabalho como {profissao} e estou fazendo um curso de {curso}')

PI = 3.14159

print(f'O valor de PI é: {PI}')
print(f'O valor de PI é: {PI:.2f}')
print(f'O valor de PI é: {PI :10.2f}')