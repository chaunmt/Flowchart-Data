"""
This module contains class StringSplitter which
split a string into a list of strings.
"""

import re

class StringSplitter:
    """
    A class to split a string into a list of strings.
    """

    #############################################################################
    @staticmethod
    def at_index(s: str, index: int) -> list:
        """
        Split string at the specified index and
        return the result list with this character.
        """

        # Error handlers
        if not s:
            return []
        
        if index < 0 or index >= len(s):
            raise ValueError("Index out of bounds")
        
        # Split the list into two halves at index
        splits = [s[:index + 1], s[index + 1:]]
        
        if splits[1] == '':  # If the second string is empty
            splits.pop()  # Remove the empty string
        
        return splits

    #############################################################################
    @staticmethod
    def at_substring(s: str, substring: str) -> list:
        """
        Split string at the specified substring and
        return the result list without this substring.\n
        Can include empty string member in result list.
        """

        if not s:
            return []

        splits = s.split(substring)
        return splits

    #############################################################################
    @classmethod
    def at_first_type_occurrence(cls, s: str, split_type: str) -> list:
        """
        Split a string into a list of two members
        at the first occurrence of a character of type split_type.\n
        The first string will includes the character at splitted index.\n
        split_type can only be either 'letter' or 'number'.
        """

        if not s:
            return [None, None]

        if split_type == 'letter':
            match = re.search(r"[A-Za-z]", s)
        elif split_type == 'number':
            match = re.search(r"\d", s)
        else:
            raise ValueError("split_type can only be either 'letter' or 'number'")

        # If no match is found then no split occurs
        if not match:
            return [s, None]

        # Get the index of the first match
        index = match.start() - 1

        # Split the list into two halves at index
        return cls.at_index(s, index)

    #############################################################################
    @classmethod
    def at_last_type_occurrence(cls, s: str, split_type: str) -> list:
        """
        Split a string into a list of two members
        at the last occurrence of a character of type split_type.\n
        The second string will includes the character at splitted index.\n
        split_type can only be either 'letter' or 'number'.
        """

        if not s:
            return [None, None]

        if split_type == 'letter':
            matches = list(re.finditer(r"[A-Za-z]", s))
        elif split_type == 'number':
            matches = list(re.finditer(r"\d", s))
        else:
            raise ValueError("split_type can only be either 'letter' or 'number'")

        # If no match is found then no split occurs
        if not matches:
            return [s, None]

        # Get the index of the last match
        last_match = matches[-1]  # Index -1 accessed the last element of a list
        index = last_match.start()

        # Split the list into two halves at index
        splits = cls.at_index(s, index)
        if splits[1] == '':
            splits[1] = None

        return splits

    #############################################################################
    @staticmethod
    def to_letter_or_digit_substrs(s: str) -> list:
        """
        Split a string into a list of substrings
        contain either only letter or only digit character.
        """

        if not s:
            return []

        substrings = re.findall(r'[a-zA-Z]+|\d+', s)
        return substrings
