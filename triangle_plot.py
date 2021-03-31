import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

data=pd.read_csv("C:/python/sample11.csv")
Ag=data["'[107Ag]+'"]+data["'[109Ag]+'"]
Pt=data["'[194Pt]+'"]+data["'[195Pt]+'"]+data["'[196Pt]+'"]+data["'[198Pt]+'"]
Au=data["'[197Au]+'"]
SUM=Ag+Pt+Au
pAg=Ag/SUM*100
pPt=Pt/SUM*100
pAu=Au/SUM*100
data_concat=pd.concat([pAg,pPt,pAu],axis=1)
data_concat.columns=['Ag','Pt','Au']

h = np.sqrt(3.0)*0.5

plotx=(100-data_concat['Pt'])/100-data_concat['Ag']/200
ploty=h*data_concat['Ag']/100
data_plot=pd.concat([plotx,ploty],axis=1)
data_plot.columns=['x','y']

fig = plt.figure()
ax1 = fig.add_subplot(111)
ax1.set_aspect('equal', 'datalim')
plt.tick_params(labelbottom=False, labelleft=False, labelright=False, labeltop=False)
plt.tick_params(bottom=False, left=False, right=False, top=False)
plt.gca().spines['bottom'].set_visible(False)
plt.gca().spines['left'].set_visible(False)
plt.gca().spines['right'].set_visible(False)
plt.gca().spines['top'].set_visible(False)

for i in range(1,10):
    ax1.plot([i/20.0, 1.0-i/20.0],[h*i/10.0, h*i/10.0], color='gray', lw=0.5)
    ax1.plot([i/20.0, i/10.0],[h*i/10.0, 0.0], color='gray', lw=0.5)
    ax1.plot([0.5+i/20.0, i/10.0],[h*(1.0-i/10.0), 0.0], color='gray', lw=0.5)

ax1.plot([0.0, 1.0],[0.0, 0.0], 'k-', lw=2)
ax1.plot([0.0, 0.5],[0.0, h], 'k-', lw=2)
ax1.plot([1.0, 0.5],[0.0, h], 'k-', lw=2)

ax1.text(0.48, h+0.0283, 'x', fontsize=16)
ax1.text(-0.05, -0.02, 'y', fontsize=16)
ax1.text(1.02, -0.02, 'z', fontsize=16)

for i in range(1,10):
    ax1.text(0.5+(10-i)/20.0+0.01, h*(1.0-(10-i)/10.0), '%d0' % i, fontsize=10)
    ax1.text((10-i)/20.0-0.06, h*(10-i)/10.0, '%d0' % i, fontsize=10)
    ax1.text(i/10.0-0.03, -0.048, '%d0' % i, fontsize=10)

ax1.text(0.84,h/2,'% x',fontsize=12)
ax1.text(0.08,h/2,'% y',fontsize=12)
ax1.text(0.5,-0.11,'% z',fontsize=12)

ax1.scatter(data_plot["x"],data_plot["y"])

plt.show()