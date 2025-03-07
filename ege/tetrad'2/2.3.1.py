import numpy as np
import pandas as pd
a = pd. Series ([1, 2, 3])
b = pd.Series([4, 5, 6])
rast= np.sqrt(np.sum((a - b) ** 2))
print(rast)