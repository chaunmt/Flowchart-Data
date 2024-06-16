"""
This module contains test cases for class CourseChecker of module course_checker.
"""

from python.helper.checker.course_checker import CourseChecker

from python.test.test_setup import TestCourse, unittest

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

        assert CourseChecker.is_writing('W') is True
        assert CourseChecker.is_writing('V') is True
        assert CourseChecker.is_writing('') is False
        assert CourseChecker.is_writing('H') is False
        assert CourseChecker.is_writing(' ') is False
        assert CourseChecker.is_writing('3081W') is False

    #############################################################################
    def test_is_honors(self):
        """
        Test method is_honors of class CourseChecker.
        """

        assert CourseChecker.is_honors('V') is True
        assert CourseChecker.is_honors('H') is True
        assert CourseChecker.is_honors('') is False
        assert CourseChecker.is_honors('W') is False
        assert CourseChecker.is_honors(' ') is False
        assert CourseChecker.is_honors('1933H') is False

    #############################################################################
    def test_is_valid_subj(self):
        """
        Test method is_valid_subj of class CourseChecker.
        """

        assert CourseChecker.is_valid_subj('MATH') is True
        assert CourseChecker.is_valid_subj('PE') is True
        assert CourseChecker.is_valid_subj('LITR') is False
        assert CourseChecker.is_valid_subj('') is False
        assert CourseChecker.is_valid_subj(' ') is False

    #############################################################################
    def test_is_valid_num(self):
        """
        Test method is_valid_num of class CourseChecker.
        """

        assert CourseChecker.is_valid_num('1933') is True
        assert CourseChecker.is_valid_num('01933') is True
        assert CourseChecker.is_valid_num('193') is False
        assert CourseChecker.is_valid_num('0933') is False
        assert CourseChecker.is_valid_num('19333') is False

    #############################################################################
    def test_is_valid_suf(self):
        """
        Test method is_valid_suf of class CourseChecker.
        """

        assert CourseChecker.is_valid_suf('') is True
        assert CourseChecker.is_valid_suf('W') is True
        assert CourseChecker.is_valid_suf('H') is True
        assert CourseChecker.is_valid_suf('V') is True
        assert CourseChecker.is_valid_suf(' ') is False
        assert CourseChecker.is_valid_suf('A') is False
        assert CourseChecker.is_valid_suf('WW') is False

if __name__ == '__main__':
    unittest.main()
