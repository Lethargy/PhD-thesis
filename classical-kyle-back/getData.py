import numpy as np
from scipy.stats import norm, lognorm

np.random.seed(0)

p0 = 5.0
Sig0 = 1.0
sqrtSig0 = np.sqrt(Sig0)
sig = 1.5
lam = sqrtSig0 / sig

T = 1.0
N = 1024
dt = T / N
t = np.linspace(0.0, T, N+1)

dZ = norm.rvs(size = N, scale = sig * np.sqrt(dt))
Z = np.zeros(N + 1)
Z[1:] = dZ.cumsum()

V = norm.rvs(loc = p0, scale = sqrtSig0)
S = sig / np.sqrt(Sig0) * (V - p0)

X = np.empty(N + 1); X[0] = 0.0
for n in range(N):
    X[n+1] = X[n] + (S - X[n] - Z[n]) / (T - t[n]) * dt
    
Y = X + Z

P = p0 + lam * Y

yy = np.linspace(-1.0, 1.0, 256)
dy = norm.pdf(yy, scale = sig)
pp = np.linspace(p0 - 3.0 * sqrtSig0, p0 + 3.0 * sqrtSig0, 256)
dp = lognorm.pdf(pp, loc = p0, s = sqrtSig0)

J = np.cumsum((V - P[1:]) * np.diff(X))
Sig = Sig0 * (T - t)
ub = P + 1.96 * np.sqrt(Sig)
lb = P - 1.96 * np.sqrt(Sig)

yy = np.linspace(- 3.25 * sig, 3.25 * sig, 256)
dy = norm.pdf(yy, scale = sig)
pp = np.linspace(p0 - 3.0 * sqrtSig0, p0 + 3.0 * sqrtSig0, 256)
dp = norm.pdf(pp, loc = p0, scale = sqrtSig0)

# parameters
np.save('data/Sig0.npy', Sig0)
np.save('data/sig.npy', sig)
np.save('data/p0.npy', p0)
np.save('data/N.npy', N)
np.save('data/lam.npy', lam)

# time
np.save('data/t.npy', t)

# trades
np.save('data/X.npy', X)
np.save('data/Y.npy', Y)
np.save('data/Z.npy', Z)

# prices
np.save('data/P.npy', P)
np.save('data/V.npy', V)

# signal
np.save('data/S.npy', S)