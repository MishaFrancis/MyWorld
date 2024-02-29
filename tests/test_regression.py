import pytest

class Test_regression:
    @pytest.mark.smoke
    def test_01(self):
        print("+++++++++++++++++++++++++++++++++++")

    @pytest.mark.smoke
    def test_02(self):
        assert 5 == 5
        print("=========333==d=d=======")

# if __name__ == '__main__':
#     Test_regression.test_01()
#     Test_regression.test_02()
