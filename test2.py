import numpy as np
import itertools
R = list(itertools.product([0, 1], repeat=2))

centroids = np.empty((2, 2), dtype='object')
centroids[:, 0] = np.random.choice(1,2)
centroids[:, 1] = np.random.choice(2,2)
print centroids
print R
for centroid in centroids:
    print tuple(centroid)
    if R.__contains__(tuple(centroid)):
        R.remove(tuple(centroid))
print R