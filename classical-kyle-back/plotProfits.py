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

# prices
P = np.load('data/P.npy')
V = np.load('data/V.npy')

# insider profits
J = np.zeros(shape = N + 1)
J[1:] = np.cumsum((V - P[1:]) * np.diff(X))

# noise trader profits
L = np.zeros(shape = N + 1)
L[1:] = np.cumsum((V - P[1:]) * np.diff(Z))

# market maker profits
M = np.zeros(shape = N + 1)
M[1:] = np.cumsum((P[1:] - V) * np.diff(Y))

fig, ax = plt.subplots(nrows = 2, ncols = 1,
                       figsize = (4.5,3.5), dpi = 256,
                      sharex = 'col', sharey = True)

ymin = min([J.min(), L.min(), M.min()]) * 1.2
ymax = max([J.max(), L.max(), M.max()]) * 1.2

K = int(1.0 * N)

ax[0].set_xlim(left = -0.05, right = 1.05)
ax[0].set_ylabel('what the informed \n trader sees', fontsize = 'small')
ax[0].plot(t[:K], J[:K], label = 'informed profits', c = 'C1')
ax[0].plot(t[:K], L[:K], label = 'noise profits', c = 'gray')
ax[0].plot(t[:K], M[:K], label = 'market maker profits', c = 'C0')

ax[1].set_xlabel('time')
ax[1].set_ylabel('what the market \n maker sees', fontsize = 'small')
ax[1].plot(t[:K], M[:K], label = 'market maker profits', c = 'C0')

ax[0].legend(fontsize = 'xx-small')
ax[1].legend(fontsize = 'xx-small')

fig.savefig('plots/profits.jpeg', transparent = False, bbox_inches = 'tight');