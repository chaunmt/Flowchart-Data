"""
This module contains test cases for class CourseInfoSplitter from module course_info_splitter.
"""

from python_archived.helper.course_info_splitter import CourseInfoSplitter

from python_archived.test.test_setup import TestString, unittest, assert_eq

class TestCourseInfoSplitter(TestString):
    """
    Test cases for class CourseInfoSplitter from module course_info_splitter.
    """

    #############################################################################
    def test_to_subj_num_suf(self):
        """
        Test method to_subj_num_suf of class CourseInfoSplitter.
        """

        assert_eq(
            CourseInfoSplitter.to_subj_num_suf(self.s1),
            [None, None, None]
        )
        assert_eq(
            CourseInfoSplitter.to_subj_num_suf(self.s3),
            [None, None, None]
        )
        assert_eq(
            CourseInfoSplitter.to_subj_num_suf(self.s7),
            [None, None, None]
        )
        assert_eq(
            CourseInfoSplitter.to_subj_num_suf(self.s8),
            [None, None, None]
        )
        assert_eq(
            CourseInfoSplitter.to_subj_num_suf(self.s9),
            ['', '1239', '']
        )
        assert_eq(
            CourseInfoSplitter.to_subj_num_suf(self.s10),
            ['CSCI', '3081', '']
        )
        assert_eq(
            CourseInfoSplitter.to_subj_num_suf(self.s11),
            ['CSCI', '3081', 'W']
        )
        assert_eq(
            CourseInfoSplitter.to_subj_num_suf(self.s12),
            ['CSCI', '3081', 'W']
        )

    #############################################################################
    def test_to_num_suf(self):
        """
        Test method to_num_suf of class CourseInfoSplitter.
        """

        assert_eq(
            CourseInfoSplitter.to_num_suf(self.s5),
            [None, None]
        )
        assert_eq(
            CourseInfoSplitter.to_num_suf(self.s7),
            [None, None]
        )
        assert_eq(
            CourseInfoSplitter.to_num_suf(self.s8),
            [None, None]
        )
        assert_eq(
            CourseInfoSplitter.to_num_suf(self.s9),
            ['1239', '']
        )
        assert_eq(
            CourseInfoSplitter.to_num_suf(self.s10),
            ['3081', '']
        )
        assert_eq(
            CourseInfoSplitter.to_num_suf(self.s11),
            ['3081', 'W']
        )
        assert_eq(
            CourseInfoSplitter.to_num_suf(self.s12),
            ['3081', 'W']
        )
        assert_eq(
            CourseInfoSplitter.to_num_suf(self.s12),
            ['3081', 'W']
        )
