import numpy as np
import scipy.linalg as LA
from scipy.stats import norm, chi2

T = 1.0
N = 2**13
t = np.linspace(0.0,T,N+1)
dt = T / N

# defining sigma

# first, define W

np.random.seed(1)

dW1 = np.sqrt(dt) * norm.rvs(size = N)
W1 = np.empty(shape = N+1)
W1[0] = 0.0; W1[1:] = dW1.cumsum()

dW2 = np.sqrt(dt) * norm.rvs(size = N)
W2 = np.empty(shape = N+1)
W2[0] = 0.0; W2[1:] = dW2.cumsum()

# then, construct eigenvalue processes
m1 = 0.5
nu1 = 0.4
sig1 = np.exp((m1 - 0.5 * nu1**2) * t + nu1 * W1)

m2 = 0.7
nu2 = 0.2
sig2 = np.exp((m2 - 0.5 * nu2**2) * t + nu2 * W2)

# then, construct eigenvectors V
th = 0.5
V = np.array([[np.cos(th), -np.sin(th)],
              [np.sin(th), np.cos(th)]])

# finally, construct sigma = Vt @ D @ V
sig = np.empty(shape = (N+1,2,2))
for i in range(N+1):
    sig[i] = V @ np.diag([sig1[i], sig2[i]]) @ V.T
    
# defining Z

# first, define B

np.random.seed(2)
dB = np.sqrt(dt) * norm.rvs(size = (N,2))
B = np.empty(shape = (N+1,2))
B[0] = 0.0; B[1:] = dB.cumsum(axis = 0)

# then, define Z
Z = np.empty(shape = (N+1,2))
Z[0] = 0

for i in range(N):
    Z[i+1] = Z[i] + sig[i] @ dB[i]
    
# define v tilde

p0 = np.array([0.5,2.25])
Sig0 = V @ np.diag([3.0, 4.0]) @ V.T

np.random.seed(3)
vt = p0 + LA.sqrtm(Sig0) @ norm.rvs(size = 2)

# define minimizer

s1 = V[:,0].T @ Sig0 @ V[:,0]
s2 = V[:,1].T @ Sig0 @ V[:,1]
lam1 = np.sqrt(2 * m1 * s1 / (np.exp(2*m1*T) - 1)) * np.exp(m1 * t) / sig1
lam2 = np.sqrt(2 * m2 * s2 / (np.exp(2*m2*T) - 1)) * np.exp(m2 * t) / sig2
M1 = 1.0 / lam1
M2 = 1.0 / lam2

M = np.empty(shape = (N+1,2,2))
Lam = np.empty(shape = (N+1,2,2))
dSig = np.empty(shape = (N+1,2,2))

for i in range(N+1):
    M[i] = V @ np.diag([M1[i], M2[i]]) @ V.T
    Lam[i] = V @ np.diag([lam1[i], lam2[i]]) @ V.T
    dSig[i] = V @ np.diag([(lam1[i]*sig1[i])**2, (lam2[i]*sig2[i])**2]) @ V.T * dt
    
# filtering error

Sig = np.empty(shape = (N+1,2,2))
Sig[0] = Sig0

for i in range(N):
    Sig[i+1] = Sig[i] - dSig[i]

# pricing rule

P = np.empty(shape = (N+1,2)); P[0] = p0
X = np.empty(shape = (N+1,2)); X[0] = 0.0
Y = np.empty(shape = (N+1,2)); Y[0] = 0.0

for i in range(N):
    dX = sig[i] @ sig[i] @ Lam[i] @ LA.solve(Sig[i], vt - P[i]) * dt
    dY = dX + sig[i] @ dB[i]
    dP = Lam[i] @ dY
    
    X[i+1] = X[i] + dX
    Y[i+1] = Y[i] + dY
    P[i+1] = P[i] + dP
    
# parameters
np.save('data/p0', p0)
np.save('data/Lam', Lam)
np.save('data/N', N)

# volatility
np.save('data/sig', sig)

# trades
np.save('data/X', X)
np.save('data/Y', Y)
np.save('data/Z', Z)

# prices
np.save('data/P', P)
np.save('data/vt', vt)

# variance
np.save('data/Sig', Sig)

# time
np.save('data/t', t)