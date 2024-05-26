from Test.test_setup import *

class TestCourseChecker(TestCourse):
  """
  Test module course_checker.
  """

  #############################################################################
  def test_is_equal(self):
    # Test for Course type
    assert CourseChecker.is_equal(self.courses[0], self.courses[0]) == True
    assert CourseChecker.is_equal(self.courses[0], self.courses[1]) == False
    assert CourseChecker.is_equal(self.courses[0], self.courses[2]) == False

    # Test for CourseShell type
    assert CourseChecker.is_equal(
      self.course_shells[0], self.course_shells[0]) == True
    assert CourseChecker.is_equal(
      self.course_shells[0], self.course_shells[1]) == False
    assert CourseChecker.is_equal(
      self.course_shells[0], self.course_shells[2]) == False

    # Test for objects of different types
    assert CourseChecker.is_equal(
      self.courses[0], self.course_shells[0]) == False
  
  #############################################################################
  def test_is_writing(self):
    # TODO
    pass
  
  #############################################################################
  def test_is_honors(self):
    # TODO
    pass