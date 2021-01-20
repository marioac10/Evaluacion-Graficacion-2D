#ROTACION 3D
#Mario Edmundo Ac Hernandez Fecha: 14/12/2020
#Mario Edmundo Ac Hernandez    Fecha: 14/12/2020
# Plotear dos rectangulos y dentro de uno de ellos un circulo
#Mi numero de control el 18390055 y mi ultimo digito es 5

import matplotlib.pyplot as plt 
import numpy as np

plt.axis([0,200,0,200])
plt.axis('on')
plt.grid(True)

xc=80
yc=100
r=25 #El ultimo digito de mi no. de control es 5 y lo multiplico por 5 y me da un radio de 25

p1=0*np.pi/180
p2=360*np.pi/180
dp=(p2-p1)/100
xlast=xc+r*np.cos(p1)
ylast=yc+r*np.sin(p1)
#Ploteamos el circulo
for p in np.arange(p1,p2+dp,dp):
    xp=xc+r*np.cos(p)
    yp=yc+r*np.sin(p)

    plt.plot([xlast,xp],[ylast,yp],c=(0/10,5/10,5/10))
    xlast=xp
    ylast=yp

#Creamos el rectangulo original con las coordenadas originales
xp1=0
xp2=0
xp3=100
xp4=100

yp1=0
yp2=-80
yp3=-80
yp4=0
#Ploteamos el rectangulo con respecto al centro del circulo
xg1=xp1+xc #Coordenas en Xg, Yg----> Sistema global
yg1=yp1+yc
xg2=xp2+xc #Coordenas en Xg, Yg----> Sistema global
yg2=yp2+yc
xg3=xp3+xc #Coordenas en Xg, Yg----> Sistema global
yg3=yp3+yc
xg4=xp4+xc #Coordenas en Xg, Yg----> Sistema global
yg4=yp4+yc

xg=np.array([xg1,xg2,xg3,xg4,xg1])
yg=np.array([yg1,yg2,yg3,yg4,yg1])
#Para definir el color usamos mis ultimos 3 digidos que son (055) divididos entre 10
plt.plot(xg,yg,color=(0/10,5/10,5/10))

#Ahora vamos a definir el segundo rectangulo donde el centro toque la esquina del primer rectangulo
dx=-50 #Trasladamos el rectangulo en el eje x en -50 
dy=40 #Trasladamos el rectangulo en el eje Y en 40 
xg+=dx
yg+=dy
plt.plot(xg,yg,color=(0/10,5/10,5/10)) #Ploteamos el rectangulo con el circulo adentro

plt.xlabel('X')
plt.ylabel('Y')
plt.show()