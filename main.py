# Arrays used as indices must be of integer (or boolean) type

import numpy as np

indices_array = np.array([
    [0, 1.1, 2],
    [1.3, 3.2, 2]
])

# [[0.  1.1 2. ]
#  [1.3 3.2 2. ]]
print(indices_array)