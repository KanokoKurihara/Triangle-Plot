import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import pandas as pd

data=pd.read_csv("C:/python/sample11.csv")#TOF測定データ
Ag=data["'[107Ag]+'"]+data["'[109Ag]+'"]
Pt=data["'[194Pt]+'"]+data["'[195Pt]+'"]+data["'[196Pt]+'"]+data["'[198Pt]+'"]
Au=data["'[197Au]+'"]
SUM=Ag+Pt+Au
pAg=Ag/SUM*100
pPt=Pt/SUM*100
pAu=Au/SUM*100
data_concat=pd.concat([pAg,pPt,pAu,SUM],axis=1)
data_concat.columns=['Ag','Pt','Au','SUM']

h = np.sqrt(3.0)*0.5

zmax=data_concat['SUM'].max()
plotx=(100-data_concat['Pt'])/100-data_concat['Ag']/200
ploty=h*data_concat['Ag']/100
plotz=data_concat['SUM']/zmax #←書き換える　元素別
data_plot=pd.concat([plotx,ploty,plotz],axis=1)
data_plot.columns=['x','y','z']

fig=plt.figure(figsize=(6,6))
ax1=fig.add_subplot(111,projection='3d')
ax1.set_xticks([])
ax1.set_yticks([])
ax1.set_zticks([])
plt.axis('off')
ax1.view_init(elev=4,azim=138)

for i in range(1,10):
    ax1.plot([i/20.0, 1.0-i/20.0],[h*i/10.0, h*i/10.0],[0,0],color='gray', lw=0.5)
    ax1.plot([i/20.0, i/10.0],[h*i/10.0, 0.0],[0,0], color='gray', lw=0.5)
    ax1.plot([0.5+i/20.0, i/10.0],[h*(1.0-i/10.0), 0.0],[0,0], color='gray', lw=0.5)

ax1.plot([0.0, 1.0],[0.0, 0.0],[0,0], 'k-', lw=2)
ax1.plot([0.0, 0.5],[0.0, h],[0,0], 'k-', lw=2)
ax1.plot([1.0, 0.5],[0.0, h],[0,0], 'k-', lw=2)

ax1.plot([0.0, 0.0],[0.0, 0.0],[0,1], 'k-', lw=2)
ax1.plot([1, 1],[0,0],[0,1], 'k-', lw=2)
ax1.plot([0.5, 0.5],[h, h],[0,1], 'k-', lw=2)

ax1.text(0.48, h+0.0283,0, 'x', fontsize=16)
ax1.text(-0.05, -0.02,0, 'y', fontsize=16)
ax1.text(1.02, -0.02,0, 'z', fontsize=16)

for i in range(1,10):
    ax1.plot([i/20.0, 1.0-i/20.0],[h*i/10.0, h*i/10.0],[1,1],color='gray', lw=0.5)
    ax1.plot([i/20.0, i/10.0],[h*i/10.0, 0.0],[1,1], color='gray', lw=0.5)
    ax1.plot([0.5+i/20.0, i/10.0],[h*(1.0-i/10.0), 0.0],[1,1], color='gray', lw=0.5)

ax1.plot([0.0, 1.0],[0.0, 0.0],[1,1], 'k-', lw=2)
ax1.plot([0.0, 0.5],[0.0, h],[1,1], 'k-', lw=2)
ax1.plot([1.0, 0.5],[0.0, h],[1,1], 'k-', lw=2)

for i in range(1,10):
    ax1.plot([i/20.0, 1.0-i/20.0],[h*i/10.0, h*i/10.0],[0.5,0.5],color='gray', lw=0.5)
    ax1.plot([i/20.0, i/10.0],[h*i/10.0, 0.0],[0.5,0.5], color='gray', lw=0.5)
    ax1.plot([0.5+i/20.0, i/10.0],[h*(1.0-i/10.0), 0.0],[0.5,0.5], color='gray', lw=0.5)

ax1.plot([0.0, 1.0],[0.0, 0.0],[0.5,0.5], 'k-', lw=2)
ax1.plot([0.0, 0.5],[0.0, h],[0.5,0.5], 'k-', lw=2)
ax1.plot([1.0, 0.5],[0.0, h],[0.5,0.5], 'k-', lw=2)


ax1.plot([0.0, 0.0],[0.0, 0.0],[0,1], 'k-', lw=2)
ax1.plot([1, 1],[0,0],[0,1], 'k-', lw=2)
ax1.plot([0.5, 0.5],[h, h],[0,1], 'k-', lw=2)


ax1.set_xlim(0,1)
ax1.set_ylim(0,1)
ax1.set_zlim(0,1)

ax1.scatter(data_plot["x"],data_plot["y"],data_plot["z"])


plt.show()
