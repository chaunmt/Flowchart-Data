from Helper.string_splitter import *
from Helper.Checker.string_checker import *
from Converter.prereq_logic_converter import *
from Filter.string_filter import *

class CourseStringSplitter:
  """
  A class to split a course's info string into a list of strings.
  """
  
  #############################################################################
  @staticmethod
  def code_into_subj_num_suf(s: str) -> list:
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
    
    subject, number = StringSplitter.at_first_type_occurrence(s, 'number')

    if StringChecker.is_empty(subject):
      subject = None
    
    number, suffix = StringSplitter.separate_number_suffix(number)
    
    return [subject, number, suffix]

  #############################################################################
  @staticmethod
  def separate_number_suffix(s: str) -> list:
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
    
    number, suffix = StringSplitter.at_last_type_occurrence(s, 'number')

    if StringChecker.is_empty(suffix):
      suffix = None

    return [number, suffix]

  #############################################################################
  @staticmethod
  def get_course_codes(s: str, target_course_subject: str) -> list:
    """
    Get a list of course's code out of the original string.\n
    Noted: Encoded key's prefix "NESTEDSTR" is treated as a subject,
    making the complete key a valid course's code.\n
    
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
