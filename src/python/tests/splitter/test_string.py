"""
Unit tests for the string manipulation functionality in the StringSplitter class.
This module tests various methods that split strings based on indices, substrings,
and type-based conditions like letters and digits.
"""

import pytest
from ...splitter.string import StringSplitter


class TestStringSplitter:
    """
    This class contains unit tests for the StringSplitter class.
    """

    def test_at_index(self):
        """
        Tests the at_index method of the StringSplitter class.
        """
        assert StringSplitter.at_index("abcdef", 2) == ['abc', 'def']
        assert StringSplitter.at_index("abcdef", 1) == ['ab', 'cdef']
        assert StringSplitter.at_index("abcdef", 0) == ['a', 'bcdef']
        assert StringSplitter.at_index("abcdef", 5) == ['abcdef', '']
        assert StringSplitter.at_index("a", 0) == ['a', '']
        # Any empty input string returns []
        assert StringSplitter.at_index("", 0) == []

        # Test index out of bounds
        with pytest.raises(ValueError) as error:
            assert StringSplitter.at_index("abcdef", 10)

        # Test negative index
        with pytest.raises(ValueError) as error:
            assert StringSplitter.at_index("abcdef", -5)

    def test_at_substring(self):
        """
        Tests the at_substring method of the StringSplitter class.
        """
        assert StringSplitter.at_substring("hello world", " ") == [
            "hello", "world"]
        assert StringSplitter.at_substring("", " ") == []
        assert StringSplitter.at_substring(
            "hello world", "x") == ["hello world"]
        assert StringSplitter.at_substring("apple|banana|cherry", "|") == [
            "apple", "banana", "cherry"]
        assert StringSplitter.at_substring("|apple|banana|", "|") == [
            "", "apple", "banana", ""]
        assert StringSplitter.at_substring(
            "abc--def--ghi", "--") == ['abc', 'def', 'ghi']

    def test_at_first_type_occurrence(self):
        """
        Tests the at_first_type_occurrence method of the StringSplitter class.
        """
        assert StringSplitter.at_first_type_occurrence(
            "123abc456", "letter") == ["123", "abc456"]
        assert StringSplitter.at_first_type_occurrence(
            "abc123def", "number") == ["abc", "123def"]
        assert StringSplitter.at_first_type_occurrence(
            "123456", "letter") == ["123456", None]
        assert StringSplitter.at_first_type_occurrence(
            "abcdef", "number") == ["abcdef", None]
        assert StringSplitter.at_first_type_occurrence("", "letter") == [
            None, None]
        assert StringSplitter.at_first_type_occurrence(
            "123!abc456", "letter") == ["123!", "abc456"]

        # Test invalid split_type (split type can only be number or letter)
        with pytest.raises(ValueError):
            StringSplitter.at_first_type_occurrence("abc123!!", "symbol")

    def test_at_last_type_occurrence(self):
        """
        Tests the at_last_type_occurrence method of the StringSplitter class.
        """
        assert StringSplitter.at_last_type_occurrence(
            "123abc456", "letter") == ["123abc", "456"]
        assert StringSplitter.at_last_type_occurrence(
            "abc123def", "number") == ["abc123", "def"]
        assert StringSplitter.at_last_type_occurrence(
            "123456", "letter") == ["123456", None]
        assert StringSplitter.at_last_type_occurrence(
            "abcdef", "number") == ["abcdef", None]
        assert StringSplitter.at_last_type_occurrence("", "letter") == [
            None, None]
        assert StringSplitter.at_last_type_occurrence(
            "123abc!456", "letter") == ["123abc", "!456"]

        # Test invalid split_type (split type can only be number or letter)
        with pytest.raises(ValueError):
            StringSplitter.at_last_type_occurrence("abc123!!", "symbol")

    def test_to_letter_or_digit_substrs(self):
        """
        Tests the to_letter_or_digit_substrs method of the StringSplitter class.
        """
        assert StringSplitter.to_letter_or_digit_substrs(
            "abc123def456") == ["abc", "123", "def", "456"]
        assert StringSplitter.to_letter_or_digit_substrs("abcdef") == [
            "abcdef"]
        assert StringSplitter.to_letter_or_digit_substrs("123456") == [
            "123456"]
        assert StringSplitter.to_letter_or_digit_substrs("") == []
        assert StringSplitter.to_letter_or_digit_substrs(
            "abc123!@#def456") == ["abc", "123", "def", "456"]
