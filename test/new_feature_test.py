
from app.new_feature import announce #from my_script import enlarge


def test_enlarge():
    result = announce()
    assert result == "Hello World new test"