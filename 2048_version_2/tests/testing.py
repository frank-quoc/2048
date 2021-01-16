import numpy as np

a = np.arange(16).reshape(4,4)

it = np.nditer(a, flags=['multi_index'])
for i in np.nditer(a, flags=['multi_index']):
    print(i, it.multi_index)