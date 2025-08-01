from fractalplots import generate_koch

def test_koch_point_count():
    # For order 0, it's a triangle: 3 sides + 1 closing point
    points = generate_koch(order=0)
    assert len(points) >= 4

    # For higher order, point count should increase
    points_3 = generate_koch(order=3)
    assert len(points_3) > len(points)
