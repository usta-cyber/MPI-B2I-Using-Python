from mpi4py import MPI

# Get the rank of the process and the size of the communicator
rank = MPI.COMM_WORLD.rank
size = MPI.COMM_WORLD.size

# Create a graph on the root process
if rank == 0:
    graph = {"A": ["B", "C"], "B": ["C", "D"], "C": ["D"], "D": []}
else:
    graph = None

# Scatter the nodes of the graph to the processes
nodes = MPI.COMM_WORLD.scatter(list(graph.keys()), root=0)

# On each process, print the received node and its neighbors
print(f"Process {rank}: {nodes} -> {graph[nodes]}")
