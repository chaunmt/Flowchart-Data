"""
This module contains checkers on prerequisites object .\n
It includes CourseChecker and CourseInfoChecker.
"""

from python.schema.course import Course, CourseShell
from python.sources.format import JSONHandler

class CourseInfoChecker:
    """
    Perform checks on an info string of Course's type object.
    """

    #############################################################################
    @staticmethod
    def is_writing_suf(suffix: str) -> bool:
        """
        Check whether a Course's suffix is of writing types.
        """

        if suffix in ('W', 'V'):
            return True
        return False

    #############################################################################
    @staticmethod
    def is_honors_suf(suffix: str) -> bool:
        """
        Check whether a Course's suffix is of honors types.
        """

        if suffix in ('H', 'V'):
            return True
        return False

    #############################################################################
    @staticmethod
    def is_valid_subj(subject: str) -> bool:
        """
        Check whether a Course's subject is valid.
        """

        # Get JSON data for valid subject codes
        path = '../data/UMNTC/allSubjects.json'
        data = JSONHandler.get_from_path(path)

        # Only department code is a valid subject code
        if subject in data:
            return True

        return False

    #############################################################################
    @staticmethod
    def is_valid_num(number: str) -> bool:
        """
        Check whether a Course's number is valid.\n
        Note: Pre-college courses (Course with its 'number' value < 1000)
        are excluded from our data (check Readme file for information).
        """

        # NoneType is not a valid number
        if not number:
            return False

        # Remove '0' prefix
        number = number.lstrip('0')

        return number.isdigit() and len(number) == 4

    #############################################################################
    @staticmethod
    def is_valid_suf(suffix: str) -> bool:
        """
        Check whether a Course's suffix is valid.
        """

        if suffix in ['', 'W', 'H', 'V']:
            return True

        return False

###############################################################################
class CourseChecker(CourseInfoChecker):
    """
    Perform checks on Course type related object.
    """

    #############################################################################
    @staticmethod
    def is_equal(a: Course | CourseShell, b: Course | CourseShell) -> bool:
        """
        Check whether 2 Course are the same.
        """

        # NoneType is not a valid object to compare
        if not a or not b:
            return False

        # We can't compared objects of different types/instances
        if not (isinstance(a, type(b)) and isinstance(b, type(a))):
            return False

        if not a.uid == b.uid:
            return False

        return True
