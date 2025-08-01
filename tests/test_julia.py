from fractalplots import generate_julia
import numpy as np

def test_julia_output():
    c = complex(-0.4, 0.6)
    result = generate_julia(c, width=120, height=90, max_iter=60)
    assert isinstance(result, np.ndarray)
    assert result.shape == (120, 90)
    assert result.max() <= 60
