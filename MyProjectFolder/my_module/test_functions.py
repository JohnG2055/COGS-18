from my_module.functions import *
from unittest import mock

def test_find_categories():
    test_categories = GradeCalculator()

    with mock.patch('builtins.input', return_value='6'):    # https://learnbyexample.gitbooks.io/python-basics/content/Testing.html#using-unittest.mock-to-test-user-input-and-program-output
        
        test_categories.find_categories()

    assert test_categories.num_categories == 6
    assert isinstance(test_categories.num_categories, int)
