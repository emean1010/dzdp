<<<<<<< Updated upstream
# %matplotlib inline
=======
>>>>>>> Stashed changes
from IPython.core.pylabtools import figsize
import numpy as np
from matplotlib import pyplot as plt
figsize(12.5, 4)
<<<<<<< Updated upstream
plt.rcParams['savefig.dpi'] = 300
plt.rcParams['figure.dpi'] = 300

colors = ["#348ABD","#A60628"]
prior = [1/21., 20/21.]
posterior = [0.087,1-0.087]
plt.bar([0, .7], prior, alpha = 0.70, width = 0.25,color=colors[0],label="prior distribution",lw="3", edgecolor="#348ABD")

plt.bar([0+0.25, .7+0.25],posterior,alpha=0.7,width=0.25, color=colors[1],label="posterior distribution",lw="3",edgecolor="#A60628")

plt.xticks([0.20, 0.95], ["Librarian","Farmer"])
plt.title("Prior and posterior\
          occupation")
plt.ylabel("Probability")
plt.legend(loc="upper left")
plt.show()
=======

import scipy.stats as stats
a = np.arange(16)
poi = stats.poisson
lambda_ = [1.5, 4.25]
colors = ["#348ABD", "#A60628"]

plt.bar(a, poi.pmf(a, lambda_[0]), color=colors[0],
       label="$\lambda = %.1f$" % lambda_[0], alpha=0.60,
       edgecolor=colors[0], lw="3")
plt.show()
plt.bar(a, poi.pmf(a, lambda_[1]), color=colors[1],
       label="$\lambda = %.1f$" % lambda_[1], alpha=0.60,
       edgecolor=colors[1], lw="3")
plt.xticks(a + 0.4, a)
plt.legend()
plt.ylabel("Probability of $k$")
plt.xlabel("$k$")
plt.title("Probability mass function of a Poisson random variable,\
         differing \$\lambda$ values")
>>>>>>> Stashed changes
