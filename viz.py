import numpy as np
import matplotlib.pyplot as plt

def plot_shape(original, transformed, matrix, title=""):
    print(title)
    print(matrix)

    plt.fill(original[0], original[1], alpha=0.5, label="Original")
    plt.fill(transformed[0], transformed[1], alpha=0.5, label="Transformed")
    plt.axis("equal")
    plt.title(title)
    plt.legend()
    plt.show()

def plot_points(X, matrix, title=""):
    print(title)
    print(matrix)

    lim = np.linalg.norm(X, axis=0).max()

    ax = plt.figure().add_subplot(projection="3d")
    ax.scatter(X[0], X[1], X[2], c=X[2], s=1)
    ax.set_xlim(-lim, lim)
    ax.set_ylim(-lim, lim)
    ax.set_zlim(-lim, lim)
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")
    ax.set_title(title)
    plt.show()