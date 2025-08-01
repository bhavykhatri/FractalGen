import numpy as np
import matplotlib.pyplot as plt

def generate_barnsley_fern(n_points=100000):
    """
    Generate points of the Barnsley Fern using IFS rules.

    Args:
        n_points (int): Number of points to generate.

    Returns:
        ndarray: Array of shape (n_points, 2) with x, y coordinates.
    """
    points = np.zeros((n_points, 2))
    x, y = 0, 0

    for i in range(1, n_points):
        r = np.random.random()
        if r < 0.01:
            x, y = 0, 0.16 * y
        elif r < 0.86:
            x, y = 0.85 * x + 0.04 * y, -0.04 * x + 0.85 * y + 1.6
        elif r < 0.93:
            x, y = 0.20 * x - 0.26 * y, 0.23 * x + 0.22 * y + 1.6
        else:
            x, y = -0.15 * x + 0.28 * y, 0.26 * x + 0.24 * y + 0.44
        points[i] = [x, y]

    return points

def plot_barnsley_fern(points, show=True, save_path=None):
    """
    Plot the Barnsley Fern using generated point data.

    Args:
        points (ndarray): Array of x, y coordinates.
        show (bool): Whether to display the plot.
        save_path (str or None): Path to save the image.
    """
    x, y = points[:, 0], points[:, 1]
    plt.figure(figsize=(6, 10))
    plt.scatter(x, y, s=0.1, color="green", marker="o")
    plt.axis("off")
    plt.title("Barnsley Fern")

    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches="tight")
        print(f"Saved Barnsley Fern to {save_path}")

    if show:
        plt.show()
