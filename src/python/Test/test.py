"""
This file contains all testcases for this project.
- def setUp(self) is automatically called before any test of its class is run.
- def tearDown(self) is automatically called after any test of its class is run.
"""
import unittest

from Helper.new_types import *
from Helper.string_splitter import *
from Helper.Checker.string_checker import *
from Helper.Checker.course_checker import *

from Filter.filter import *
from Filter.string_filter import *
from Filter.course_filter import *
from Filter.prereq_filter import *

def merge_lists(list1, list2):
  """
  Merge members at the same index of 2 lists together.
  """
  merged_list = []
  for first, second in zip(list1, list2):
    merged_list.append({**first, **second})

  return merged_list

def assert_eq(result, goal):
  """
  Assert whether result equals goal.\n
  If not, print out the unwanted result.
  """
  assert result == goal, f"Unwanted result: {result}"

class TestString(unittest.TestCase):
  """
  Parent class to set up and tear down all child classes.
  """
  def setUp(self):
    self.s1 = "Hello, world!"
    self.s2 = "Python  is   fun!"
    self.s3 = "12!3 !4.5"
    self.s4 = "C?S1!0^1@"
    self.s5 = "This ! is ? a ^ test."
    self.s6 = "!@#$%^&*()"
    self.s7 = ""
    self.s8 = "   1   "
    
  def tearDown(self):
    pass

class TestCourse(unittest.TestCase):
  """
  Parent class to set up and tear down all child classes.
  """
  def setUp(self):
    self.course_shell_data = [
      {
        'uid_': '1',
        'code_': 'CSC101',
        'subject_': 'Computer Science',
        'number_': '101',
      },
      {
        'uid_': '2',
        'code_': 'CSC101',
        'subject_': 'Computer Science',
        'number_': '101',
      },
      {
        'uid_': '3',
        'code_': 'CSC102',
        'subject_': 'Computer Science',
        'number_': '102',
      }
    ]

    self.additional_data = [
      {
        'name_': 'Introduction to Computer Science',
        'longname_': 'CS 101',
        'info_': 'Introductory course covering basic concepts in computer science.',
        'prereq_': None
      },
      {
        'name_': 'Introduction to Computer Science',
        'longname_': 'CS 101',
        'info_': 'Introductory course covering basic concepts in computer science.',
        'prereq_': None
      },
      {
        'name_': 'Data Structures',
        'longname_': 'CS 102',
        'info_': 'A course focusing on data structures and algorithms.',
        'prereq_': None
      }
    ]

    # Merge course_shell_data with additional attributes for each course
    self.course_data = merge_lists(self.course_shell_data, self.additional_data)

    # Initialize CourseShell objects
    self.course_shells = [CourseShell(**data) for data in self.course_shell_data]

    # Initialize Course objects
    self.courses = [Course(**data) for data in self.course_data]

  def tearDown(self):
    pass

class TestFilter(unittest.TestCase):
  """
  Test module filter.
  """
  # Class Filter is tested with its children classes
  pass

class TestNewTypes(TestCourse, TestString):
  """
  Test module new_types
  """
  def test_course_shell(self):
    for index, shell in enumerate(self.course_shells):
      assert_eq(shell.uid, self.course_shell_data[index]['uid_'])
      assert_eq(shell.code, self.course_shell_data[index]['code_'])
      assert_eq(shell.subject, self.course_shell_data[index]['subject_'])
      assert_eq(shell.number, self.course_shell_data[index]['number_'])

  def test_course(self):
    for index, course in enumerate(self.courses):
      assert_eq(course.uid, self.course_data[index]['uid_'])
      assert_eq(course.code, self.course_data[index]['code_'])
      assert_eq(course.subject, self.course_data[index]['subject_'])
      assert_eq(course.number, self.course_data[index]['number_'])
      assert_eq(course.name, self.course_data[index]['name_'])
      assert_eq(course.longname, self.course_data[index]['longname_'])
      assert_eq(course.info, self.course_data[index]['info_'])
      assert_eq(course.prereq, self.course_data[index]['prereq_'])

  def test_prereq_courses(self):
    pass

  def test_prereq_list(self):
    pass
  
