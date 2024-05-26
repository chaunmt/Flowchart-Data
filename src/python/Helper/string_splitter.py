import re
from Helper.Checker.string_checker import *
from Filter.string_filter import StringFilterSpace
from Filter.filter import *
from Converter.prereq_logic_converter import *

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
  def get_course_codes(cls, s: str, target_course_subject: str) -> list:
    """
    Get a list of course's code out of the original string.\n
    Noted: Encoded key's prefix "NESTEDSTR" is treated as a subject, making the complete key a valid course's code.\n
    EX: "Students have to take CSCI 2041 and 2021 or NESTEDSTR0."\n
    ==> [ "CSCI2041", "CSCI2021", "NESTEDSTR0" ]\n
    """
    # The regex pattern to get out acceptable code or partial code
    pattern = (
      '\b[A-Za-z]+\s?\d{2,4}[A-Za-z]*\b'  # Full code pattern (EX: CSCI 3081W)
      + '\b\d{2,4}[A-Za-z]*\b'  # No subject code pattern (EX: 3081W)
      + '\bNESTEDSTR\d+\b'  # Encoded key pattern (EX: NESTEDSTR0)
    )

    # Get the list of matches strings
    course_codes = re.findall(pattern, s)

    # Convert all partial codes into full code format
    course_codes = PrereqLogicConverter.missing_subject_converter(
      course_codes,
      target_course_subject
    )
    
    # Remove all space to follow CourseDog's course code format
    for index, code in enumerate(course_codes):
      course_codes[index] = StringFilterSpace(code).process()
    
    return course_codes

    
    

    
