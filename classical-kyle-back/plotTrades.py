import numpy as np
import matplotlib.pyplot as plt

# parameters
N = np.load('data/N.npy')

# time
t = np.load('data/t.npy')

# trades
X = np.load('data/X.npy')
Y = np.load('data/Y.npy')
Z = np.load('data/Z.npy')

# plot
fig, ax = plt.subplots(nrows = 2, ncols = 1,
                       figsize = (4.5,3.5), dpi = 256,
                      sharex = 'col', sharey = True)

K = int(0.75 * N)
ax[0].plot(t[:K], X[:K], label = r'informed demand $(X_t)$', c = 'C1')
ax[0].plot(t[:K], Z[:K], label = r'noise demand $(Z_t)$', c = 'grey')
ax[0].plot(t[:K], Y[:K], label = r'total demand $(Y_t = X_t + Z_t)$', c = 'C0')
ax[0].set_xlim(left = -0.05, right = 1.05)
ax[0].set_ylabel('what the informed \n trader sees', fontsize = 'small')
ax[0].legend(fontsize = 'xx-small', loc = 'lower right')

ax[1].plot(t[:K], Y[:K], label = r'total demand $(Y_t)$', c = 'C0')
ax[1].set_xlim(left = -0.05, right = 1.05)
ax[1].set_ylabel('what the market \n maker sees',  fontsize = 'small')
ax[1].set_xlabel('time')
ax[1].legend(fontsize = 'xx-small', loc = 'lower right')

fig.savefig('plots/trades.jpeg', transparent = False, bbox_inches = 'tight');