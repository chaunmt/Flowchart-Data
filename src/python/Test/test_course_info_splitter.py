"""
This module contains test cases for class CourseInfoSplitter from module course_info_splitter.
"""

from python.helper.course_info_splitter import CourseInfoSplitter

from python.test.test_setup import TestString, assert_eq

class TestCourseInfoSplitter(TestString):
    """
    Test cases for class CourseInfoSplitter from module course_info_splitter.
    """

    #############################################################################
    def test_code_into_subj_num_suf(self):
        """
        Test method code_into_subj_num_suf of class CourseInfoSplitter.
        """

        assert_eq(
            CourseInfoSplitter.code_into_subj_num_suf(self.s1),
            [None, None, None]
        )
        assert_eq(
            CourseInfoSplitter.code_into_subj_num_suf(self.s3),
            [None, None, None]
        )
        assert_eq(
            CourseInfoSplitter.code_into_subj_num_suf(self.s7),
            [None, None, None]
        )
        assert_eq(
            CourseInfoSplitter.code_into_subj_num_suf(self.s8),
            [None, '1', None]
        )
        assert_eq(
            CourseInfoSplitter.code_into_subj_num_suf(self.s9),
            [None, '1239WAD12', None]
        )
        assert_eq(
            CourseInfoSplitter.code_into_subj_num_suf(self.s10),
            ['CSCI', '3081', None]
        )
        assert_eq(
            CourseInfoSplitter.code_into_subj_num_suf(self.s11),
            ['CSCI', '3081', 'W']
        )
        assert_eq(
            CourseInfoSplitter.code_into_subj_num_suf(self.s12),
            ['CSCI', '3081', 'W']
        )

    #############################################################################
    def test_separate_num_suf(self):
        """
        Test method separate_num_suf of class CourseInfoSplitter.
        """

        assert_eq(
            CourseInfoSplitter.separate_num_suf(self.s5),
            [None, None]
        )
        assert_eq(
            CourseInfoSplitter.separate_num_suf(self.s7),
            [None, None]
        )
        assert_eq(
            CourseInfoSplitter.separate_num_suf(self.s8),
            ['1', None]
        )
        assert_eq(
            CourseInfoSplitter.separate_num_suf(self.s9),
            ['1239WAD12', None]
        )
        assert_eq(
            CourseInfoSplitter.separate_num_suf(self.s10),
            ['CSCI3081', None]
        )
        assert_eq(
            CourseInfoSplitter.separate_num_suf(self.s11),
            ['CSCI3081', 'W']
        )
        assert_eq(
            CourseInfoSplitter.separate_num_suf(self.s12),
            ['CSCI3081', 'W']
        )
        assert_eq(
            CourseInfoSplitter.separate_num_suf(self.s12),
            ['CSCI3081', 'W']
        )
