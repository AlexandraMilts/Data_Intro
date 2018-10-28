#This is known as the General Binomial Probability Formula, and we use it to calculate the probability mass function (or PMF)
#  for a binomial variable. In other words, the we can use it to calculate the probability for each possible value for the variable
#  and use that information to determine the relative frequency of the variable values as a distribution.

#In Python, the scipy.stats.binom.pmf function encapsulates the general binomial probability formula, and you can use it
#  to calculate the probability of a random variable having a specific value (k, the number of successful observations) for a given number of experiments (n) where
#  the event being tested has a given probability (p), as demonstrated in the following code:

from scipy.stats import binom
from matplotlib import pyplot as plt
import numpy as np

n = 5
p = 0.25
x = np.array(range(0, n+1))

prob = np.array([binom.pmf(k, n, p) for k in x])

# Set up the graph
plt.xlabel('x')
plt.ylabel('Probability')
plt.bar(x, prob)
plt.show()