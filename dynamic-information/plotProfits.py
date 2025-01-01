import numpy as np
import matplotlib.pyplot as plt

N = np.load('data/N.npy')
P = np.load('data/P.npy')
X = np.load('data/X.npy')
Y = np.load('data/Y.npy')
Z = np.load('data/Z.npy')
V = np.load('data/V.npy')
t = np.load('data/t.npy')

J = np.zeros(shape = N + 1)
J[1:] = np.cumsum((V[-1] - P[1:]) * np.diff(X))
L = np.zeros(shape = N + 1)
L[1:] = np.cumsum((V[-1] - P[1:]) * np.diff(Z))
M = np.zeros(shape = N + 1)
M[1:] = np.cumsum((P[1:] - V[-1]) * np.diff(Y))

fig, ax = plt.subplots(nrows = 2, ncols = 1,
                       figsize = (4.5,3.5), dpi = 256,
                      sharex = 'col', sharey = True)

K = int(0.75 * N)

ax[0].set_xlim(left = -0.05, right = 1.05)
ax[0].set_ylabel('what the informed \n trader sees', fontsize = 'small')
ax[0].plot(t[:K], J[:K], label = 'informed profits', c = 'C1')
ax[0].plot(t[:K], L[:K], label = 'noise profits', c = 'gray')
ax[0].plot(t[:K], M[:K], label = 'market maker profits', c = 'C0')

ax[1].set_xlabel('time')
ax[1].set_ylabel('what the market \n maker sees', fontsize = 'small')
ax[1].plot(t[:K], M[:K], label = 'market maker profits', c = 'C0')

ax[0].legend(fontsize = 'xx-small', loc = 'center right')
ax[1].legend(fontsize = 'xx-small', loc = 'center right')

fig.savefig('plots/profits.jpeg', transparent = False, bbox_inches = 'tight')
