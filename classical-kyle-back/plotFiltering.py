import numpy as np
import matplotlib.pyplot as plt

# parameters
N = np.load('data/N.npy')
sig = np.load('data/sig.npy')

# time
t = np.load('data/t.npy')

# prices
P = np.load('data/P.npy')
V = np.load('data/V.npy')

# filtering confidence intervals
ub = P + 1.96 * sig * np.sqrt(t[N] - t)
lb = P - 1.96 * sig * np.sqrt(t[N] - t)

fig, ax = plt.subplots(nrows = 2, ncols = 1,
                       figsize = (4.5,3.5), dpi = 256,
                      sharex = 'col', sharey = True)

K = int(0.75 * N)

ax[0].set_xlim(left = -0.05, right = 1.05)
ax[0].set_ylabel('what the informed \n trader knows', fontsize = 'small')
ax[0].scatter(t[K],P[K], marker = 'o', color = 'C0')
ax[0].plot(t[:K], P[:K], label = r'market price ($P_t$)', color = 'C0')
ax[0].scatter(t[N], V, marker = 'o', label = r'true price ($\tilde v$)', color = 'C2')
ax[0].hlines(V, 0, t[N], ls = '--', color = 'C2')
ax[0].legend(fontsize = 'xx-small', loc = 'lower right')

ax[1].plot(t[:K], P[:K], label = r'market price ($P_t$)', c = 'C0')
ax[1].fill_between(t[:K], y1 = lb[:K], y2 = ub[:K], color = 'lightblue', label = '95% CI')
ax[1].scatter(t[K],P[K], marker = 'o', color = 'C0')
ax[1].set_ylabel('the market maker\'s \n best guess', fontsize = 'small')
ax[1].set_xlabel('time')
ax[1].legend(fontsize = 'xx-small', loc = 'lower right')

fig.savefig('plots/filtering.jpeg', transparent = False, bbox_inches = 'tight');