class TestStringSplitter(TestString):
  """
  Test module string_splitter.
  """
  def test_at_index(self):
    assert_eq(StringSplitter.at_index(self.s1, 5), ['Hello,', ' world!'])
    assert_eq(StringSplitter.at_index(self.s1, 7), ['Hello, w', 'orld!'])
    assert_eq(StringSplitter.at_index(self.s2, 11), ['Python  is  ', ' fun!'])
    assert_eq(StringSplitter.at_index(self.s3, 3), ['12!3', ' !4.5'])
    assert_eq(StringSplitter.at_index(self.s3, 5), ['12!3 !', '4.5'])
    assert_eq(StringSplitter.at_index(self.s6, 3), ['!@#$', '%^&*()'])

  def test_at_substring(self):
    assert_eq(StringSplitter.at_substring(self.s1, ','), ['Hello', ' world!'])
    assert_eq(StringSplitter.at_substring(self.s1, 'world'), ['Hello, ', '!'])
    assert_eq(StringSplitter.at_substring(self.s2, ' '), ['Python', 'is', 'fun!'])
    assert_eq(StringSplitter.at_substring(self.s2, '  '), ['Python', 'is', ' fun!'])
    assert_eq(StringSplitter.at_substring(self.s3, '!'), ['12', '3 ', '4.5'])
    assert_eq(StringSplitter.at_substring(self.s3, '12!'), ['3 !4.5'])
    assert_eq(StringSplitter.at_substring(self.s4, '?S1'), ['C', '!0^1@'])
    assert_eq(StringSplitter.at_substring(self.s5, '^'), ['This ! is ? a ', ' test.'])
    assert_eq(StringSplitter.at_substring(self.s6, '*'), ['!@#$%^&', '()'])

  def test_at_first_type_occurrence(self):
    # Test wrong split_type
    self.assertRaises(
      ValueError,
      StringSplitter.at_first_type_occurrence, self.s1, 'word'
    )

    # Test splitting at the first letter occurrence
    assert_eq(
      StringSplitter.at_first_type_occurrence(self.s1, 'letter'),
      ['H', 'ello, world!']
    )
    assert_eq(
      StringSplitter.at_first_type_occurrence(self.s3, 'letter'),
      ['12!3 !4.5', None]
    )
    assert_eq(
      StringSplitter.at_first_type_occurrence(self.s4, 'letter'),
      ['C', '?S1!0^1@']
    )

    # Test splitting at the first number occurrence
    assert_eq(
      StringSplitter.at_first_type_occurrence(self.s3, 'number'),
      ['1', '2!3 !4.5']
    )
    assert_eq(
      StringSplitter.at_first_type_occurrence(self.s1, 'number'),
      ['Hello, world!', None]
    )
    assert_eq(
      StringSplitter.at_first_type_occurrence(self.s6, 'number'),
      ['!@#$%^&*()', None]
    )
    assert_eq(
      StringSplitter.at_first_type_occurrence(self.s4, 'number'),
      ['C?S1', '!0^1@']
    )

  def test_at_last_type_occurrence(self):
    # Test wrong split_type
    self.assertRaises(
      ValueError,
      StringSplitter.at_last_type_occurrence, self.s1, 'word'
    )

    # Test splitting at the last letter occurrence
    assert_eq(
      StringSplitter.at_last_type_occurrence(self.s1, 'letter'),
      ['Hello, world', '!']
    )
    assert_eq(
      StringSplitter.at_last_type_occurrence(self.s3, 'letter'),
      ['12!3 !4.5', None]
    )
    assert_eq(
      StringSplitter.at_last_type_occurrence(self.s4, 'letter'),
      ['C?S', '1!0^1@']
    )

    # Test splitting at the last number occurrence
    assert_eq(
      StringSplitter.at_last_type_occurrence(self.s3, 'number'),
      ['12!3 !4.5', None]
    )
    assert_eq(
      StringSplitter.at_last_type_occurrence(self.s1, 'number'),
      ['Hello, world!', None]
    )
    assert_eq(
      StringSplitter.at_last_type_occurrence(self.s6, 'number'),
      ['!@#$%^&*()', None]
    )
    assert_eq(
      StringSplitter.at_last_type_occurrence(self.s4, 'number'),
      ['C?S1!0^1', '@']
    )

  def test_code_into_subj_id(self):
    """Need to change type name"""
    pass

  def test_id_into_num_suffix(self):
    """Need to change type name"""
    pass

class TestStringChecker(TestString):
  """
  Test module string_checker.
  """
  def test_has_number(self):
    assert StringChecker.has_number(self.s1) == False
    assert StringChecker.has_number(self.s3) == True
    assert StringChecker.has_number(self.s4) == True
    assert StringChecker.has_number(self.s5) == False
    assert StringChecker.has_number(self.s7) == False
    assert StringChecker.has_number(self.s8) == True

  def test_has_word(self):
    assert StringChecker.has_letter(self.s2) == True
    assert StringChecker.has_letter(self.s3) == False
    assert StringChecker.has_letter(self.s4) == True
    assert StringChecker.has_letter(self.s5) == True
    assert StringChecker.has_letter(self.s6) == False
    assert StringChecker.has_letter(self.s7) == False

  def test_includes(self):
    assert StringChecker.includes(self.s1, "Hello") == True
    assert StringChecker.includes(self.s3, "123") == False
    assert StringChecker.includes(self.s4, "!0") == True
    assert StringChecker.includes(self.s6, "!@#$%^&*()") == True
    assert StringChecker.includes(self.s6, "!@#$%^&*() ") == False
    assert StringChecker.includes(self.s7, "") == True
    assert StringChecker.includes(self.s8, "") == True

class TestCourseChecker(TestCourse):
  """
  Test module course_checker.
  """
  def test_is_equal(self):
    # Test for Course type
    assert CourseChecker.is_equal(self.courses[0], self.courses[0]) == True
    assert CourseChecker.is_equal(self.courses[0], self.courses[1]) == False
    assert CourseChecker.is_equal(self.courses[0], self.courses[2]) == False

    # Test for CourseShell type
    assert CourseChecker.is_equal(self.course_shells[0], self.course_shells[0]) == True
    assert CourseChecker.is_equal(self.course_shells[0], self.course_shells[1]) == False
    assert CourseChecker.is_equal(self.course_shells[0], self.course_shells[2]) == False

    # Test for objects of different types
    assert CourseChecker.is_equal(self.courses[0], self.course_shells[0]) == False

class TestStringFilter(TestString):
  """
  Test cases for module string_filter
  """
  pass

  def test_string_filter_space(self):
    pass

  @unittest.skip('too much assumption')
  def test_string_filter_signs(self):
    pass

  @unittest.skip('too much assumption')
  def test_string_filter_redundancy(self):
    pass

class TestCourseFilter(TestCourse):
  """
  Test module course_filter.
  """
  pass

class TestPrereqFilter(unittest.TestCase):
  """
  Test module prereq_filter.
  """
  def setUp(self):
    pass
  
  def tearDown(self):
    pass

# Run all tests by default
if __name__ == '__main__':
  unittest.main()
