import re

from Filter.filter import Filter
import Helper.string_splitter as HelpSplit

class StringFilter(Filter):
  allowed_type = str

class StringFilterSpace(StringFilter):
  """
  Delete all spaces in string component
  and return the new string.
  """

  def process(self):
    return self.item.replace(' ', '')

class StringFilterSigns(StringFilter):
  """
  Replace certain signs with corresponding words
  and return the new string.
  """

  def process(self):
    item_ = self.item
    item_ = item_.replace(",", " and ")
    item_ = item_.replace("/", " or ")
    item_ = item_.replace("&", " and ")
    return item_

class StringFilterRedundancy(StringFilter):
  """
  Delete all redundant substrings
  and return the new string.
  """

  def process(self):
    item_ = self.item
    item_ = HelpSplit.StringSplitter.at_last_type_occurrence(
      item_, 'number'
    )[0]
    return item_