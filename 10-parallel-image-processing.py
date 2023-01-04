
from mpi4py import MPI
from PIL import Image

# Get the rank of the process and the size of the communicator
rank = MPI.COMM_WORLD.rank
size = MPI.COMM_WORLD.size

# Load the image on the root process
if rank == 0:
    image = Image.open("image.jpg")
else:
    image = None

# Scatter the image rows to the processes
rows = image.size[1]
local_rows = np.array_split(np.arange(rows), size)[rank]
local_image = image.crop((0, min(local_rows), image.size[0], max(local_rows)))

# Perform image processing on the local image
local_image = local_image.convert("L")
local_image = local_image.filter(ImageFilter.BLUR)

# Gather the local images on the root process
images = MPI.COMM_WORLD.gather(local_image, root=0)

# On the root process, stitch the images together
if rank == 0:
    images = [image] + images
    result = Image.new("RGB", image.size)
    y_offset = 0
    for im in images:
        result.paste(im, (0, y_offset))
        y_offset += im.size[1]
    result.save("result.jpg")
