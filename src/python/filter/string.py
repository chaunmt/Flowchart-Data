"""
This module contains classes which
filter string component and return the new string.
"""

import re

from python.filter.filter import Filter
from python.splitter.string import StringSplitter

###############################################################################
class StringFilter(Filter):
    """
    This is the base class for all string filter classes.
    """

    allowed_type = str

###############################################################################
class StringFilterSpace(StringFilter):
    """
    This class filter out all spaces in string.
    """

    def filter(cls):
        """
        Delete all spaces in string component
        and return the new string.
        """

        return cls.item.replace(' ', '')

###############################################################################
class StringFilterSign(StringFilter):
    """
    This class filter out all signs in string.
    """

    def filter(cls):
        """
        Delete all signs (excluding space) in string component
        and return the new string.
        """

        return re.sub(r'[^a-zA-Z0-9]', '', cls.item)

###############################################################################
class StringFilterBracket(StringFilter):
    """
    This class filter out all brackets in string.
    """

    def filter(cls):
        """
        Delete all brackets (round, square, and curly) in string component
        and return the new string.
        """

        return re.sub(r'[()\[\]{}]', '', cls.item)

###############################################################################
class StringFilterAlpha(StringFilter):
    """
    This class filter all letters in string.
    """

    def filter(cls):
        """
        Delete all letters in string component
        and return the new string.
        """

        return re.sub(r'[A-Za-z]', '', cls.item)

###############################################################################
class StringFilterNumeric(StringFilter):
    """
    This class filter all digits in string.
    """

    def filter(cls):
        """
        Delete all digits in string component
        and return the new string.
        """

        return re.sub(r'\d', '', cls.item)
