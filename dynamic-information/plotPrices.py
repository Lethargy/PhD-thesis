import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt

t = np.load('data/t.npy')
S = np.load('data/S.npy')
P = np.load('data/P.npy')
X = np.load('data/X.npy')
Z = np.load('data/Z.npy')
V = np.load('data/V.npy')
p0 = np.load('data/p0.npy')
lam = np.load('data/lam.npy')
SIG = np.load('data/SIG.npy')
N = np.load('data/N.npy')

fig, ax = plt.subplots(nrows = 2, ncols = 1,
                       figsize = (4.5,3.5), dpi = 256,
                      sharex = 'col', sharey = True)

K = int(0.75 * len(t))

ax[0].set_xlim(left = -0.05, right = 1.05)
ax[0].set_ylabel('what the informed \n trader sees', fontsize = 'small')
ax[0].plot(t[:K], P[:K], label = 'market price', c = 'C0')
ax[0].plot(t[:K], V[:K], label = 'true price', c = 'C2')
ax[0].legend(fontsize = 'xx-small', loc = 'lower right')

ax[1].plot(t[:K], P[:K], label = 'market price', c = 'C0')
ax[1].set_ylabel('what the market \n maker sees', fontsize = 'small')
ax[1].set_xlabel('time')
ax[1].legend(fontsize = 'xx-small', loc = 'lower right')

fig.savefig('plots/prices.jpeg', transparent = False, bbox_inches = 'tight')
