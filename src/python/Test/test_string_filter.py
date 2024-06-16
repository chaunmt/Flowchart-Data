"""
This module contains test cases for all classes from module string_filter.
"""

from python.filter.string_filter import (
    StringFilter,
    StringFilterSpace,
    StringFilterSign,
    StringFilterRedundancy
)

from python.test.test_setup import unittest, TestString, assert_eq

class TestStringFilter(TestString):
    """
    Test cases for all classes from module string_filter.
    """

    def test_string_filter(self):
        """
        Test class StringFilter from module string_filter.
        """

        # Test for disallowed type
        self.assertRaises(
            TypeError,
            StringFilter, 12
        )
        self.assertRaises(
            TypeError,
            StringFilter, None
        )

    #############################################################################
    def test_string_filter_space(self):
        """
        Test class StringFilterSpace from module string_filter.
        """

        # Test for allowed type
        assert_eq(
            StringFilterSpace(self.s1).process(),
            'Hello,world!'
        )
        assert_eq(
            StringFilterSpace(self.s2).process(),
            'Pythonisfun!'
        )
        assert_eq(
            StringFilterSpace(self.s7).process(),
            ''
        )
        assert_eq(
            StringFilterSpace(self.s8).process(),
            '1'
        )
        assert_eq(
            StringFilterSpace(self.s9).process(),
            '1239WAD12'
        )

    #############################################################################
    def test_string_filter_sign(self):
        """
        Test class StringFilterSign from module string_filter.
        """

        # Test for allowed type
        assert_eq(
            StringFilterSign(self.s2).process(),
            'Pythonisfun'
        )
        assert_eq(
            StringFilterSign(self.s6).process(),
            ''
        )
        assert_eq(
            StringFilterSign(self.s11).process(),
            'CSCI3081W'
        )


    #############################################################################
    def test_string_filter_redundancy(self):
        """
        Test class StringFilterRedundancy from module string_filter.
        """

        # Test for allowed type
        assert_eq(
            StringFilterRedundancy(self.s2).process(),
            'Python  is   fun!'
        )
        assert_eq(
            StringFilterRedundancy(self.s3).process(),
            '12!3 !4.5'
        )
        assert_eq(
            StringFilterRedundancy(self.s4).process(),
            'C?S1!0^1'
        )
        assert_eq(
            StringFilterRedundancy(self.s7).process(),
            ''
        )
        assert_eq(
            StringFilterRedundancy(self.s8).process(),
            '   1'
        )

if __name__ == '__main__':
    unittest.main()
