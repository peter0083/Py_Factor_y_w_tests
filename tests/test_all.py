# Testing the functions in 
import pytest
#import pandas as pd
from py_factor_y import my_py_sd

def test_for_zeros():
    with pytest.raises(ZeroDivisionError):
        my_py_sd.standard_deviation([])

def test_correct():
    assert my_py_sd.standard_deviation([1, 2]) == 0.5
    assert my_py_sd.standard_error([1, 1]) == 0

def test_for_type1():
    with pytest.raises(TypeError):
        my_py_sd.standard_error(56)

def test_for_type2():
    with pytest.raises(TypeError):
        my_py_sd.standard_deviation(["1234", "2345"])

#def test_for_df():
#    Df = pd.DataFrame({“Testing”:[“Yes”, “No”], “Numbers”:[1, 2]})
#    assert my_py_sd.stanard_deviation(Df.Numbers) == 0.5



