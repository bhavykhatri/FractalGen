from fractalplots import generate_barnsley_fern, plot_barnsley_fern

points = generate_barnsley_fern(n_points=100000)
plot_barnsley_fern(points, show=False, save_path="examples/output/barnsley.png")
