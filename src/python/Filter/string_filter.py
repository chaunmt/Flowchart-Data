import re

from Filter.filter import Filter
from Helper.string_splitter import StringSplitter

# Define the return type of these filters
T = str

class StringFilterSpace(Filter):
  """
  Delete all spaces in string component
  and return the new string
  """
  def operation(self, item: T) -> T:
    return item.replace(' ', '')

class StringFilterSigns(Filter):
  """
  Replace certain signs with corresponding words
  and return the new string
  """
  def operation(self, item: T) -> T:
    item = item.replace(", ", " and ")
    item = item.replace("/", " or ")
    item = item.replace("&", " and ")
    return item

class StringFilterRedundancy(Filter):
  """
  Delete all redundant substrings
  and return the new string
  """
  def operation(self, item: T) -> T:
    item = StringSplitter.at_last_type_occurrence(item, 'number')[0]
    return item