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

yy = np.linspace(-2.5, 2.5, 501); dy = norm.pdf(x = yy)
pp = np.linspace(p0 - 2.5 * lam, p0 + 2.5 * lam, 501)
dp = norm.pdf(x = pp, loc = p0, scale = np.sqrt(lam));

ub = P + 1.96 * lam * np.sqrt(SIG)
lb = P - 1.96 * lam * np.sqrt(SIG)


fig, ax = plt.subplots(nrows = 2, ncols = 1,
                       figsize = (4.5,3.5), dpi = 256,
                      sharex = 'col')

ymin = lb.min() - 0.25
ymax = ub.max() + 0.25

K = int(0.75 * len(t))

ax[0].set_ylim(bottom = ymin, top = ymax)
ax[0].set_xlim(left = -0.05, right = 1.05)
ax[0].set_ylabel('price')
ax[0].set_ylim(bottom = ymin, top = ymax)
ax[0].text(0,9.5,'what the informed trader knows', color = 'gray')
ax[0].plot(t[:K], P[:K], label = 'market price', c = 'C0')
ax[0].plot(t[:K], V[:K], label = 'true price', c = 'C2')
ax[0].legend(fontsize = 'xx-small', loc = 'lower right')

ax[1].set_ylim(bottom = ymin, top = ymax)
ax[1].plot(t[:K], P[:K], label = 'market price', c = 'C0')
ax[1].fill_between(t[:K], y1 = lb[:K], y2 = ub[:K], color = 'lightblue', label = '95% CI')
ax[1].text(0,9.5,'the market maker\'s best guess', color = 'gray')
ax[1].set_ylabel('price')
ax[1].set_xlabel('time')
ax[1].legend(fontsize = 'xx-small', loc = 'lower right')

fig.savefig('plots/filtering.jpeg', transparent = False, bbox_inches = 'tight')