import numpy as np
import matplotlib.pyplot as plt

t,X,Y,Z = np.load('data/tXYZ.npy')

# plot
fig, ax = plt.subplots(nrows = 2, ncols = 1,
                       figsize = (4.5,3.5), dpi = 256,
                      sharex = 'col')

K = int(0.75 * len(X))

ax[0].set_ylim(bottom = min([X.min(), Y.min(), Z.min()]) - 0.1,
               top = max([X.max(), Y.max(), Z.max()]) + 0.1)
ax[0].set_xlim(left = -0.05, right = 1.05)
ax[0].plot(t[:K], X[:K], label = 'informed trades', c = 'C1')
ax[0].plot(t[:K], Z[:K], label = 'noise trades', c = 'gray')
ax[0].plot(t[:K], Y[:K], label = 'net trades', c = 'C0')
ax[0].text(0.0,2.0, 'what the informed trader sees', color = 'gray')
ax[0].set_ylabel('trades')

ax[1].set_ylim(bottom = min([X.min(), Y.min(), Z.min()]) - 0.1,
               top = max([X.max(), Y.max(), Z.max()]) + 0.1)
ax[1].set_xlim(left = -0.05, right = 1.05)
ax[1].plot(t[:K], Y[:K], label = 'net trades', c = 'C0')
ax[1].text(0.0,2.0, 'what the market maker sees', color = 'gray')
ax[1].set_xlabel('time')
ax[1].set_ylabel('trades')

ax[0].legend(fontsize = 'xx-small', loc = 'lower right')
ax[1].legend(fontsize = 'xx-small', loc = 'lower right')

fig.savefig('plots/trades.jpeg', transparent = False, bbox_inches = 'tight')