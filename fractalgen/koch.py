import matplotlib.pyplot as plt
import math

def generate_koch(order, length=1.0):
    def koch_curve(p1, p2, depth):
        if depth == 0:
            return [p1, p2]
        else:
            dx = (p2[0] - p1[0]) / 3
            dy = (p2[1] - p1[1]) / 3
            pA = (p1[0] + dx, p1[1] + dy)
            pB = (p1[0] + 2*dx, p1[1] + 2*dy)
            angle = math.atan2(dy, dx) - math.pi / 3
            px = pA[0] + math.cos(angle) * math.hypot(dx, dy)
            py = pA[1] + math.sin(angle) * math.hypot(dx, dy)
            pC = (px, py)
            return (
                koch_curve(p1, pA, depth - 1)[:-1] +
                koch_curve(pA, pC, depth - 1)[:-1] +
                koch_curve(pC, pB, depth - 1)[:-1] +
                koch_curve(pB, p2, depth - 1)
            )

    p1 = (0, 0)
    p2 = (length, 0)
    p3 = (length / 2, math.sqrt(3) * length / 2)

    side1 = koch_curve(p1, p2, order)
    side2 = koch_curve(p2, p3, order)
    side3 = koch_curve(p3, p1, order)
    return side1 + side2 + side3 + [p1]

def plot_koch(points, show=True, save_path=None):
    x, y = zip(*points)
    plt.figure(figsize=(8, 6))
    plt.plot(x, y)
    plt.axis('equal')
    plt.title("Koch Snowflake")
    if save_path:
        plt.savefig(save_path, dpi=150)
        print(f"Saved Koch Snowflake to {save_path}")
    if show:
        plt.show()
