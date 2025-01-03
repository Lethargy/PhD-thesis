import numpy as np
import scipy.linalg as LA
import matplotlib.pyplot as plt
from scipy.stats import chi2

P = np.load('data/P.npy')
vt = np.load('data/vt.npy')
N = np.load('data/N.npy')
p0 = np.load('data/p0.npy')
Sig = np.load('data/Sig.npy')

z = np.sqrt(chi2.ppf(0.95, df = 2))

def conf_ellipse(mu,Cov):
    theta = np.linspace(0.0, 2.0 * np.pi, 101)
    r = np.empty(101)
    for i in range(101):
        U = np.array([np.cos(theta[i]), np.sin(theta[i])])
        r[i] = z / np.sqrt(U @ LA.solve(Cov, U.T))

    x1 = r * np.cos(theta) + mu[0]
    x2 = r * np.sin(theta) + mu[1]
    
    return x1, x2


fig, ax = plt.subplots(ncols = 2, nrows = 3, figsize = (6, 9), dpi = 256,
                       sharey = True, sharex = True)

ax[0,0].set_xlim(-5, 8)
ax[0,0].set_ylim(-5, 8)

ax[0,0].scatter(P[0,0],P[0,1], marker = 'o',  color = 'C0', label = r'$P_0$')
ax[0,0].scatter(vt[0],vt[1], marker = 'o', color = 'C2', label = r'$\tilde{\bf{v}}$')
ax[0,0].set_ylabel('price of asset 2')
ax[0,0].text(x = -4, y = -4, s = r'$t = 0$')
ax[0,0].tick_params(labelbottom=False) 
ax[0,0].tick_params(labelleft=False)
ax[0,0].set_title('what the insider knows', fontsize = 'medium')
ax[0,0].legend()

x1, x2 = conf_ellipse(p0,Sig[0])
ax[0,1].scatter(P[0,0],P[0,1], marker = 'o',  color = 'C0', label = r'$P_0$')
ax[0,1].fill(x1,x2,'C0', alpha = 0.5, label = '95% confidence ellipse')
ax[0,1].tick_params(labelbottom=False)
#ax[1].text(x = -4, y = -4, s = 'the market maker\'s best guess', color = 'gray')
ax[0,1].set_title('the market maker\'s best guess', fontsize = 'medium')
ax[0,1].legend(fontsize = 'small')

M = int(0.75 * N)

ax[1,0].set_xlim(-5, 8)
ax[1,0].set_ylim(-5, 8)
ax[1,0].tick_params(labelleft=False)
ax[1,0].text(x = -4, y = -4, s = r'$t = 0.75 T$')
ax[1,0].scatter(vt[0],vt[1], marker = 'o',  color = 'C2')
ax[1,0].scatter(P[M,0],P[M,1], marker = 'o',  color = 'C0', label = r'$P_{0.75T}$')
ax[1,0].set_ylabel('price of asset 2')
ax[1,0].legend()

x1, x2 = conf_ellipse(P[M],Sig[M])
ax[1,1].fill(x1,x2,'C0', alpha = 0.5)
ax[1,1].scatter(P[M,0],P[M,1], marker = 'o',  color = 'C0')

splits = 64
bins = np.arange(0,M+1,M // splits)
C = np.tan(1)

for i in range(splits):
    j0 = bins[i]
    j1 = bins[i+1]
    ax[1,0].plot(P[j0:j1,0],P[j0:j1,1], alpha = np.tan(i / splits) / C, c = 'C0')
    ax[1,1].plot(P[j0:j1,0],P[j0:j1,1], alpha = np.tan(i / splits) / C, c = 'C0')
    
M = int(0.95 * N)

ax[2,0].scatter(vt[0],vt[1], marker = 'o',  color = 'C2', zorder = 3)
ax[2,0].tick_params(labelbottom=False)
ax[2,0].tick_params(labelleft=False)
ax[2,0].scatter(P[M,0],P[M,1], marker = 'o',  color = 'C0', label = r'$P_{0.95T}$')
ax[2,0].text(x = -4, y = -4, s = r'$t = 0.95 T$')
ax[2,0].set_xlabel('price of asset 1')
ax[2,0].set_ylabel('price of asset 2')
ax[2,0].legend()

x1, x2 = conf_ellipse(P[M],Sig[M])
ax[2,1].fill(x1,x2,'C0', alpha = 0.5)
ax[2,1].scatter(P[M,0],P[M,1], marker = 'o',  color = 'C0')
ax[2,1].tick_params(labelbottom=False)
ax[2,1].set_xlabel('price of asset 1')

splits = 64
bins = np.arange(0,M+1,M // splits)
C = np.tan(1)

for i in range(splits):
    j0 = bins[i]
    j1 = bins[i+1]
    ax[2,0].plot(P[j0:j1,0],P[j0:j1,1], alpha = np.tan(i / splits) / C, c = 'C0')
    ax[2,1].plot(P[j0:j1,0],P[j0:j1,1], alpha = np.tan(i / splits) / C, c = 'C0')
    
fig.tight_layout()

fig.savefig('plots/filtering.jpg', transparent = False, bbox_inches = 'tight')