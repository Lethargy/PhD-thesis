import numpy as np
from scipy.stats import norm

np.random.seed(1)

N = 2048
T = 1.0
dt = T / N
t = np.linspace(0.0, T, N + 1)
sig = 1.0 / np.sqrt(2.0)

SIG = 0.5 - 0.5 * t

S = np.empty(N + 1)
S[0] = norm.rvs(scale = sig) # S_0 ~ N(0, 1/2)
S[1:] = S[0] + sig * np.sqrt(dt) * norm.rvs(size = N).cumsum()

dZ = np.sqrt(dt) * norm.rvs(size = N)
Z = np.empty(N + 1)
Z[0] = 0.0
Z[1:] = dZ.cumsum()

X = np.empty(N + 1); X[0] = 0.0

for n in range(N):
    X[n+1] = X[n] + (S[n] - X[n] - Z[n]) / SIG[n] * dt
    
Y = X + Z

p0 = 5.0
lam = 2.0
P = p0 + lam * Y
V = p0 + lam * S

# parameters
np.save('data/p0', p0)
np.save('data/lam', lam)
np.save('data/N', N)

# time
np.save('data/t', t)

# trades
np.save('data/X', X)
np.save('data/Y', Y)
np.save('data/Z', Z)

# prices
np.save('data/P', P)
np.save('data/V', V)

# signal
np.save('data/S', S)

# filtering
np.save('data/SIG', SIG)
