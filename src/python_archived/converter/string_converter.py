"""
This module contains class StringConverter which contains
converters dedicated to alter string type object.
"""

class StringConverter:
    """
    Converter dedicated to transform string type objects.
    """

    @staticmethod
    def sign_to_letter_op(s: str) -> str:
        """
        Replace certain signs with corresponding words
        and return the new string.
        """

        s = s.replace(",", " and ")
        s = s.replace("/", " or ")
        s = s.replace("&", " and ")
        return s

    @staticmethod
    def paren_to_square_bracket(s: str) -> str:
        """
        Replace parentheses with square brackets.
        """

        s = s.replace("(", "[")
        s = s.replace(")", "]")
        return s
