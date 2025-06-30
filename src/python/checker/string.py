"""
This module contains class StringChecker which perform checks on String type object.
"""

class StringChecker:
    
    @staticmethod
    def is_empty(s: str) -> bool:
        return s and not s.strip()

    @staticmethod
    def has_number(s: str) -> bool:
        return s and any(char.isdigit() for char in s)

    @staticmethod
    def has_letter(s: str) -> bool:
        return s and any(char.isalpha() for char in s)

    @staticmethod
    def has_sign(s: str) -> bool:
        return s and any(
            not char.isalnum() and
            not char.isspace() for char in s
        )

    @staticmethod
    def includes(s: str, substring: str) -> bool:
        return s and substring in s
