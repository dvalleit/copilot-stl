from stl import mesh
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D, art3d

# Load the STL file
your_mesh = mesh.Mesh.from_file('cube.stl')

# Create a new plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Add the STL mesh to the plot
ax.add_collection3d(art3d.Poly3DCollection(your_mesh.vectors))

# Auto scale to the mesh size
scale = your_mesh.points.flatten("A")
ax.auto_scale_xyz(scale, scale, scale)

# Show the plot
plt.show()