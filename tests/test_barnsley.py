from fractalplots import generate_barnsley_fern

def test_barnsley_shape():
    points = generate_barnsley_fern(n_points=5000)
    assert points.shape == (5000, 2)
    assert abs(points[:, 0]).max() < 5  # bounding box check
    assert points.dtype == float
