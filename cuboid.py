import numpy as np
import scipy.io as sio
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def generate_cuboid_points(length=10, width=1, height=1, resolution=20):
    # Create grids for each dimension
    x = np.linspace(0, length, resolution)
    y = np.linspace(0, width, resolution)
    z = np.linspace(0, height, resolution)
    x, y, z = np.meshgrid(x, y, z)

    # Flatten the arrays to create a list of 3D coordinates
    points = np.vstack([x.ravel(), y.ravel(), z.ravel()]).T

    # Select points on the cuboid surfaces
    x1b = points[points[:, 0] == 0]   # Front face (x=0)
    x1u = points[points[:, 0] == length]  # Back face (x=length)
    x2b = points[points[:, 1] == 0]   # Left face (y=0)
    x2u = points[points[:, 1] == width]  # Right face (y=width)
    x3b = points[points[:, 2] == 0]   # Bottom face (z=0)
    x3u = points[points[:, 2] == height]  # Top face (z=height)
    xy = points  # All points in the cuboid

    return x1b, x1u, x2b, x2u, x3b, x3u, xy

# Generate cuboid points
x1b, x1u, x2b, x2u, x3b, x3u, xy = generate_cuboid_points()

# Save the data to a .mat file
sio.savemat('Cuboid_geometries.mat', {
    'x1b': x1b,
    'x1u': x1u,
    'x2b': x2b,
    'x2u': x2u,
    'x3b': x3b,
    'x3u': x3u,
    'xy': xy
})

# Plot the points to verify the geometry
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Plot each set of points with a different color
ax.scatter(x1b[:, 0], x1b[:, 1], x1b[:, 2], color='r', label='x1b (Front Face)')
ax.scatter(x1u[:, 0], x1u[:, 1], x1u[:, 2], color='g', label='x1u (Back Face)')
ax.scatter(x2b[:, 0], x2b[:, 1], x2b[:, 2], color='b', label='x2b (Left Face)')
ax.scatter(x2u[:, 0], x2u[:, 1], x2u[:, 2], color='y', label='x2u (Right Face)')
ax.scatter(x3b[:, 0], x3b[:, 1], x3b[:, 2], color='c', label='x3b (Bottom Face)')
ax.scatter(x3u[:, 0], x3u[:, 1], x3u[:, 2], color='m', label='x3u (Top Face)')

ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')

ax.legend()
ax.set_title('Cuboid Geometry Verification')
plt.show()
