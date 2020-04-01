# testing-123/test/my_test.py

#from my_script import enlarge
from app.my_script import enlarge

def test_enlarge():
    result = enlarge(3)
    assert result == 300