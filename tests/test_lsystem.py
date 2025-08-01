from fractalplots import generate_lsystem

def test_lsystem_length_increases():
    axiom = "F"
    rules = {"F": "F+F-F"}
    
    string_1 = generate_lsystem(axiom, rules, iterations=1)
    string_2 = generate_lsystem(axiom, rules, iterations=2)
    
    assert isinstance(string_1, str)
    assert len(string_2) > len(string_1)
    assert "F" in string_2
