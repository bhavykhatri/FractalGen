from fractalgen import generate_sierpinski

def test_sierpinski_triangle_count():
    p1 = (0, 0)
    p2 = (1, 0)
    p3 = (0.5, 0.866)
    triangles = generate_sierpinski(order=3, p1=p1, p2=p2, p3=p3)
    
    # For order n, there are 3^n triangles
    assert len(triangles) == 3**3
