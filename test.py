import numpy as np
from mpi4py import MPI
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Load the data
X, y = load_iris(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Initialize MPI
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

# Split the training data among the processes
X_train_split = np.array_split(X_train, size)
y_train_split = np.array_split(y_train, size)

# Train a model on the local portion of the training data
clf = RandomForestClassifier()
clf.fit(X_train_split[rank], y_train_split[rank])
accuracy = clf.score(X_train_split, y_train_split)

accuracies = comm.gather(accuracy, root=0)

# Gather the models from all processes

# The root process averages the models to create the ensemble model
if rank == 0:
    print(f"Final accuracy: {np.mean(accuracies)}")


