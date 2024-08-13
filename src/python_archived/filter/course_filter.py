"""
This module contains CourseFilter which
filter the course component and return its new result.
"""

from python_archived.filter.filter import Filter
from python_archived.helper.new_types import Course, CourseShell

###############################################################################
class CourseFilter(Filter):
    """
    Filter the course component and return its new result.
    """

    allowed_type = Course
