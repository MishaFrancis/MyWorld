import pytest
import site

class test_regression:
    @pytest.mark.smoke
<<<<<<< HEAD
    def test_01():
        print("+++++++++++++sdsd++")
        assert 1 + 1 == 2
=======
    def test_01():
        print("++++++++++++++++++++++++++++++++++++++++++++++++")
        assert 1 + 1 == 2
>>>>>>> ff8e9073407197ed88c926494e4ccb3366f6b7e9


if __name__ == '__main__':
    test_regression.test_01()




