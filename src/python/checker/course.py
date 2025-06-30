"""
This module contains checkers on prerequisites object.\n
It includes CourseChecker and PrereqChecker.
"""

from python.schema.definitions import PrereqFormat
from python.sources.format import JSONHandler
from python.sources.config.school import SchoolConfig

class CourseChecker:
    """
    Perform checks on a course's info.
    """

    @staticmethod
    def is_writing_suf(suffix: str) -> bool:
        return suffix in ('W', 'V')

    @staticmethod
    def is_honors_suf(suffix: str) -> bool:
        return suffix in ('H', 'V')

    @staticmethod
    def is_valid_subj(subject: str) -> bool:
        school_config = SchoolConfig(school_id="umn_umntc_peoplesoft")
        valid_subjs = JSONHandler.get_from_path(f"{school_config.all_subjects_path}")
        return subject in valid_subjs

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

    @staticmethod
    def is_valid_suf(suffix: str) -> bool:
        return suffix in ['', 'W', 'H', 'V']

###############################################################################
class PrereqChecker():
    """
    Perform checks on PrereqFormat type related object.
    """

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
