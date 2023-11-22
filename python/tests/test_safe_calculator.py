# import pytest
# import sys 
# import pathlib
# from unittest.mock import MagicMock 
# sys.path.append(pathlib.Path(__file__).parent.absolute().parent)  

# from safe_calculator import SafeCalculator

# # class AuthorizerStub:
# #     def authorize(self):
# #         return False

# # def test_add_should_raise_error_when_not_authorized():
# #     authorizer = AuthorizerStub()
# #     calculator = SafeCalculator(authorizer)

# #     with pytest.raises(Exception) as excinfo:
# #         calculator.add(5, 7)
    
# #     assert str(excinfo.value) == "Not authorized"


# Test file
import pytest
from unittest.mock import MagicMock
from safe_calculator import SafeCalculator

def test_add_should_not_raise_any_error_when_authorized():
    # Create a test double for the authorizer that returns True
    authorizer_double = MagicMock()
    authorizer_double.authorize.return_value = True

    # Create an instance of SafeCalculator with the test double
    calculator = SafeCalculator(authorizer_double)

    # Try to add two numbers; the test should fail because of the bug in add
    try:
        calculator.add(2, 3)
    except Exception as e:
        assert str(e) == "Not authorized"
        pytest.fail("Exception raised unexpectedly")