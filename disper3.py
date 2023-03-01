# funcoes usadas dos pacotes numpy e matplotlib

from mpl_toolkits import mplot3d 
from matplotlib import pyplot
from math import sqrt, radians
from math import sin, cos, tan
import csv

# constantes
phi = 1.168034
ang = 360/phi
angle = 360 - ang

# prepação:

index = [x for x in range(1024) if x % 2 != 0]
delta = [sqrt(x) for x in index]

# =D2+$A$3
theta = [t + angle for t in index]

# =C3*COS(RADIANOS(D3))
data1 = [delta[i] * cos(radians(theta[i])) for i,d in enumerate(delta)]
# =C3*SEN(RADIANOS(D3))
data2 = [delta[i] * sin(radians(theta[i])) for i,d in enumerate(delta)]
# =C3*TAN(RADIANOS(D3))
data3 = [delta[i] * tan(radians(theta[i])) for i,d in enumerate(delta)]

# Criando figura 
fig = pyplot.figure(figsize = (10, 7)) 
ax = pyplot.axes(projection ="3d") 

# plot
ax.scatter3D(data1, data2, data3)
pyplot.title('Gráfico de Dispersão 3D - entre data1, data2 e data3')
pyplot.show()
