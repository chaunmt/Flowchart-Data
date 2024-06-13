# Course Flowchart Data
Course Flowchart's Data Server

__Table of Contents__
- [Course Flowchart Data](#course-flowchart-data)
  - [1. How to run?](#1-how-to-run)
    - [Main](#main)
    - [Test](#test)
    - [Clean](#clean)
  - [2. Python](#2-python)
    - [Filter](#filter)
    - [Helper](#helper)
    - [Converter](#converter)
  - [3. PostgreSQL](#3-postgresql)
  - [4. Sample](#4-sample)
  - [5. Configuration](#5-configuration)

## 1. How to run?
- Run from `src/python`.

### Main
    python3 -m sources

### Test
    # Run all tests
    python3 -m run_tests

    # Run a module test
    python3 -m Test.test_file_name.module_name

    # Run a method test
    python3 -m Test.test_file_name.module_name.method_name

- `run_tests.py` can be modified to run only specified tests.
- For more information, check: [unnittest documentation](https://docs.python.org/3/library/unittest.html)

### Clean
    pylint filename

## 2. Python

### Filter
- Applying Decorator Design Pattern to make sure that objects come in and out with the same type. Each filter only allows a certain type of object to be processed.
- Folder's structure:
    + `filter.py` holds the base class Filter for all filters.
    + `prereq_filter.py` holds all filters dedicated for PrereqFormat type object.
    + `course_filter.py` holds all filters dedicated for Course type object.
    + `string_filter.py` holds all filters dedicated for string type object.

### Helper
- Helper classes and methods to help cleaning and modifying our data.
- Folder's structure:
    + Checker: classes and methods that output a boolean as the result of a valuation on an object.
        + `course_checker.py` holds all checkers dedicated for Course type object.
        + `string_checker.py` holds all checkers dedicated for String type object.
    + `new_types.py` defines all the newly created types to be used in our project: CourseShell, Course, PrereqFormat, ProgramShell, Program.
    + `string_splitter.py` holds all classes and methods that can help split a string into a list of strings.

### Converter
- Converter classes and methods to help with the converting process.
- Folder's structure:
    + `nested_course_converter.py` holds all converters dedicated to encoded, decoded, and reformat our nested course info strings.
    + `prereq_logic_converter.py` holds all converters dedicated to implement logic into our prerequisites.

## 3. PostgreSQL
- ...
  
## 4. Sample
- All JavaScript and TypeScript files can be found in src/jsts. They are used as references for the python files.

## 5. Configuration
- `.pylintrc` holds the configuration for pylint.
