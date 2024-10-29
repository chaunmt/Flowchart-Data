"""
This module contains tests for string's checkers.
"""

import pytest
from ...checker.string import StringChecker


class TestStringChecker:
    """
    This class contains tests for the StringChecker class.
    """

    def test_is_empty(self):
        """
        This method contains tests for the is_empty method.
        """
        assert StringChecker.is_empty("") is True, (
            "Empty string is 'empty'"
        )
        assert StringChecker.is_empty("   ") is True, (
            "Whitespace-only string is 'empty'"
        )
        assert StringChecker.is_empty(None) is True, (
            "None is 'empty'"
        )
        assert StringChecker.is_empty("hello") is False, (
            "Non-empty string is 'not empty'"
        )

    def test_has_number(self):
        """
        This method contains tests for the has_number method.
        """
        assert StringChecker.has_number("123") is True, (
            "String with numbers returns True"
        )
        assert StringChecker.has_number("hello123") is True, (
            "Mixed string with numbers returns True"
        )
        assert StringChecker.has_number("hello") is False, (
            "String with no numbers returns False"
        )
        assert StringChecker.has_number("") is False, (
            "Empty string returns False"
        )
        assert StringChecker.has_number("   ") is False, (
            "Whitespace-only string returns False"
        )
        assert StringChecker.has_number(None) is False, (
            "None returns False"
        )
        assert StringChecker.has_number("!@#") is False, (
            "String with only signs returns False"
        )

    def test_has_letter(self):
        """
        This method contains tests for the has_letter method.
        """
        assert StringChecker.has_letter("hello") is True, (
            "String with letters returns True"
        )
        assert StringChecker.has_letter("123hello") is True, (
            "Mixed string with letters returns True"
        )
        assert StringChecker.has_letter("123") is False, (
            "String with no letters returns False"
        )
        assert StringChecker.has_letter("") is False, (
            "Empty string returns False"
        )
        assert StringChecker.has_letter("   ") is False, (
            "Whitespace-only string returns False"
        )
        assert StringChecker.has_letter(None) is False, (
            "None returns False"
        )
        assert StringChecker.has_letter("!@#") is False, (
            "String with only signs returns False"
        )

    def test_has_sign(self):
        """
        This method contains tests for the has_sign method.
        """
        assert StringChecker.has_sign("hello@") is True, (
            "String with special character returns True"
        )
        assert StringChecker.has_sign("!@#") is True, (
            "String with only signs returns True"
        )
        assert StringChecker.has_sign("hello") is False, (
            "String with no signs returns False"
        )
        assert StringChecker.has_sign("123") is False, (
            "String with only numbers returns False"
        )
        assert StringChecker.has_sign("") is False, (
            "Empty string returns False"
        )
        assert StringChecker.has_sign("   ") is False, (
            "Whitespace-only string returns False"
        )
        assert StringChecker.has_sign(None) is False, (
            "None returns False"
        )

    def test_includes(self):
        """
        This method contains tests for the includes method.
        """
        assert StringChecker.includes("hello world", "world") is True, (
            "Substring is found in string"
        )
        assert StringChecker.includes("hello world", "WORLD") is False, (
            "Case-sensitive makes it a different substring"
        )
        assert StringChecker.includes("hello", "") is True, (
            "Empty substring is always included"
        )
        assert StringChecker.includes("", "world") is False, (
            "Empty string does not contain any substring"
        )
        assert StringChecker.includes("   ", " ") is True, (
            "Whitespace-only string includes space substring"
        )
        assert StringChecker.includes(None, "world") is False, (
            "None does not contain any substring"
        )
        assert StringChecker.includes("!@#", "@") is True, (
            "String with only signs includes sign substring"
        )
