import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt
import numpy as np

t = np.linspace(0, 2 * np.pi, 500)
x = np.sin(7 * np.pi * t)
y = np.cos(5 * np.pi * t)
fig = plt.figure()

plt.plot(x, y)
fig.savefig("parametric2")