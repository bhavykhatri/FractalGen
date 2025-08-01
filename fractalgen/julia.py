import numpy as np
import matplotlib.pyplot as plt

def generate_julia(c, xmin=-2, xmax=2, ymin=-2, ymax=2, width=800, height=800, max_iter=100):
    x = np.linspace(xmin, xmax, width)
    y = np.linspace(ymin, ymax, height)
    Z = x[:, None] + 1j * y[None, :]
    div_time = np.full(Z.shape, max_iter)

    for i in range(max_iter):
        Z = Z**2 + c
        mask = (np.abs(Z) > 2) & (div_time == max_iter)
        div_time[mask] = i
        Z[mask] = 2

    return div_time

def plot_julia(div_time, extent=[-2, 2, -2, 2], show=True, save_path=None):
    plt.imshow(div_time.T, cmap='magma', extent=extent)
    plt.colorbar(label="Escape time")
    plt.title("Julia Set")
    if save_path:
        plt.savefig(save_path, dpi=150)
        print(f"Saved Julia Set to {save_path}")
    if show:
        plt.show()
