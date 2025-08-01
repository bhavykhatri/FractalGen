from fractalgen import generate_mandelbrot, plot_mandelbrot

# Generate the Mandelbrot set
div_time = generate_mandelbrot(xmin=-2.0, xmax=1.0, ymin=-1.5, ymax=1.5, width=800, height=800, max_iter=100)

# Plot and save
plot_mandelbrot(div_time, show=False, save_path="examples/output/mandelbrot.png")
