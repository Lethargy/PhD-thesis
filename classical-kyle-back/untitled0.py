import numpy as np
import matplotlib.pyplot as plt

# parameters
N = np.load('data/N.npy')

# time
t = np.load('data/t.npy')

# prices
P = np.load('data/P.npy')
V = np.load('data/V.npy')

# plot
fig, ax = plt.subplots(nrows = 2, ncols = 1,
                       figsize = (4.5,3.5), dpi = 256,
                      sharex = 'col', sharey = True)

K = int(0.75 * N)
ax[0].plot(t[:K], P[:K], label = r'market price $(P_t)$', c = 'C0')
ax[0].plot(t[-1], V, 'o', color = 'C2', label = r'fundamental price $(\tilde v)$')

ax[0].set_xlim(left = -0.05, right = 1.05)
ax[0].set_ylabel('what the informed \n trader sees', fontsize = 'small')

ax[1].plot(t[:K], P[:K], label = r'market price $(P_t)$', c = 'C0')
ax[1].set_ylabel('what the market \n maker sees', fontsize = 'small')
ax[1].set_xlabel('time')

ax[0].legend(fontsize = 'xx-small', loc = 'lower right')
ax[1].legend(fontsize = 'xx-small', loc = 'lower right')

fig.savefig('plots/prices.jpeg', transparent = False, bbox_inches = 'tight');