p1 = float(input('qual o preço do produto que deseja? R$ '))
p2 = (5/100*p1)
p3 = (p1 - p2)
print('este produto que custava R${}, na promoção com 5% de desconto custará R${:.2f}'.format(p1, p3))

