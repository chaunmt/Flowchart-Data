import re
from typing import Array

class StringSplitter:
  """
  A class to split a string into an array of strings
  """

  @staticmethod
  def at_index(s: str, index: int) -> list:
    """
    Split string at the specified index and
    return the result array with this character
    """
    return [s[:index + 1], s[index + 1:]]

  @staticmethod
  def at_substring(s: str, substring: str) -> Array[str]:
    """
    Split string at the specified substring and
    return the result array without this substring
    """
    return s.split(substring)

  @classmethod
  def at_first_type_occurrence(cls, s, split_type) -> Array[str]:
    """
    Split a string into an array of two members
    at the first occurrence of a character of type split_type
    with split_type can only be either 'word' or 'num'
    """
    if split_type == 'word':
      match = re.search(r"[A-Za-z]", s)
    else:
      match = re.search(r"\d", s)

    # If no match is found then no split occurs
    if not match:
      return [s, None]

    # Get the index of the first match
    index = match.start()

    # Split the array into two halves at index
    return cls.at_index(s, index)
  
  @classmethod
  def at_last_type_occurrence(cls, s, split_type) -> Array[str]:
    """
    Split a string into an array of two members
    at the last occurrence of a character of type split_type
    with split_type can only be either 'word' or 'num'
    """
    if split_type == 'word':
      matches = list(re.finditer(r"[A-Za-z]", s))
    else:
      matches = list(re.finditer(r"\d", s))

    # If no match is found then no split occurs
    if not matches:
      return [s, None]

    # Get the index of the last match
    last_match = matches[-1]  # Index -1 accessed the last element of a list
    index = last_match.start()

    # Split the array into two halves at index
    return cls.at_index(s, index)

  @classmethod
  def code_into_subj_id(cls, s) -> Array[str]:
    """
    Split a string of Course's code into an array of [subject, id]
    """
    arr = cls.at_first_type_occurrence(s, 'number')

    # If the string doesn't contain a number, it is not a Course's code
    if arr[1] is None:
      return [None, None]
    
    return arr

  @classmethod
  def id_into_num_suffix(cls, s) -> Array[str]:
    """
    Split a string of Course's id into an array of [number, suffix]
    """
    return cls.at_first_type_occurrence(s, 'word')
