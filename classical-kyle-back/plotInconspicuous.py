import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt

# parameters
Sig0 = np.load('data/Sig0.npy')
sig = np.load('data/sig.npy')
p0 = np.load('data/p0.npy')
N = np.load('data/N.npy')

# time
t = np.load('data/t.npy')

# trades
X = np.load('data/X.npy')
Y = np.load('data/Y.npy')
Z = np.load('data/Z.npy')

# prices
P = np.load('data/P.npy')
V = np.load('data/V.npy')

# signal
S = np.load('data/S.npy')

yy = np.linspace(- 3.0 * sig, 3.0 * sig, 256)
dy = norm.pdf(yy, scale = sig)

fig, ax = plt.subplots(nrows = 1, ncols = 2,
                       figsize = (4.5,3), dpi = 256,
                       gridspec_kw = {'width_ratios': (2,1)},
                       sharey = True)

ax[0].plot(t, Z, label = 'noise trades', color = 'gray')
ax[0].plot(1.0, Z[-1], 'o', color = 'gray')
ax[0].plot(t, Y, label = 'aggregate trades', color = 'C0')
ax[0].plot(1.0, S, 'o', color = 'C0')

for i in range(1, int(0.75 * N), 50):
    if i == 1:
        ax[0].arrow(x = t[-i], y = Z[-i] + 0.25 * (Y[-i] - Z[-i]), dx = 0, dy = 0.5 * (Y-Z)[-i],
                    head_length = 0.1, head_width = 0.02, color = 'C1', label = 'informed trades')
    else:
        ax[0].arrow(x = t[-i], y = Z[-i] + 0.25 * (Y[-i] - Z[-i]), dx = 0, dy = 0.5 * (Y-Z)[-i],
                    head_length = 0.1, head_width = 0.02, color = 'C1')
        
ax[0].set_ylabel('running market orders')
ax[0].legend(fontsize = 'xx-small')
ax[0].set_xlabel('time')

ax[1].plot(dy, yy, color = 'grey', label = r'$\mathcal{N}(0,\sigma^2 T)$')
ax[1].set_xlabel('noise density')
ax[1].legend(fontsize = 'xx-small')

fig.tight_layout()
fig.savefig('plots/inconspicuous.jpeg', transparent = False, bbox_inches = 'tight');