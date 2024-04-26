from Helper.new_types import Course, CourseShell

class CourseChecker:
  """
  Perform checks on Course type object.
  """
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