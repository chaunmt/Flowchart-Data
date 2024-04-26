from Filter.filter import Filter
from Helper.new_types import Course, CourseShell

# Define the return type of these filters
T = Course

class CourseFilter(Filter):
  """
  Filter the course component and return its new result
  """

  # def operation(self, item: T) -> T:
  #   return f"CourseFilter({self.component.operation()})"