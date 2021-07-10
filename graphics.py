import matplotlib.pyplot as plt

#Lista os valores de faturamento entre 2016 e 2022
faturamento = [48660.06,43270.91,63005.16,64332.06,89808.29,90770.10,84165.96]
#Lista os valores de faturamento médio mensal entre 2016 e 2022
fatMedio = [4055.01,3605.91,5250.43,5361.01,7484.02,7564.18,7013.83]
#Define o eixo x para o tempo
x=[2016,2017,2018,2019,2020,2021,2022]
#Definie o eixo y para os valores
y=faturamento
y2=fatMedio

#Gera o gráfico
plt.plot(x,y,marker='o', color='#0051FF')
plt.plot(x,y2,marker='o', color='#FF9E00')

#Rótulos do gráfico
plt.title('Evolução do Faturamento')
plt.xlabel('Anos')
plt.ylabel('Faturamento em R$')

#Legenda
plt.legend(['Faturamento Anual', 'Média Mensal'], loc=0)

#Exibir, Definir cor, Estilo da linha, Espessura da linha, Primárias e secundárias, Quais linhas
plt.grid(True, color='#d6d6d6', linestyle='-', linewidth='0.3',which='both', axis='y')

#Salva uma imagem PNG do gráfico
plt.savefig('evolucao-do-faturamento.png',dpi=300)
plt.show()
