import numpy as np
import matplotlib.pyplot as plt
square = np.array([
[0, 0],
[1, 0],
[1, 1],
[0, 1],
[0, 0]
])
def transform_points(points, matrix):
homogeneous_points = np.hstack([points, np.ones((points.shape[0], 1))])
transformed_points = homogeneous_points @ matrix.T
return transformed_points[:, :2]
def translation_matrix(tx, ty):
return np.array([
[1, 0, tx],
[0, 1, ty],
[0, 0, 1]
])
def rotation_matrix(angle):
rad = np.radians(angle)
return np.array([
[np.cos(rad), -np.sin(rad), 0],
[np.sin(rad), np.cos(rad), 0],
[0, 0, 1]
])
def scaling_matrix(sx, sy):
return np.array([
[sx, 0, 0],
[0, sy, 0],
[0, 0, 1]
])
def composite_transformation(points, tx, ty, angle, sx, sy):
translation = translation_matrix(tx, ty)
points = transform_points(points, translation)
rotation = rotation_matrix(angle)
points = transform_points(points, rotation)
scaling = scaling_matrix(sx, sy)
points = transform_points(points, scaling)
return points
tx, ty = 2, 1
angle = 45
sx, sy = 1.5, 0.5
transformed_square = composite_transformation(square, tx, ty, angle, sx, sy)
plt.figure()
plt.plot(square[:, 0], square[:, 1], label="Original Square")
plt.plot(transformed_square[:, 0], transformed_square[:, 1], label="Transformed
Square")
plt.axis("equal")
plt.legend()
plt.title("Composite 2D Transformations")
plt.grid(True)
plt.show()
