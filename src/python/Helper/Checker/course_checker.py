from Helper.new_types import Course, CourseShell

class CourseChecker:
  """
  Perform checks on Course type related object.
  """

  #############################################################################
  @staticmethod
  def is_equal(a: Course | CourseShell, b: Course | CourseShell) -> bool:
    """
    Check whether 2 Course are the same.
    """

    # We can't compared objects of different types
    if not (type(a) == type(b)):
      return False
    
    if not (a.uid == b.uid):
      return False

    return True

  #############################################################################
  @staticmethod
  def is_honor(course_suffix: str) -> bool:
    """
    Check whether a course is an honors course based on its code's suffix.
    """

    if course_suffix == 'H' or course_suffix == 'V':
      return True
    return False
  
  #############################################################################
  @staticmethod
  def is_writing(course_suffix: str) -> bool:
    """
    Check whether a course is a writing course based on its code's suffix.
    """

    if course_suffix == 'W' or course_suffix == 'V':
      return True
    return False