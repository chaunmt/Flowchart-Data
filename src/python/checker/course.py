"""
This module contains checkers on prerequisites object .\n
It includes CourseChecker and CourseInfoChecker.
"""

from python.schema.course import Course, CourseShell, PrereqFormat
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
            raise ValueError("NoneType object is not a valid object to compare.")

        # We can't compared objects of different types/instances
        if not (isinstance(a, type(b)) and isinstance(b, type(a))):
            return False

        if not a.uid == b.uid:
            return False

        return True

###############################################################################
class PrereqChecker():
    """
    Perform checks on PrereqFormat type related object.
    """

    #############################################################################
    @classmethod
    def has_shared_uid(cls, prereq: PrereqFormat, course_shells: dict) -> bool:
        """
        Check whether a logical prerequisites dictionary has any shared uid with a course shells.
        """

        # If found a shared uid, return True
        if isinstance(prereq, str) and prereq in course_shells:
            return True
        elif isinstance(prereq, list):
            # Traverse all possible elements
            while True:
                for _, value in enumerate(prereq):
                    # If found a shared uid, return True
                    if isinstance(value, str) and value in course_shells:
                        return True

                    # Recursively traverse nested value
                    if cls.has_shared_uid(value, course_shells):
                        return True

                return False  # No shared uid found

        elif isinstance(prereq, dict): # Logical operation 'and', 'or' and their value
            # Traverse all possible elements
            while True:
                for _, value in prereq.items():
                    # Recursively traverse nested value
                    if cls.has_shared_uid(value, course_shells):
                        return True

                return False  # No shared uid found

        return False  # No shared uid found
