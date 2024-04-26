import unittest
from Helper.new_types import *

class TestNewTypes(unittest.TestCase):
  def test_course_shell(self):
    pass

  def test_course(self):
    pass

  def test_prereq_courses(self):
    pass

  def test_prereq_list(self):
    pass

class TestStringSplitter(unittest.TestCase):
  def test_at_index(self):
    pass

  def test_at_substring(self):
    pass

  def test_at_first_type_occurrence(self):
    pass

  def test_at_last_type_occurrence(self):
    pass

  def test_code_into_subj_id(self):
    pass

  def test_id_into_num_suffix(self):
    pass

class TestStringChecker(unittest.TestCase):
  def test_has_number(self):
    pass

  def test_has_word(self):
    pass

  def test_includes(self):
    pass

class TestCourseChecker(unittest.TestCase):
  def test_is_equal(self):
    pass

class TestFilter(unittest.TestCase):
  pass

class TestStringFilter(unittest.TestCase):
  def test_string_filter_space(self):
    pass

  @unittest.skip('too much assumption')
  def test_string_filter_signs(self):
    pass

  @unittest.skip('too much assumption')
  def test_string_filter_redundancy(self):
    pass

class TestCourseFilter(unittest.TestCase):
  pass

class TestPrereqFilter(unittest.TestCase):
  pass

if __name__ == '__main__':
  unittest.main()