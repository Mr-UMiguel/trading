import sys
from queue import Queue
import pandas as pd
import numpy as np



q = Queue()
l = list()
s = pd.Series()
a = np.empty((1))


for i in range(10000):
    q.put(i)
    l.append(i)
    s = pd.concat([s,pd.Series([i])])
    a = np.concatenate([a,np.array([i])])



print(sys.getsizeof(q.queue))
print(sys.getsizeof(l))
print(sys.getsizeof(s))
print(sys.getsizeof(a))