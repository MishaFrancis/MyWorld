from mysql import connector
from mysql.connector.pooling import connect
import pytest
import os
import requests
import json
import sqlite3
import mysql
import mysql.connector
import test_urls
from pprint import pprint
from dotenv import load_dotenv
load_dotenv()

class Test_regression:

    @pytest.mark.smoke
    def test_01_simple_print_output_check(self):

        print("++++++++++++++++ Hello world ! +++++++++++++++++++")


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
    def test_05_call_an_API_and_get_data_from_another_file(self):

        url = test_urls.url                        # Read data from another file(test_urls.py)
        print(url)
     
        with open('json_file.json', 'r') as f:     # Load the data from the file(json_file.json)
            data = json.load(f)                          # Read data from the loaded file  
        print(data['url'])
        print(data['url1'])
    

    @pytest.mark.smoke
    @pytest.mark.api
    def test_06_call_an_API_and_get_data(self):

        response = requests.get("https://api.sampleapis.com/wines/reds")
        print(response)
        print('++++++++++++++++++++++++++++++ The status code is ' + str(response.status_code) + ' ++++++++++++++++++++++++++++++')
        print('This is the cookie list ' + str(response.cookies))
        print('++++++++++++++++++++++++++++ Below is the API response +++++++++++++++++++++++++++++')
        print(response.text)
    

    @pytest.mark.smoke
    @pytest.mark.api
    def test_07_send_data_with_an_API_and_check_data(self):

        response = requests.post("https://httpbin.org/post", 
                                data={"key": "value"},
                                headers={"Content-Type": "application/json"},
                                )

        print(response.json())
        print('++++++++++++++++++++++++++++++ The status code is ' + str(response.status_code) + ' ++++++++++++++++++++++++++++++')


    @pytest.mark.smoke
    @pytest.mark.db
    def test_08_insert_query_data_from_mysql_db_and_print(self):

        conn = connect(
        user = os.getenv('user'),
        password = os.getenv('password'),
        host = os.getenv('host'),
        database = os.getenv('database'))
        print('A connection object has been created.')

        cursor = conn.cursor()
        
        # Below is the insert query to add data to the DB
        query = 'INSERT INTO users VALUE (CURTIME(),"Tom",CURTIME())'
        cursor.execute(query)

        # Below is the select query to check the DB
        query = 'SELECT * FROM users WHERE name = "Tom"'
        cursor.execute(query)
        result = cursor.fetchall()
 
        # print the results in each row
        for r in result:
          print(r)
    
        # commit and close db connection
        conn.commit()
        conn.close()

    @pytest.mark.smoke
    def test_09_sort_assert_check(self):

        # Define an array
        my_array = [5, 2, 7, 3, 1, 9, 2, 0]

        # Sort the array using sort() method
        my_array.sort()

        # Remove duplicate values using set() method
        my_array = set(my_array)

        # Print the sorted array with unique values
        print("Sorted array with unique values:", my_array)



# if __name__ == '__main__':
#     obj = Test_regression()
#     obj.test_05_call_an_API_and_get_data_from_another_file()
