print('Esta aplicação converte velocidades em Km/h para Kt (Nós).')
print('----------------------------------------------------------')
def kmParaKt():
    knot = round((kmh/1.852),ndigits=2)
    print(f'A velocidade de {kmh}Km/h equivale a {knot}Kt.')

kmh = float(input('Informe a velocidade em Km/h: '))
kmParaKt()
print('----------------------------------------------------------')