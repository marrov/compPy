import numpy as np
import time as t

n = 256
a = np.ones((n, n))
b = np.ones((n, n))
c = np.zeros((n, n))

t1 = t.clock()
for i in range(n):
    for j in range(n):
        for k in range(n):
            c[i, j] += a[i, k]*b[k, j]
t2 = t.clock()
print("Loop timing", t2-t1)

t1 = t.clock()
d = np.dot(a, b)
t2 = t.clock()
print("Dot timing", t2-t1)
