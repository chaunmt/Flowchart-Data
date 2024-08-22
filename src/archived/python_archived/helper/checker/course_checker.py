"""
This module contains class CourseChecker which
perform checks on Course type related object.
"""

from python_archived.helper.new_types import Course, CourseShell
from python_archived.helper.json_handler import JSONHandler

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

        # NoneType is not a valid object to compare
        if not a or not b:
            return False

        # We can't compared objects of different types/instances
        if not (isinstance(a, type(b)) and isinstance(b, type(a))):
            return False

        if not a.uid == b.uid:
            return False

        return True

    #############################################################################
    @staticmethod
    def is_writing(suffix: str) -> bool:
        """
        Check whether a course is a writing course based on its code's suffix.
        """

        if suffix in ('W', 'V'):
            return True
        return False

    #############################################################################
    @staticmethod
    def is_honors(suffix: str) -> bool:
        """
        Check whether a course is an honors course based on its code's suffix.
        """

        if suffix in ('H', 'V'):
            return True
        return False

    #############################################################################
    @staticmethod
    def is_valid_subj(subject: str) -> bool:
        """
        Check whether a course's subject is valid.
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
        Check whether a course's number is valid.
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
        Check whether a course's suffix is valid.
        """

        if suffix in ['', 'W', 'H', 'V']:
            return True

        return False
