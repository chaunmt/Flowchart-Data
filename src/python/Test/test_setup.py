"""
This file contains the setup for all testcases of this project.\n
  - def setUp(self) is automatically called
    before any test of its class is run.
  - def tearDown(self) is automatically called
    after any test of its class is run.
"""
import unittest

from Helper.new_types import *
from Helper.string_splitter import *
from Helper.course_info_splitter import *
from Helper.json_handler import *

from Helper.Checker.string_checker import *
from Helper.Checker.course_checker import *

from Filter.filter import *
from Filter.string_filter import *
from Filter.course_filter import *
from Filter.prereq_filter import *

from Converter.nested_course_converter import *
from Converter.prereq_logic_converter import *

###############################################################################
# Helper functions for all unit tests.

#######################################
def merge_lists(list1, list2):
  """
  Merge members at the same index of 2 lists together.
  """
  
  merged_list = []
  for first, second in zip(list1, list2):
    merged_list.append({**first, **second})

  return merged_list

#######################################
def assert_eq(result, goal):
  """
  Assert whether result equals goal.\n
  If not, print out the unwanted result.
  """

  assert result == goal, f"Unwanted result: {result}"

###############################################################################
# Parent classes to setup and teardown its children test classes.

#######################################
class TestString(unittest.TestCase):
  """
  Parent class for all string tests.
  """

  def setUp(self):
    self.s1 = 'Hello, world!'
    self.s2 = 'Python  is   fun!'
    self.s3 = '12!3 !4.5'
    self.s4 = 'C?S1!0^1@'
    self.s5 = 'This ! is ? a ^ test.'
    self.s6 = '!@#$%^&*()'
    self.s7 = ''
    self.s8 = '   1   '
    self.s9 = '1239WAD12'
    self.s10 = 'CSCI 3081'
    self.s11 = 'CSCI 3081W'
    self.s12 = 'CSCI3081W'
    self.s13 = None
    self.s14 = 'CSCI 4041/3081,3081W/2041&2021'
    
  def tearDown(self):
    pass

#######################################
class TestCourse(unittest.TestCase):
  """
  Parent class for all course tests.
  """

  def setUp(self):
    self.course_shell_data = [
      {
        'uid_': '1',
        'code_': 'CSC101',
        'subject_': 'CSC',
        'number_': 101,
        'honors_': False
      },
      {
        'uid_': '2',
        'code_': 'CSC101',
        'subject_': 'CSC',
        'number_': 101,
        'honors_': False
      },
      {
        'uid_': '3',
        'code_': 'CSC102V',
        'subject_': 'CSC',
        'number_': 102,
        'honors_': True
      }
    ]

    self.additional_data = [
      {
        'writingIntensive_': False,
        'name_': 'Introduction to ComSci',
        'fullname_': 'Introduction to Computer Science',
        'info_': (
          'Introductory course coveringbasic concepts in computer science.'
        ),
        'prereq_': None
      },
      {
        'writingIntensive_': False,
        'name_': 'Introduction to ComSci',
        'fullname_': 'Introduction to Computer Science',
        'info_': (
          'Introductory course covering basic concepts in computer science.'
        ),
        'prereq_': None
      },
      {
        'writingIntensive_': True,
        'name_': 'Data Structures',
        'fullname_': 'Data Structures and Algorithms',
        'info_': (
          'A course focusing on data structures and algorithms.'
        ),
        'prereq_': None
      }
    ]

    # Merge course_shell_data with additional attributes for each course
    self.course_data = merge_lists(
      self.course_shell_data,
      self.additional_data
    )

    # Initialize CourseShell objects
    self.course_shells = [
      CourseShell(**data)
      for data in self.course_shell_data
    ]

    # Initialize Course objects
    self.courses = [
      Course(**data)
      for data in self.course_data
    ]

  def tearDown(self):
    pass

#######################################
class TestPrereq(TestCourse):
  """
  Parent class for all prereq tests.
  """

  def setUp(self):
    TestCourse.setUp(self)
    self.p1 = PrereqFormat(self.course_shells[0])
    self.p2 = PrereqFormat(self.course_shells)
    self.p3 = PrereqFormat({'and' : self.course_shells})
    self.p3 = PrereqFormat({'and' : { self.course_shells[0] } })

  def tearDown(self):
    TestCourse.tearDown(self)

#######################################
class TestFilter(unittest.TestCase):
  """
  Parent class for all filter tests.
  """

  # Class Filter is tested with its children classes
  pass