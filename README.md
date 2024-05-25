# Course-Flowchart-Data
Course Flowchart's Data Server

- [Course-Flowchart-Data](#course-flowchart-data)
  - [1. Filter](#1-filter)
  - [2. Helper](#2-helper)
  - [3. PostgreSQL](#3-postgresql)
  - [4. Test](#4-test)

## 1. Filter
- Applying Decorator Design Pattern to make sure the object comes in and out as the same type.
- Folder's structure:
  + filter.py holds the base class Filter for all filters.
  + prereq_filter.py holds all filters dedicated for PrereqFormat type object.
  + course_filter.py holds all filters dedicated for Course type object.
  + string_filter.py holds all filters dedicated for string type object.

## 2. Helper
- Helper classes and methods to help cleaning and modifying our data.
- Folder's structure:
  + Checker:
    + Checker classes and methods that give our a boolean as the result of a valuation of an object.
    + course_checker.py holds all checkers dedicated for Course type object.
    + string_checker.py holds all checkers dedicated for String type object.
  + new_types.py defines all the newly created types to be used in our project: Course, CourseShell, PrereqList, PrereqFormat.
  + string_splitter.py holds all classes and methods that can help split a string into an array of strings.

## 3. PostgreSQL
- ...

## 4. Test
- Run from src/python/.
- To run all tests specified in run_tests.py (default is to run all tests).
  ```
  python3 -m run_tests
  ```
- To test some classes or methods, modify run_tests.py file to only include the tests needed to be run or run them separately from the terminal.
  + To test a single class:<br>
    Modify run_tests.py
    ```
    from Test.test_file_name import test_module_name

    suite.addTest(unittest.makeSuite(test_module_name))
    ```
    or run it seprately from the terminal.
    ```
    python3 -m Test.test_file_name.module_name
    ```
  + To test a single method:<br>
    Modify run_tests.py
    ```
    from Test.test_file_name import test_module_name

    suite.addTest(test_module_name('test_method_name'))
    ```
    or run it seprately from the terminal.
    ```
    python3 -m Test.test_file_name.module_name.method_name
    ```
- For more information, check: [unnittest documentation](https://docs.python.org/3/library/unittest.html)