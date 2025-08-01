from fractalgen import generate_julia, plot_julia

# Example Julia set with complex parameter c
c = complex(-0.7, 0.27015)
div_time = generate_julia(c, width=800, height=800, max_iter=100)

# Plot and save
plot_julia(div_time, show=False, save_path="examples/output/julia.png")
