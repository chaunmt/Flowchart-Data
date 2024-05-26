from Filter.filter import Filter
from Helper.new_types import Course, CourseShell

###############################################################################
class CourseFilter(Filter):
  """
  Filter the course component and return its new result.
  """
  
  allowed_type = Course
