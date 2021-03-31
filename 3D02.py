import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig=plt.figure(figsize=(8,8))
ax1=fig.add_subplot(111,projection='3d')
ax1.set_xticks([])
ax1.set_yticks([])
ax1.set_zticks([])
ax1.view_init(elev=90,azim=90)


h = np.sqrt(3.0)*0.5

for i in range(1,20):
    ax1.plot([i/2/20.0, 1.0-i/2/20.0],[h*i/2/10.0, h*i/2/10.0],[0,0],color='gray', lw=0.5)
    ax1.plot([i/2/20.0, i/2/10.0],[h*i/2/10.0, 0.0],[0,0], color='gray', lw=0.5)
    ax1.plot([0.5+i/2/20.0, i/2/10.0],[h*(1.0-i/2/10.0), 0.0],[0,0], color='gray', lw=0.5)

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

ax1.plot([0.0, 0.0],[0.0, 0.0],[0,1], 'k-', lw=2)
ax1.plot([1, 1],[0,0],[0,1], 'k-', lw=2)
ax1.plot([0.5, 0.5],[h, h],[0,1], 'k-', lw=2)

ax1.set_xlim(0,1)
ax1.set_ylim(0,1)
ax1.set_zlim(0,1)


plt.show()
