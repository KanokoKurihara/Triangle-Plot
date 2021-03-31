import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import mpl_toolkits.mplot3d.art3d as art3d

fig=plt.figure(figsize=(5,5))
ax=fig.add_subplot(111,projection='3d')

h = np.sqrt(3.0)*0.5

for i in range(0,20):
    for j in range(0,20-i):
      x1=[i/40+j/20,i/40+(j+1)/20,i/40+(j+1)/20,i/40+j/20]
      y1=[i*h/20,i*h/20,i*h/20,i*h/20]
      z1=[0,0,1,1]
      poly1=list(zip(x1,y1,z1))
      ax.add_collection3d(art3d.Poly3DCollection([poly1],facecolors='m',linewidth=1,alpha=0.2))
      x2=[i/40+(j+1)/20,i/40+j/20+1/40,i/40+j/20+1/40,i/40+(j+1)/20]
      y2=[i*h/20,i*h/20+h/20,i*h/20+h/20,i*h/20]
      z2=[0,0,1,1]
      poly2=list(zip(x2,y2,z2))
      ax.add_collection3d(art3d.Poly3DCollection([poly2],color='m',linewidth=1,alpha=0.2))
      x3=[i/40+j/20+1/40,i/40+j/20,i/40+j/20,i/40+j/20+1/40]
      y3=[i*h/20+h/20,i*h/20,i*h/20,i*h/20+h/20]
      z3=[0,0,1,1]
      poly3=list(zip(x3,y3,z3))
      ax.add_collection3d(art3d.Poly3DCollection([poly3],color='m',linewidth=1,alpha=0.2))
      x4=[i/40+j/20,i/40+(j+1)/20,i/40+j/20+1/40]
      y4=[i*h/20,i*h/20,i*h/20+h/20]
      z4=[1,1,1]
      poly4=list(zip(x4,y4,z4))
      ax.add_collection3d(art3d.Poly3DCollection([poly4],color='m',linewidth=1,alpha=0.2))
      x5=[i/40+j/20,i/40+(j+1)/20,i/40+j/20+1/40]
      y5=[i*h/20,i*h/20,i*h/20+h/20]
      z5=[0,0,0]
      poly5=list(zip(x5,y5,z5))
      ax.add_collection3d(art3d.Poly3DCollection([poly5],color='m',linewidth=1,alpha=0.2))

for i in range(0,20):
    for j in range(0,20-i-1):
      x1=[i/40+j/20+3/40,i/40+(j+1)/20,i/40+(j+1)/20,i/40+j/20+3/40]
      y1=[i*h/20+h/20,i*h/20,i*h/20,i*h/20+h/20]
      z1=[0,0,1,1]
      poly1=list(zip(x1,y1,z1))
      ax.add_collection3d(art3d.Poly3DCollection([poly1],facecolors='b',linewidth=1,alpha=0.2))
      x2=[i/40+(j+1)/20,i/40+j/20+1/40,i/40+j/20+1/40,i/40+(j+1)/20]
      y2=[i*h/20,i*h/20+h/20,i*h/20+h/20,i*h/20]
      z2=[0,0,1,1]
      poly2=list(zip(x2,y2,z2))
      ax.add_collection3d(art3d.Poly3DCollection([poly2],color='b',linewidth=1,alpha=0.2))
      x3=[i/40+j/20+1/40,i/40+j/20+3/40,i/40+j/20+3/40,i/40+j/20+1/40]
      y3=[i*h/20+h/20,i*h/20+h/20,i*h/20+h/20,i*h/20+h/20]
      z3=[0,0,1,1]
      poly3=list(zip(x3,y3,z3))
      ax.add_collection3d(art3d.Poly3DCollection([poly3],color='b',linewidth=1,alpha=0.2))
      x4=[i/40+j/20+3/40,i/40+(j+1)/20,i/40+j/20+1/40]
      y4=[i*h/20+h/20,i*h/20,i*h/20+h/20]
      z4=[1,1,1]
      poly4=list(zip(x4,y4,z4))
      ax.add_collection3d(art3d.Poly3DCollection([poly4],color='b',linewidth=1,alpha=0.2))
      x5=[i/40+j/20+3/40,i/40+(j+1)/20,i/40+j/20+1/40]
      y5=[i*h/20+h/20,i*h/20,i*h/20+h/20]
      z5=[0,0,0]
      poly5=list(zip(x5,y5,z5))
      ax.add_collection3d(art3d.Poly3DCollection([poly5],color='b',linewidth=1,alpha=0.2))

ax.set_xlim(0,1)
ax.set_ylim(0,1)
ax.set_zlim(0,1)

plt.show()
