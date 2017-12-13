import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import os

cur_dir = os.path.dirname(os.path.abspath(__file__))
loadName = os.path.join(cur_dir, "reconstruction_global/colorized.ply")

try:
    f = open(loadName, 'r')
except IOError:
    print "Error loading file"
    sys.exit()

content = "start"
while content != "end_header":
    content = f.readline()
    content = content.strip()

full = np.loadtxt(f, dtype=np.float64)

x = full[:, 0]
y = full[:, 1]
z = full[:, 2]
rgb = full[:, 3:]
rgb = np.divide(rgb, np.array([255.0]))

fig = plt.figure()
ax = fig.add_subplot(111, projection = '3d')
ax.scatter(x, y, z, s=10, c=rgb)
plt.show()
