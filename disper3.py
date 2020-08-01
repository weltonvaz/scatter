# funcoes usadas dos pacotes numpy e matplotlib

from matplotlib import pyplot
from math import sqrt, radians
from math import sin, cos
import csv

# constantes
phi = 1.168034
ang = 360/phi
angle = 360 - ang

# listas
dados1 = []
dados2 = []

# prepação:

with open('data1.csv', 'r') as arquivo_csv:
    leitor = csv.reader(arquivo_csv, delimiter='\n')
    for x in leitor:
        dados1.append(x)


with open('data2.csv', 'r') as arquivo_csv:
    leitor = csv.reader(arquivo_csv, delimiter='\n')
    for y in leitor:
        dados2.append(y)

# plot
pyplot.scatter(dados1, dados2)
pyplot.title('Gráfico de Dispersão entre data1 e data2')
pyplot.show()
