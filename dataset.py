import numpy as np
import pandas as pd
# Generate a random dataset
X = np.random.rand(1000, 10)
y = np.random.randint(2, size=1000)

# Concatenate X and y into a single array
data = np.concatenate((X, y[:, np.newaxis]), axis=1)
np.savetxt("array.csv", data, delimiter=",")
# Save the dataset to a file
np.save("mydata.npy", data)
