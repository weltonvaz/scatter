# funcoes usadas dos pacotes numpy e matplotlib

from matplotlib import pyplot
from math import sqrt, radians
from math import sin, cos

# constantes
phi = 1.168034
ang = 360/phi
angle = 360 - ang

# prepação:

index = [x for x in range(1056) if x % 2 != 0]
delta = [sqrt(x) for x in index]

# =D2+$A$3
theta = [t + angle for t in index]

# =C3*COS(RADIANOS(D3))
data1 = [delta[i-1] * cos(radians(theta[i])) for i,d in enumerate(delta)]
# =C3*SEN(RADIANOS(D3))
data2 = [delta[i-1] * sin(radians(theta[i])) for i,d in enumerate(delta)]

# plot
pyplot.scatter(data1, data2)
pyplot.title('Gráfico de Dispersão entre data1 e data2')
pyplot.show()
