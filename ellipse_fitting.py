import numpy as np
from ellipse import LsqEllipse
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse
import json


with open('data.json', 'r') as json_file:
    data = json.load(json_file)
# print(x, y)
x = []
y = []
for i in range(len(data)):
    x.append(data[i]["center_x"])
    y.append(data[i]["center_y"])
X1 = x
X2 = y
X = np.array(list(zip(X1, X2)))
reg = LsqEllipse().fit(X)
center, width, height, phi = reg.as_parameters()
print(f'center: {center[0]:.3f}, {center[1]:.3f}')
print(f'width: {width:.3f}')
print(f'height: {height:.3f}')
print(f'phi: {phi:.3f}')
with open('circle.json', 'w') as json_file:
    json_file.write(json.dumps(reg.as_parameters(), indent=4))
print(f'circle data stored in circle.json')
fig = plt.figure(figsize=(10, 10))
ax = plt.subplot()
ax.axis('equal')
ax.plot(X1, X2, 'ro', zorder=1)
ellipse = Ellipse(
    xy=center, width=2*width, height=2*height, angle=np.rad2deg(phi),
    edgecolor='b', fc='None', lw=2, label='Fit'
)
ax.add_patch(ellipse)
circle = plt.Circle((center[0], center[1]),
                    (width+height)/2,
                    fill=False)
ax.add_patch(circle)
plt.xlabel('$X_1$')
plt.ylabel('$X_2$')
plt.legend()
plt.show()
