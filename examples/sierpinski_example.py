from fractalplots import generate_sierpinski, plot_sierpinski

# Define initial triangle points
p1 = (0, 0)
p2 = (1, 0)
p3 = (0.5, 0.866)  # height of equilateral triangle

# Generate triangle list
triangles = generate_sierpinski(order=5, p1=p1, p2=p2, p3=p3)

# Plot and save
plot_sierpinski(triangles, show=False, save_path="examples/output/sierpinski.png")
