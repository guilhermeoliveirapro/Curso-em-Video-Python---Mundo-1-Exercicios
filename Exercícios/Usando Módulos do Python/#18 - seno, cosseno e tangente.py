from math import radians, cos, tan, sin
an = float(input('digite o angulo que deseja: '))
seno = sin(radians(an))
cosseno = cos(radians(an))
tangente = tan(radians(an))
print('O ângulo de {} tem o SENO de {:.2f} \nO ãngulo de {} tem o COSSENO de {:.2f} \nO ângulo de {} tem a TANGENTE de {:.2f}'.format(an, seno, an, cosseno, an, tangente))


