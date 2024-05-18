from Filter.filter import Filter
from Helper.new_types import *

class PrereqFilter(Filter):
  """
  Filter the prereq component and return its new result.
  """
  allowed_type = PrereqList
