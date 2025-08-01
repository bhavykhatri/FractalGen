import matplotlib.pyplot as plt

def generate_sierpinski(order, p1, p2, p3):
    if order == 0:
        return [(p1, p2, p3)]
    else:
        mid12 = midpoint(p1, p2)
        mid23 = midpoint(p2, p3)
        mid31 = midpoint(p3, p1)

        return (
            generate_sierpinski(order - 1, p1, mid12, mid31) +
            generate_sierpinski(order - 1, p2, mid23, mid12) +
            generate_sierpinski(order - 1, p3, mid31, mid23)
        )

def midpoint(p1, p2):
    return ((p1[0]+p2[0])/2, (p1[1]+p2[1])/2)

def plot_sierpinski(triangles, show=True, save_path=None):
    plt.figure(figsize=(8, 8))
    for tri in triangles:
        x, y = zip(*(tri + (tri[0],)))  # Close the triangle
        plt.plot(x, y, 'k-')
    plt.axis('equal')
    plt.axis('off')
    plt.title("Sierpinski Triangle")
    if save_path:
        plt.savefig(save_path, dpi=150)
        print(f"Saved Sierpinski Triangle to {save_path}")
    if show:
        plt.show()
