from .mandelbrot import generate_mandelbrot, plot_mandelbrot
from .koch import generate_koch, plot_koch
from .sierpinski import generate_sierpinski, plot_sierpinski
from .julia import generate_julia, plot_julia
from .lsystem import generate_lsystem, draw_lsystem

__all__ = [
    "generate_mandelbrot", "plot_mandelbrot",
    "generate_koch", "plot_koch",
    "generate_sierpinski", "plot_sierpinski",
    "generate_julia", "plot_julia",
    "generate_lsystem", "draw_lsystem"
]
