import numpy as np
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

fig, ax = plt.subplots(nrows = 1, ncols = 2,
                       figsize = (4.5,3), dpi = 256,
                       gridspec_kw = {'width_ratios': (2,1)},
                       sharey = True)
ax[0].plot(t, Z, label = 'noise trades', color = 'gray')
ax[0].plot(1.0, Z[-1], 'o', color = 'gray')


for i in range(1, int(0.75 * N), 50):
    if i == 1:
        ax[0].arrow(x = t[-i], y = Z[-i] + 0.25 * (Y[-i] - Z[-i]), dx = 0, dy = 0.5 * (Y-Z)[-i],
                    head_length = 0.1, head_width = 0.02, color = 'C1', label = 'informed trades')
    else:
        ax[0].arrow(x = t[-i], y = Z[-i] + 0.25 * (Y[-i] - Z[-i]), dx = 0, dy = 0.5 * (Y-Z)[-i],
                    head_length = 0.1, head_width = 0.02, color = 'C1')

ax[0].plot(t, Y, label = 'aggregate trades', color = 'C0')
ax[0].plot(1.0, S, 'o', color = 'C0')
        
ax[0].set_ylabel('running market orders')
ax[0].legend(fontsize = 'xx-small')
ax[0].set_xlabel('time')

rightbound = V - p0 - np.sqrt(Sig0) * Z[-1] / sig
foo = np.linspace(0.0 - 0.5, rightbound + 0.5, 256)
RSC = (sig / np.sqrt(Sig0)) * (V - p0 - foo)

ax[1].plot(foo,RSC, c = 'C1', ls = '--')
ax[1].set_xlabel('residual supply' + '\n' + 'curve')
ax[1].fill_between(x = np.linspace(0.0, rightbound, 256),
                   y1 = (sig / np.sqrt(Sig0)) * (V - p0 - np.linspace(0.0, rightbound, 256)),
                  y2 = Z[-1], color = 'C1', alpha = 0.5, label = 'profit')
ax[1].legend()
fig.tight_layout()
fig.savefig('plots/residualsupply.jpeg', transparent = False, bbox_inches = 'tight');