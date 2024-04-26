import re

class StringSplitter:
  """
  A class to split a string into a list of strings
  """

  @staticmethod
  def at_index(s: str, index: int) -> list:
    """
    Split string at the specified index and
    return the result array with this character
    """
    return [s[:index + 1], s[index + 1:]]

  @staticmethod
  def at_substring(s: str, substring: str) -> list:
    """
    Split string at the specified substring and
    return the result array without this substring
    """
    return s.split(substring)

  @classmethod
  def at_first_type_occurrence(cls, s: str, split_type: str) -> list:
    """
    Split a string into a list of two members
    at the first occurrence of a character of type split_type
    with split_type can only be either 'letter' or 'number'
    """
    if split_type == 'letter':
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
  def at_last_type_occurrence(cls, s: str, split_type: str) -> list:
    """
    Split a string into a list of two members
    at the last occurrence of a character of type split_type
    with split_type can only be either 'letter' or 'number'
    """
    if split_type == 'letter':
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
  def code_into_subj_id(cls, s: str) -> list:
    """
    Split a string of Course's code into a list of [subject, id]
    """
    arr = cls.at_first_type_occurrence(s, 'number')

    # If the string doesn't contain a number, it is not a Course's code
    if arr[1] is None:
      return [None, None]
    
    return arr

  @classmethod
  def id_into_num_suffix(cls, s: str) -> list:
    """
    Split a string of Course's id into a list of [number, suffix]
    """
    return cls.at_first_type_occurrence(s, 'letter')
