import pytest

class test_regression:
    @pytest.mark.smoke
    def test_01(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++")
        assert 1 + 1 == 5


if __name__ == '__main__':
    test_regression.test_01()
