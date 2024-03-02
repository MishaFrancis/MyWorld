import pytest
import os
import requests
from dotenv import load_dotenv
load_dotenv()

class Test_regression:
    @pytest.mark.smoke
    def test_01_Simple_print_output_check(self):

        print("+++++++++++++++++++++++++++++++++++")

    @pytest.mark.smoke
    def test_02_simple_assert_check(self):

        assert 5 == 5

    @pytest.mark.smoke
    def test_03_simple_url_print_check(self):

        url = 'www.google.com'
        print (url)

    @pytest.mark.smoke
    def test_04_call_url_from_dotenv_and_print_check(self):

        url1 = os.getenv('url1')
        print(url1)

    @pytest.mark.smoke
    def test_05_call_an_API_and_get_data(self):

        response = requests.get("https://api.sampleapis.com/wines/reds")
        print(response)
        print(response.status_code)
        print('asdfasdf' + response.cookies)
        print(response.text)


# if __name__ == '__main__':
#     Test_regression.test_01()
#     Test_regression.test_02()
