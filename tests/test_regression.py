import pytest
import os
import requests
import json
import sqlite3
import mysql.connector
from mysql.connector import connect
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
    def test_06_send_data_with_an_API_and_check_data(self):
        print('In Progress with API')


    @pytest.mark.smoke
    @pytest.mark.db
    def test_07_insert_query_data_from_mysql_db_and_print(self):

        conn = connect(
        user = 'root',
        password = 'admin',
        host = 'localhost',
        database = 'movies')
#       database = 'mysql')

        print('A connection object has been created.')

        cursor = conn.cursor()
        
        # Below is the insert query to add data to the DB
        query = 'INSERT INTO users VALUE (CURTIME(),"Tom",CURTIME())'
        cursor.execute(query)

        # Below is the select query to check the DB
        name = "Tom"
        query = 'SELECT * FROM users WHERE name = {name}'
        cursor.execute(query)
        result = cursor.fetchall()
 
        # print the results in each row
        for r in result:
          print(r)
    
        # commit and close db connection
        conn.commit()
        conn.close()




# if __name__ == '__main__':
#     Test_regression.test_01()
#     Test_regression.test_02()
