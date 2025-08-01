from fractalplots import generate_lsystem, draw_lsystem

# Define L-system rules for a fractal tree
axiom = "F"
rules = {
    "F": "F[+F]F[-F]F"
}

# Generate instructions and draw
instructions = generate_lsystem(axiom=axiom, rules=rules, iterations=4)
draw_lsystem(instructions, angle=25, length=5, show=False, save_path="examples/output/lsystem.png")
