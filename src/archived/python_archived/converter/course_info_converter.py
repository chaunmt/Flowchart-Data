"""
This module contains class CourseInfoConverter which contains
converters dedicated to alter course's info string.
"""

from python_archived.helper.checker.course_checker import CourseChecker
from python_archived.helper.course_info_splitter import CourseInfoSplitter
from python_archived.converter.prereq_logic_converter import PrereqLogicConverter

class CourseInfoConverter:
    """
    Converter dedicated to transform course's info strings.
    """

    @staticmethod
    def to_valid_codes(codes: list, target_course_subject: str) -> list:
        """
        Convert a list of strings in course's code's form
        into a list of valid course's code strings.\n
        Criteria:
        - Subject has to be a department code.
        - Number has to have 4 digits with no '0' prefix.
        - Suffix has to be in ['', 'W', 'H', 'V'].
        """

        for index, code in enumerate(codes):
            [subject, number, suffix] = CourseInfoSplitter.to_subj_num_suf(code)

            # If a code's number is invalid, this code is invalid
            if not CourseChecker.is_valid_num(number):
                codes[index] = ''
                continue

            # If a code's subject or suffix is invalid, make them empty string
            if not CourseChecker.is_valid_subj(subject):
                subject = ''
            if not CourseChecker.is_valid_suf(suffix):
                suffix = ''

            # Assign new code value
            codes[index] = subject + number + suffix

        # Assign empty code's subject with
        # target's course subject or closest code's subject
        codes = PrereqLogicConverter.missing_subject_converter(
            codes,
            target_course_subject
        )

        return codes
