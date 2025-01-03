import numpy as np
import matplotlib.pyplot as plt

# parameters
N = np.load('data/N.npy')

# trades
X = np.load('data/X.npy')
Y = np.load('data/Y.npy')
Z = np.load('data/Z.npy')

# price
P = np.load('data/P.npy')
vt = np.load('data/vt.npy')

# time
t = np.load('data/t.npy')

# plot
fig, ax = plt.subplots(nrows = 2, ncols = 2,
                       figsize = (5,5), dpi = 256,
                      sharex = True, sharey = True)

K = int(0.75 * N)

ax[0,0].set_xlim(left = -0.05, right = 1.05)
ax[0,0].plot(t[:K], X[:K,0], label = 'insider trades', c = 'C1')
ax[0,0].plot(t[:K], Z[:K,0], c = 'gray', label = 'noise trades')
ax[0,0].plot(t[:K], Y[:K,0], label = 'total trades', c = 'C0')
ax[0,0].set_title('what the insider sees', fontsize = 'small')
ax[0,0].set_ylabel('demand for asset 1', fontsize = 'small')
ax[0,0].tick_params(labelleft=False)
ax[0,0].legend(fontsize = 'x-small')

ax[1,0].plot(t[:K], X[:K,1], c = 'C1')
ax[1,0].plot(t[:K], Y[:K,1], c = 'C0')
ax[1,0].plot(t[:K], Z[:K,1], c = 'gray')
ax[1,0].set_ylabel('demand for asset 2', fontsize = 'small')
ax[1,0].tick_params(labelleft=False)
ax[1,0].tick_params(labelbottom=False)
ax[1,0].set_xlabel('time', fontsize = 'small')

ax[0,1].plot(t[:K], Y[:K,0], c = 'C0')
ax[0,1].tick_params(labelleft=False) 
ax[0,1].tick_params(labelbottom=False)
ax[0,1].set_title('what the market maker sees', fontsize = 'small')

ax[1,1].plot(t[:K], Y[:K,1], c = 'C0')
ax[1,1].set_xlabel('time', fontsize = 'small')
ax[1,1].tick_params(labelbottom=False) 

fig.tight_layout()

fig.savefig('plots/trades.jpg', transparent = False, bbox_inches = 'tight')