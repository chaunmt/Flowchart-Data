"""
This module contains classes which
filter string component and return the new string.
"""

import re

from python_archived.filter.filter import Filter
from python_archived.helper.string_splitter import StringSplitter

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
        Delete all signs (including space) in string component
        and return the new string.
        """

        return re.sub(r'[^a-zA-Z0-9]', '', self.item)

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

###############################################################################
class StringFilterBracket(StringFilter):
    """
    """
    # TODO
