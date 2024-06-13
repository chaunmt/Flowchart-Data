"""
This module contains test cases for class CourseChecker of module course_checker.
"""

from python.helper.checker.course_checker import CourseChecker

from python.test.test_setup import TestCourse

class TestCourseChecker(TestCourse):
    """
    Test cases for class CourseChecker of module course_checker.
    """

    #############################################################################
    def test_is_equal(self):
        """
        Test method is_equal of class CourseChecker.
        """

        # Test for Course type
        assert CourseChecker.is_equal(self.courses[0], self.courses[0]) is True
        assert CourseChecker.is_equal(self.courses[0], self.courses[1]) is False
        assert CourseChecker.is_equal(self.courses[0], self.courses[2]) is False

        # Test for CourseShell type
        assert CourseChecker.is_equal(
        self.course_shells[0], self.course_shells[0]) is True
        assert CourseChecker.is_equal(
        self.course_shells[0], self.course_shells[1]) is False
        assert CourseChecker.is_equal(
        self.course_shells[0], self.course_shells[2]) is False

        # Test for objects of different types
        assert CourseChecker.is_equal(
        self.courses[0], self.course_shells[0]) is False

    #############################################################################
    def test_is_writing(self):
        """
        Test method is_writing of class CourseChecker.
        """

        # TODO
        pass

    #############################################################################
    def test_is_honors(self):
        """
        Test method is_honors of class CourseChecker.
        """

        # TODO
        pass

    #############################################################################
    def test_is_valid_subj(self):
        """
        Test method is_valid_subj of class CourseChecker.
        """

        # TODO
        pass
