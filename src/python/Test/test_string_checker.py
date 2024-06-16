"""
This module contains test cases for class StringChecker from module string_checker.
"""

from python.helper.checker.string_checker import StringChecker

from python.test.test_setup import unittest, TestString

class TestStringChecker(TestString):
    """
    Test cases for class StringChecker from module string_checker.
    """

    #############################################################################
    def test_is_empty(self):
        """
        Test method is_empty of class StringChecker.
        """

        assert StringChecker.is_empty(self.s7) is True
        assert StringChecker.is_empty(self.s13) is True
        assert StringChecker.is_empty(self.s15) is True
        assert StringChecker.is_empty(self.s1) is False

    #############################################################################
    def test_has_number(self):
        """
        Test method has_number of class StringChecker.
        """

        assert StringChecker.has_number(self.s1) is False
        assert StringChecker.has_number(self.s3) is True
        assert StringChecker.has_number(self.s4) is True
        assert StringChecker.has_number(self.s5) is False
        assert StringChecker.has_number(self.s7) is False
        assert StringChecker.has_number(self.s8) is True
        assert StringChecker.has_number(self.s13) is False

    #############################################################################
    def test_has_letter(self):
        """
        Test method has_letter of class StringChecker.
        """

        assert StringChecker.has_letter(self.s2) is True
        assert StringChecker.has_letter(self.s3) is False
        assert StringChecker.has_letter(self.s4) is True
        assert StringChecker.has_letter(self.s5) is True
        assert StringChecker.has_letter(self.s6) is False
        assert StringChecker.has_letter(self.s7) is False
        assert StringChecker.has_letter(self.s13) is False

    #############################################################################
    def test_has_sign(self):
        """
        Test method has_sign of class StringChecker.
        """

        assert StringChecker.has_sign(self.s1) is True
        assert StringChecker.has_sign(self.s4) is True
        assert StringChecker.has_sign(self.s6) is True
        assert StringChecker.has_sign(self.s7) is False
        assert StringChecker.has_sign(self.s8) is False
        assert StringChecker.has_sign(self.s11) is False
        assert StringChecker.has_sign(self.s13) is False

    #############################################################################
    def test_includes(self):
        """
        Test method includes of class StringChecker.
        """

        assert StringChecker.includes(self.s1, 'Hello') is True
        assert StringChecker.includes(self.s3, '123') is False
        assert StringChecker.includes(self.s4, '!0') is True
        assert StringChecker.includes(self.s6, '!@#$%^&*()') is True
        assert StringChecker.includes(self.s6, '!@#$%^&*() ') is False
        assert StringChecker.includes(self.s7, '') is False
        assert StringChecker.includes(self.s8, '') is True
        assert StringChecker.includes(self.s13, '') is False

if __name__ == '__main__':
    unittest.main()
