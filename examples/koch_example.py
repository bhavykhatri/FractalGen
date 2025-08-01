from fractalplots import generate_koch, plot_koch

# Generate the points of the Koch snowflake
points = generate_koch(order=4, length=1.0)

# Plot and save
plot_koch(points, show=False, save_path="examples/output/koch.png")
