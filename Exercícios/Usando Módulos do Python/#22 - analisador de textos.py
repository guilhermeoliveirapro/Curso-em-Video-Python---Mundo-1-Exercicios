nome = input('digite o seu nome: ')
frase = nome
print('Analisando seu nome...')
print('Seu nome em maiúsculas é {}'.format((frase.upper())))
print('Seu nome em minúsculas é {}'.format((frase.lower())))
esp = frase.replace(' ', '')
print('seu nome tem ao todo {} letras'.format((len(esp))))
dividido = frase.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(dividido[0], len(dividido[0])))





