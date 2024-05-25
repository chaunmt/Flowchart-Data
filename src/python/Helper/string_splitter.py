import re
from Helper.Checker.string_checker import *
from Filter.string_filter import StringFilterSpace
from Filter.filter import *

class StringSplitter:
  """
  A class to split a string into a list of strings.
  """

  @staticmethod
  def at_index(s: str, index: int) -> list:
    """
    Split string at the specified index and
    return the result list with this character.
    """
    return [s[:index + 1], s[index + 1:]]

  @staticmethod
  def at_substring(s: str, substring: str) -> list:
    """
    Split string at the specified substring and
    return the result list without this substring.\n
    Can include empty string member in result list.
    """
    splits = s.split(substring)
    return splits

  @classmethod
  def at_first_type_occurrence(cls, s: str, split_type: str) -> list:
    """
    Split a string into a list of two members
    at the first occurrence of a character of type split_type.\n
    The first string will includes the character at splitted index.\n
    split_type can only be either 'letter' or 'number'.
    """
    if split_type == 'letter':
      match = re.search(r"[A-Za-z]", s)
    elif split_type == 'number':
      match = re.search(r"\d", s)
    else:
      raise ValueError("split_type can only be either 'letter' or 'number'")

    # If no match is found then no split occurs
    if not match:
      return [s, None]

    # Get the index of the first match
    index = match.start() - 1

    # Split the list into two halves at index
    return cls.at_index(s, index)
  
  @classmethod
  def at_last_type_occurrence(cls, s: str, split_type: str) -> list:
    """
    Split a string into a list of two members
    at the last occurrence of a character of type split_type.\n
    The second string will includes the character at splitted index.\n
    split_type can only be either 'letter' or 'number'.
    """
    if split_type == 'letter':
      matches = list(re.finditer(r"[A-Za-z]", s))
    elif split_type == 'number':
      matches = list(re.finditer(r"\d", s))
    else:
      raise ValueError("split_type can only be either 'letter' or 'number'")

    # If no match is found then no split occurs
    if not matches:
      return [s, None]

    # Get the index of the last match
    last_match = matches[-1]  # Index -1 accessed the last element of a list
    index = last_match.start()

    # Split the list into two halves at index
    splits = cls.at_index(s, index)
    if splits[1] == '':
      splits[1] = None

    return splits

  @classmethod
  def code_into_subj_num_suffix(cls, s: str) -> list:
    """
    Split a string of Course's code into a list of [subject, number, suffix].
    """
    # Remove all spaces
    s = StringFilterSpace(s)
    s = s.process()

    if (
      StringChecker.has_signs(s) or   # code does not have sign
      StringChecker.is_empty(s) or    # code can't be empty
      not StringChecker.has_number(s) # code has to have number
    ):
      return [None, None, None]
    
    subject, number = cls.at_first_type_occurrence(s, 'number')

    if StringChecker.is_empty(subject):
      subject = None
    
    number, suffix = cls.separate_number_suffix(number)
    
    return [subject, number, suffix]

  @classmethod
  def separate_number_suffix(cls, s: str) -> list:
    """
    Split a string of Course's number with suffix into a list of [number, suffix].
    """
    # Remove all spaces
    s = StringFilterSpace(s)
    s = s.process()

    if (
      StringChecker.has_signs(s) or   # code does not have sign
      StringChecker.is_empty(s) or    # code can't be empty
      not StringChecker.has_number(s) # code has to have number
    ):
      return [None, None]
    
    number, suffix = cls.at_last_type_occurrence(s, 'number')

    if StringChecker.is_empty(suffix):
      suffix = None

    return [number, suffix]

  @classmethod
  def get_courses(cls, s: str) -> list:
    pass
