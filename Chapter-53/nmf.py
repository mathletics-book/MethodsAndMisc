from scipy.stats import norm
import pandas as pd
import numpy as np
from numpy import linalg as LA
from sklearn.decomposition import NMF
import matplotlib.pyplot as plt
from scipy.special import expit


df = pd.read_csv("matrix.csv")

m = np.array(df.iloc[0:288,2:14])

m = expit(m)

model = NMF(n_components=10,max_iter=1000, beta_loss = 'kullback-leibler',solver='mu',init='random', random_state=0)
W = model.fit_transform(m)
H = model.components_

frob = []

for i in range(1,40):
	model = NMF(n_components=i, init='random', random_state=0)
	W = model.fit_transform(m)
	H = model.components_
	frob.append(np.linalg.norm(m - np.matmul(W,H)))

fig, ax = plt.subplots(1, 1)
plt.xlabel("Number of latent patterns k",fontsize=20)
plt.ylabel("Frobenius Norm S-WH",fontsize=20)
ax.plot(range(1,40), frob, 'k-', lw=7)
plt.show()
