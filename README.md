This is my world to see how version control and git/commit/push/pull works

## Below is the command to run with report
pytest -m smoke --html=reports.html


## Running the tests with the -v flag to increase verbosity shows the tests passing:
pytest -v test_files.py
============================= test session starts ==============================
Python 3.9.6, pytest-6.2.5, py-1.11.0, pluggy-1.0.0 
cachedir: .pytest_cache
rootdir: /private/
collected 2 items

test_files.py::TestIsDone::test_yes PASSED                               [ 50%]
test_files.py::TestIsDone::test_no PASSED                                [100%]

============================== 2 passed in 0.00s ===============================
