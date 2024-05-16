import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5, 5, num=100)
y = np.linspace(-5, 5, num=100)

x, y = np.meshgrid(x, y)

z = np.sin(np.sqrt(x**2 + y**2))

fig = plt.figure(figsize=(14, 6))

ax = fig.add_subplot(111, projection='3d')

ax.plot_surface(x, y, z, cmap='viridis')
ax.set_title('3D Plot')
ax.set_xlabel('X-Axis')
ax.set_ylabel('Y-Axis')
ax.set_zlabel('Z-Axis')

plt.show()