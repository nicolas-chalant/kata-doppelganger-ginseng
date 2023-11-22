import pytest
import sys 
import pathlib
sys.path.append(pathlib.Path(__file__).parent.absolute().parent)  

from safe_calculator import SafeCalculator

class AuthorizerStub:
    def authorize(self):
        return False

def test_add_should_raise_error_when_not_authorized():
    authorizer = AuthorizerStub()
    calculator = SafeCalculator(authorizer)

    with pytest.raises(Exception) as excinfo:
        calculator.add(5, 7)
    
    assert str(excinfo.value) == "Not authorized"