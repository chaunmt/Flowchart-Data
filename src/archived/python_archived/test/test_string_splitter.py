"""
This module contains test cases for class StringSplitter from module string_splitter.
"""

from python_archived.helper.string_splitter import StringSplitter

from python_archived.test.test_setup import unittest, TestString, assert_eq

class TestStringSplitter(TestString):
    """
    Test cases for class StringSplitter from module string_splitter.
    """

    #############################################################################
    def test_at_index(self):
        """
        Test method at_index of class StringSplitter.
        """

        assert_eq(
            StringSplitter.at_index(self.s1, 5),
            ['Hello,', ' world!']
        )
        assert_eq(
            StringSplitter.at_index(self.s1, 7),
            ['Hello, w', 'orld!']
        )
        assert_eq(
            StringSplitter.at_index(self.s2, 11),
            ['Python  is  ', ' fun!']
        )
        assert_eq(
            StringSplitter.at_index(self.s3, 3),
            ['12!3', ' !4.5']
        )
        assert_eq(
            StringSplitter.at_index(self.s3, 5),
            ['12!3 !', '4.5']
        )
        assert_eq(
            StringSplitter.at_index(self.s6, 3),
            ['!@#$', '%^&*()']
        )
        assert_eq(
            StringSplitter.at_index(self.s6, 15),
            ['!@#$%^&*()', '']
        )
        assert_eq(
            StringSplitter.at_index(self.s13, 2),
            []
        )


    #############################################################################
    def test_at_substring(self):
        """
        Test method at_substring of class StringSplitter.
        """

        assert_eq(
            StringSplitter.at_substring(self.s1, 'Hello'),
            ['', ', world!']
        )
        assert_eq(
            StringSplitter.at_substring(self.s1, ','),
            ['Hello', ' world!']
        )
        assert_eq(
            StringSplitter.at_substring(self.s1, 'world'),
            ['Hello, ', '!']
        )
        assert_eq(
            StringSplitter.at_substring(self.s2, ' '),
            ['Python', '', 'is', '', '', 'fun!']
        )
        assert_eq(
            StringSplitter.at_substring(self.s2, '  '),
            ['Python', 'is', ' fun!']
        )
        assert_eq(
            StringSplitter.at_substring(self.s3, '!'),
            ['12', '3 ', '4.5']
        )
        assert_eq(
            StringSplitter.at_substring(self.s3, '12!'),
            ['', '3 !4.5']
        )
        assert_eq(
            StringSplitter.at_substring(self.s4, '?S1'),
            ['C', '!0^1@']
        )
        assert_eq(
            StringSplitter.at_substring(self.s5, '^'),
            ['This ! is ? a ', ' test.']
        )
        assert_eq(
            StringSplitter.at_substring(self.s6, '*'),
            ['!@#$%^&', '()']
        )
        assert_eq(
            StringSplitter.at_substring(self.s13, 'number'),
            []
        )

    #############################################################################
    def test_at_first_type_occurrence(self):
        """
        Test method at_first_type_occurrence of class StringSplitter.
        """

        # Test wrong split_type
        self.assertRaises(
            ValueError,
            StringSplitter.at_first_type_occurrence, self.s1, 'word'
        )

        # Test splitting at the first letter occurrence
        assert_eq(
            StringSplitter.at_first_type_occurrence(self.s1, 'letter'),
            ['', 'Hello, world!']
        )
        assert_eq(
            StringSplitter.at_first_type_occurrence(self.s3, 'letter'),
            ['12!3 !4.5', None]
        )
        assert_eq(
            StringSplitter.at_first_type_occurrence(self.s4, 'letter'),
            ['', 'C?S1!0^1@']
        )

        # Test splitting at the first number occurrence
        assert_eq(
            StringSplitter.at_first_type_occurrence(self.s3, 'number'),
            ['', '12!3 !4.5']
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
            ['C?S', '1!0^1@']
        )
        assert_eq(
            StringSplitter.at_first_type_occurrence(self.s13, 'number'),
            [None, None]
        )

    #############################################################################
    def test_at_last_type_occurrence(self):
        """
        Test method at_last_type_occurrence of class StringSplitter.
        """

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
        assert_eq(
            StringSplitter.at_last_type_occurrence(self.s13, 'number'),
            [None, None]
        )

    #############################################################################
    def test_letter_and_num(self):
        """
        Test method letter_and_num of class StringSplitter.
        """

        assert_eq(
            StringSplitter.letter_and_num(self.s1),
            ['Hello', 'world']
        )
        assert_eq(
            StringSplitter.letter_and_num(self.s3),
            ['12', '3', '4', '5']
        )
        assert_eq(
            StringSplitter.letter_and_num(self.s6),
            []
        )
        assert_eq(
            StringSplitter.letter_and_num(self.s13),
            []
        )
