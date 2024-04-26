from Filter.filter import Filter
from Helper.new_types import *

# Define the return type of these filters
T = PrereqList

class PrereqFilter(Filter):
  """
  Filter the prereq component and return its new result
  """

  # def operation(self, item: T) -> T:
  #   return f"PrereqFilter({self.component.operation()})"