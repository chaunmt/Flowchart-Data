# Course-Flowchart-Data
Course Flowchart's Data Server

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

## 4. Client
- ...