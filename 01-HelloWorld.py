from mpi4py import MPI

# Get the rank of the process and the size of the communicator
rank = MPI.COMM_WORLD.rank
size = MPI.COMM_WORLD.size

# If we are the root process, send a message to the other process
if rank == 0:
    message = "Hello from process 0"
    MPI.COMM_WORLD.send(message, dest=1)

# If we are the other process, receive the message from the root process
if rank == 1:
    message = MPI.COMM_WORLD.recv(source=0)
    print(f"Received message: {message}")
