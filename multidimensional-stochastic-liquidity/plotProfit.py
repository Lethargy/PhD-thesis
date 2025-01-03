import numpy as np
import matplotlib.pyplot as plt

P = np.load('data/P.npy')
vt = np.load('data/vt.npy')
N = np.load('data/N.npy')
X = np.load('data/X.npy')
Y = np.load('data/Y.npy')
Z = np.load('data/Z.npy')
Sig = np.load('data/Sig.npy')

dX = np.diff(X, axis = 0)
dY = np.diff(Y, axis = 0)
dZ = np.diff(Z, axis = 0)

Ji = np.empty(N+1); Jm = np.empty(N+1); Jn = np.empty(N+1)
Ji[0] = 0.0; Jm[0] = 0.0; Jn[0] = 0.0

for i in range(N):
    Ji[i+1] = Ji[i] + np.dot(vt - P[i,:], dX[i])
    Jn[i+1] = Jn[i] + np.dot(vt - P[i,:], dZ[i])
    Jm[i+1] = Jm[i] - np.dot(vt - P[i,:], dY[i])
    
fig, ax = plt.subplots(figsize = (5,3.5), dpi = 256)

ax.plot(Ji, label = 'insider', c = 'C1')
ax.plot(Jn, label = 'liquidity traders', c = 'gray')
ax.plot(Jm, label = 'market maker', c = 'C0')
ax.set_ylabel('profit (or loss)')
ax.set_xlabel('time')
ax.tick_params(labelbottom=False)
ax.tick_params(labelleft=False)
ax.legend(fontsize = 'small')

fig.savefig('plots/profit.jpg', transparent = False, bbox_inches = 'tight')