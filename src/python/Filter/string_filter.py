"""
This module contains classes which
filter string component and return the new string.
"""

from python.filter.filter import Filter
from python.helper.string_splitter import StringSplitter

###############################################################################
class StringFilter(Filter):
    """
    This is the base class for all string filter classes.
    """

    allowed_type = str

###############################################################################
class StringFilterSpace(StringFilter):
    """
    This class filter spaces in string.
    """

    def process(self):
        """
        Delete all spaces in string component
        and return the new string.
        """

        return self.item.replace(' ', '')

###############################################################################
class StringFilterSign(StringFilter):
    """
    This class filter signs in string.
    """

    def process(self):
        """
        Replace certain signs with corresponding words
        and return the new string.
        """

        item_ = self.item
        item_ = item_.replace(",", " and ")
        item_ = item_.replace("/", " or ")
        item_ = item_.replace("&", " and ")
        return item_

###############################################################################
class StringFilterBracket(StringFilter):
    """
    This class filter brackets in string.
    """

    def process(self):
        """
        Replace parentheses with square brackets.
        """

        item_ = self.item
        item_ = item_.replace("(", "[")
        item_ = item_.replace(")", "]")
        return item_

###############################################################################
class StringFilterRedundancy(StringFilter):
    """
    This class filter redundancies in string.
    """

    def process(self):
        """
        Delete all redundant substrings
        and return the new string.
        """

        item_ = self.item
        item_ = StringSplitter.at_last_type_occurrence(
            item_, 'number'
        )[0]
        return item_
