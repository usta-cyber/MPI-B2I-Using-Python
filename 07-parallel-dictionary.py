from mpi4py import MPI

# Get the rank of the process and the size of the communicator
rank = MPI.COMM_WORLD.rank
size = MPI.COMM_WORLD.size

# Create a dictionary on the root process
if rank == 0:
    dictionary = {"a": 1, "b": 2, "c": 3}
else:
    dictionary = None

# Scatter the dictionary keys to the processes
Keys = MPI.COMM_WORLD.scatter(list(dictionary.keys()), root=0)

# On each process, print the received key and its corresponding value
print(f"Process {rank}: {Keys} = {dictionary[Keys]}")
