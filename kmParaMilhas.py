print('Esta aplicação converte velocidades em Km/h para Mph (milhas por hora).')
print('-----------------------------------------------------------------------')
def kmhMph():
    mph = round((kmh/1.609),ndigits=2)
    print(f'A velocidade de {kmh}Km/h equivale a {mph}Mph.')

kmh = float(input('Informe a velocidade em Km/h: '))
kmhMph()
print('-----------------------------------------------------------------------')