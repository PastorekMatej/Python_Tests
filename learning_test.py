import pytest 
from format_conversion import conversion

def test_conversion():
    assert conversion("345") == 345
    assert conversion("3.456") == 3




