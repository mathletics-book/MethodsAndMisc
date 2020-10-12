import numpy as np
from scipy.stats import beta
import matplotlib.pyplot as plt
from math import factorial
import scipy.integrate as integrate
import sys

# prior distribution for the 50-yard FG success rate of kickers
# Beta distribution a = 5, b = 2.5

a,b = 5,2.0
rv = beta(a, b)

prior = lambda x: rv.pdf(x)

x = np.linspace(beta.ppf(0, a, b),beta.ppf(1, a, b), 100)
fig, ax = plt.subplots(1, 1)
plt.xlabel("50-yard FG success rate")
plt.ylabel("Density")
plt.title('Prior distribution')
ax.plot(x, prior(x), 'k-', lw=2)
plt.show()

# update belief based on observations

# input: number of field goal attempts (sys.argv[1])
# input: number of successes (sys.argv[2])

# likelihood: Bernoulli -- p^(sys.argv[2])*(1-p)^(sys.argv[1]-sys.argv[2]))

x1 = int(sys.argv[1])
x2 = int(sys.argv[2])
c = factorial(x1)/(factorial(x2)*factorial(x1-x2))

l = lambda x: c*(x**x2)*((1-x)**(x1-x2))

# total probability 

f = lambda x: prior(x)*l(x)

tp = integrate.quad(f, 0, 1)[0]

# posterior 

post = lambda x: prior(x)*l(x)/tp

fig, ax = plt.subplots(1, 1)
plt.xlabel("50-yard FG success rate")
plt.ylabel("Density")
plt.title('Posterior distribution ('+sys.argv[2]+" of "+sys.argv[1]+")")
ax.plot(x, post(x), 'k-', lw=2)
plt.show()

# probability the kicker is better than sys.argv[3] success rate kicker and worse than sys.argv[4]

#prior 

print(integrate.quad(prior, float(sys.argv[3]), float(sys.argv[4]))[0])

# posterior

print(integrate.quad(post, float(sys.argv[3]), float(sys.argv[4]))[0])
