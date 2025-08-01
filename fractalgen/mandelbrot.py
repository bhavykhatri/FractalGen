import numpy as np
import matplotlib.pyplot as plt

def generate_mandelbrot(xmin=-2.0, xmax=1.0, ymin=-1.5, ymax=1.5,
                        width=800, height=800, max_iter=100):
    x = np.linspace(xmin, xmax, width)
    y = np.linspace(ymin, ymax, height)
    C = x[:, None] + 1j * y[None, :]
    Z = np.zeros_like(C, dtype=complex)
    div_time = np.full(C.shape, max_iter)

    for i in range(max_iter):
        Z = Z**2 + C
        diverged = np.abs(Z) > 2
        div_now = diverged & (div_time == max_iter)
        div_time[div_now] = i
        Z[diverged] = 2

    return div_time

def plot_mandelbrot(div_time, extent=[-2, 1, -1.5, 1.5], show=True, save_path=None):
    """
    Plot the Mandelbrot fractal.

    Args:
        div_time (ndarray): 2D array of divergence times from generate_mandelbrot.
        extent (list): Plotting extent for imshow [xmin, xmax, ymin, ymax].
        show (bool): If True, display the image interactively using plt.show().
        save_path (str or None): If set, save the plot to this file path.
    """
    plt.imshow(div_time.T, cmap='inferno', extent=extent)
    plt.colorbar(label='Iteration count')
    plt.title("Mandelbrot Set")
    plt.tight_layout()

    if save_path:
        plt.savefig(save_path, dpi=150)
        print(f"Saved Mandelbrot image as {save_path}")

    if show:
        try:
            plt.show()
        except Exception as e:
            print(f"Could not display plot: {e}")