import re

from Filter.filter import Filter
import Helper.string_splitter as HelpSplit

class StringFilterSpace(Filter):
  """
  Delete all spaces in string component
  and return the new string.
  """
  allowed_type = str

  def process(self):
    return self.item.replace(' ', '')

class StringFilterSigns(Filter):
  """
  Replace certain signs with corresponding words
  and return the new string.
  """
  allowed_type = str

  def process(self):
    item_ = self.item
    item_ = item_.replace(",", " and ")
    item_ = item_.replace("/", " or ")
    item_ = item_.replace("&", " and ")
    return item_

class StringFilterRedundancy(Filter):
  """
  Delete all redundant substrings
  and return the new string.
  """
  allowed_type = str

  def process(self):
    item_ = self.item
    item_ = HelpSplit.StringSplitter.at_last_type_occurrence(
      item_, 'number'
    )[0]
    return item_