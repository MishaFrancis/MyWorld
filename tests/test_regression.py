import pytest

class Test_regression:
    @pytest.mark.smoke
    def test_01(self):
        print("+++++++++++++++++++++++++++++++++++")

    @pytest.mark.smoke
    def test_02(self):

        print("=========333==d=d=======")
        assert 5 == 511

# if __name__ == '__main__':
#     Test_regression.test_01()
#     Test_regression.test_02()
