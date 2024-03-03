import pytest
import os
import requests
import json
import sqlite3
import mysql.connector
from pprint import pprint
from dotenv import load_dotenv
load_dotenv()

class Test_regression:

    @pytest.mark.smoke
    def test_01_simple_print_output_check(self):

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
    @pytest.mark.api
    def test_05_call_an_API_and_get_data(self):

        response = requests.get("https://api.sampleapis.com/wines/reds")
        print(response)
        print('++++++++++++++++++++++++++++++ The status code is ' + str(response.status_code) + ' ++++++++++++++++++++++++++++++')
        print('This is the cookie list ' + str(response.cookies))
        print('++++++++++++++++++++++++++++ Below is the API response +++++++++++++++++++++++++++++')
        print(response.text)


    @pytest.mark.smoke
    @pytest.mark.api
    @pytest.mark.db
    def test_06_send_data_with_an_API_and_check_data(self):

        print('TBD - In progress')
        
        conn = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="admin",
        database="mysql"
        )

        cursor = conn.cursor()
        conn.commit()
        conn.close()




# if __name__ == '__main__':
#     Test_regression.test_01()
#     Test_regression.test_02()
