from Helper.new_types import Course, CourseShell

class CourseChecker:
  """
  A class to perform checks on Course type object
  """
  @staticmethod
  def is_equal(a: Course, b: Course) -> bool:
    """
    Check whether 2 Course are the same
    """
    if not (
      a.code == b.code and
      a.subject == b.subject and
      a.id == b.id
      ):
      return False

    return True

  @staticmethod
  def is_equal(a: CourseShell, b: CourseShell) -> bool:
    """
    Check whether 2 CourseShell are the same
    """
    if not (
      a.code == b.code and
      a.subject == b.subject and
      a.id == b.id
      ):
      return False

    return True