import math
import statistics
import numpy as np
import scipy.stats
import pandas as pd


x = [8.0, 1, 2.5, 4, 28.0]
x_with_nan = [8.0, 1, 2.5, math.nan, 4, 28.0]

y, y_with_nan = np.array(x), np.array(x_with_nan)
z, z_with_nan = pd.Series(x), pd.Series(x_with_nan)

w = [0.1, 0.2, 0.3, 0.25, 0.15]


# --------
# Mean
# --------

# Calculating mean using pure python
mean_of_x = sum(x) / len(x)

# Using Built-in Python Statistics
mean_of_y = statistics.mean(y)

# Using numpy
mean_of_z = np.mean(z)

mean_of_z_null = np.nanmean(z_with_nan)


# Weighted Mean
w_mean_01 = sum(w[i] * x[i] for i in range(len(x))) / sum(w)

# Using numpy
y, z, w = np.array(x), pd.Series(x), np.array(w)
w_mean_02 = np.average(y, weights=w)


# Harmonic Mean
scipy.stats.hmean(y)
scipy.stats.hmean(z)

# Geometric Mean
g_mean = 1
for item in x:
    g_mean *= item

g_mean **= 1 / len(x)

scipy.stats.gmean(y)


# -------
# Median
# -------

n = len(x)

if n % 2:
    median_ = sorted(x)[round(0.5 * (n-1))]
else:
    x_ord, index = sorted(x), round(0.5 * n)
    median_ = 0.5 * (x_ord[index - 1] + x_ord[index])

# Using numpy
median_01 = np.median(y)


