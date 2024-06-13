"""
This module contains class PrereqFilter which
filter the prereq component and return its new result.
"""

from python.filter.filter import Filter
from python.helper.new_types import PrereqFormat

###############################################################################
class PrereqFilter(Filter):
    """
    Filter the prereq component and return its new result.
    """

    allowed_type = PrereqFormat
