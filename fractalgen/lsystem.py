import matplotlib.pyplot as plt
import math

def generate_lsystem(axiom, rules, iterations):
    for _ in range(iterations):
        axiom = ''.join([rules.get(c, c) for c in axiom])
    return axiom

def draw_lsystem(instructions, angle=25, length=5, show=True, save_path=None):
    x, y = 0, 0
    angle_rad = math.radians(angle)
    direction = math.pi / 2
    stack = []
    points = [(x, y)]

    for cmd in instructions:
        if cmd == 'F':
            x += length * math.cos(direction)
            y += length * math.sin(direction)
            points.append((x, y))
        elif cmd == '+':
            direction += angle_rad
        elif cmd == '-':
            direction -= angle_rad
        elif cmd == '[':
            stack.append((x, y, direction))
        elif cmd == ']':
            x, y, direction = stack.pop()
            points.append((x, y))

    xs, ys = zip(*points)
    plt.figure(figsize=(8, 8))
    plt.plot(xs, ys)
    plt.axis('equal')
    plt.axis('off')
    plt.title("L-System Fractal")
    if save_path:
        plt.savefig(save_path, dpi=150)
        print(f"Saved L-system fractal to {save_path}")
    if show:
        plt.show()
