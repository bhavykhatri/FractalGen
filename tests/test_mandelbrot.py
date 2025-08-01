from fractalplots import generate_mandelbrot
import numpy as np

def test_mandelbrot_shape():
    result = generate_mandelbrot(width=100, height=80, max_iter=50)
    assert isinstance(result, np.ndarray)
    assert result.shape == (100, 80)
    assert result.dtype == np.int32 or result.dtype == np.int64
    assert result.max() <= 50
