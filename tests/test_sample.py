import pytest

class tests_regressions:

    @pytest.mark.smoke
    def test_01_check(self):

        print("++++++++++++++++++++++++++++++++++++++++++++++++")
        assert 1 + 1 == 2


# if __name__ == '__main__':
#     tests_regressions.test_01()
