import numpy as np
import scipy.linalg as LA
import matplotlib.pyplot as plt
from scipy.stats import norm, chi2

# parameters
N = np.load('data/N.npy')

# prices
P = np.load('data/P.npy')
vt = np.load('data/vt.npy')

# time
t = np.load('data/t.npy')

# plot
fig, ax = plt.subplots(nrows = 2, ncols = 2,
                       figsize = (4.5,4.5), dpi = 256,
                      sharex = True, sharey = True)

K = int(0.75 * N)

ax[0,0].set_ylim(bottom = P.min() * 1.5, top = P.max() * 1.2)
ax[0,0].set_xlim(left = -0.05, right = 1.05)
ax[0,0].plot(t[:K], P[:K,0], label = 'market price', c = 'C0')
ax[0,0].plot(t[-1], vt[0], 'o', label = 'terminal price', c = 'C2')
ax[0,0].set_title('what the insider sees', fontsize = 'small')
ax[0,0].set_ylabel('price of asset 1', fontsize = 'small')
ax[0,0].tick_params(labelleft=False) 
ax[0,0].legend(fontsize = 'x-small', loc = 'lower right')

ax[1,0].plot(t[:K], P[:K,1], c = 'C0')
ax[1,0].plot(t[-1], vt[1], 'o', c = 'C2')
ax[1,0].set_ylabel('price of asset 2', fontsize = 'small')
ax[1,0].set_xlabel('time', fontsize = 'small')
ax[1,0].tick_params(labelbottom=False)
ax[1,0].tick_params(labelleft=False)

ax[0,1].plot(t[:K], P[:K,0], label = 'asset 1', c = 'C0')
ax[0,1].set_title('what the market maker sees', fontsize = 'small')

ax[1,1].plot(t[:K], P[:K,1], label = 'asset 2', c = 'C0')
ax[1,1].set_xlabel('time', fontsize = 'small')
ax[1,1].tick_params(labelbottom=False)

fig.tight_layout()

fig.savefig('plots/prices.jpg', transparent = False, bbox_inches = 'tight')