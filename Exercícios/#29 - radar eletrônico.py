vel = float(input('Qual é a velocidade atual do carro? '))
multa = 7*vel-560
azul = '\033[36m'
if vel >80:
    print('MULTADO! Você excedeu o limite permitido que é de 80Km/h. Você deve pagar uma multa de {}R$'.format(multa))
print(f'{azul}Dirija com segurança e tenha um bom dia')
