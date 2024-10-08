"""
This module contains classes which filter string component.
"""

import re

from python.schema.others import StringComponent

###############################################################################
class StringFilter(StringComponent):
    """
    This is the base class for all string filter classes.
    """

    _s : StringComponent = None

    def __init__(self, s: str) -> None:
        self._s = s

    @property
    def prereq(self) -> StringComponent:
        return self._s

    def process(self) -> str:
        return self._s.process()

###############################################################################
class StringFilterSpace(StringFilter):
    """
    This class filter out all spaces in string.
    """

    def process(self):
        """
        Delete all spaces in string component
        and return the new string.
        """

        return self._s.process().replace(' ', '')

###############################################################################
class StringFilterSign(StringFilter):
    """
    This class filter out all signs in string.
    """

    def process(self):
        """
        Delete all signs (excluding space) in string component
        and return the new string.
        """

        return re.sub(r'[^a-zA-Z0-9]', '', self._s.process())

###############################################################################
class StringFilterBracket(StringFilter):
    """
    This class filter out all brackets in string.
    """

    def process(self):
        """
        Delete all brackets (round, square, and curly) in string component
        and return the new string.
        """

        return re.sub(r'[()\[\]{}]', '', self._s.process())

###############################################################################
class StringFilterAlpha(StringFilter):
    """
    This class filter all letters in string.
    """

    def process(self):
        """
        Delete all letters in string component
        and return the new string.
        """

        return re.sub(r'[A-Za-z]', '', self._s.process())

###############################################################################
class StringFilterNumeric(StringFilter):
    """
    This class filter all digits in string.
    """

    def process(self):
        """
        Delete all digits in string component
        and return the new string.
        """

        return re.sub(r'\d', '', self._s.process())
