import numpy as np
import matplotlib.pyplot as plt
rng = np.random.default_rng()



data = rng.normal(0, 1, 1000)

# Compute histogram
hist, bins = np.histogram(data, bins=10)

print("Histogram counts:", hist)
print("Bin edges:", bins)

plt.hist(data, bins=10)
plt.show()