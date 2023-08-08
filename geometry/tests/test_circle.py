from geometry import calculate_area
import pytest

def test_caluclate_area():
    result = calculate_area(1)
    assert result == 3.141592653589793, "Area of radius 1 is not pi"
    
def test_caluclate_area_negative():
    with pytest.raises(ValueError):
        calculate_area(-1)