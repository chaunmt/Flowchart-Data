import re

from Filter.filter import Filter
import Helper.string_splitter as HelpSplit

class StringFilter(Filter):
  allowed_type = str

class StringFilterSpace(StringFilter):
  def process(self):
    """
    Delete all spaces in string component
    and return the new string.
    """
    return self.item.replace(' ', '')

class StringFilterSigns(StringFilter):
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

class StringFilterBrackets(StringFilter):
  def process(self):
    """
    Replace parentheses with square brackets.
    """
    item_ = self.item
    item_ = item_.replace("(", "[")
    item_ = item_.replace(")", "]")
    return item_

class StringFilterRedundancy(StringFilter):
  def process(self):
    """
    Delete all redundant substrings
    and return the new string.
    """
    item_ = self.item
    item_ = HelpSplit.StringSplitter.at_last_type_occurrence(
      item_, 'number'
    )[0]
    return item_