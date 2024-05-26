from Helper.string_splitter import *
from Helper.Checker.course_checker import *

class PrereqLogicConverter:
  """
  Converters dedicated to implement logic into our prerequisites.
  """

  #############################################################################
  @classmethod
  def logical_operation_converter(
      cls,
      s: str,
      target_course_subject: str
    ) -> list:
    """
    """

    pass
  
  #############################################################################
  @staticmethod
  def replace_empty_subj(
    subjects: list,
    replacement: str,
    get_closest_replacement: bool
  ) -> list:
    """
    This method replace all empty subject in a list with a replacement subject.\n
    If 'get_closest_replacement' is true,
    'replacement' will be replaced with the closest previous non-empty subject.
    """

    for index, subject in enumerate(subjects):
      if subject == '':
        subjects[index] = replacement
      elif get_closest_replacement:
        replacement = subject
    
    return subjects

  #############################################################################
  @classmethod
  def missing_subject_converter(
      cls,
      course_codes: list,
      target_course_subject: str
    ) -> list:
    """
    Convert all missing subject course's code into the closest related subject.
    """
    
    # Get course's subject and number with suffix from course's code
    course_subjects = []
    course_numsufs = []
    for code in course_codes:
      subj, num, suf = StringSplitter.code_into_subj_num_suf(code)
      course_subjects.append(subj)
      course_numsufs.append(num + suf)
    
    # Replace all empty subject with previous code's subject
    course_subjects = cls.replace_empty_subj(
      course_subjects,
      '',
      True
    )

    # If there is no previous code's subject, replace with subsequent subject
    course_subjects = cls.replace_empty_subj(
      reversed(course_subjects),
      '',
      True
    )

    # If all subjects are empty, replace them with target course's subject
    course_subjects = cls.replace_empty_subj(
      course_subjects,
      target_course_subject,
      False
    )

    # Replace partial code with full valid code
    new_course_codes = []
    for index, subj in course_subjects:
      # Skip code with invalid subject code
      if CourseChecker.is_valid_subj(subj):
        new_course_codes.append(
          subj + course_numsufs[index]
        )
    
    return new_course_codes