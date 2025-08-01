def test_generate_mandelbrot_runs():
    from fractalgen import generate_mandelbrot
    result = generate_mandelbrot(-2.0, 1.0, -1.5, 1.5, 10, 10, 10)
    assert result.shape == (10, 10)
