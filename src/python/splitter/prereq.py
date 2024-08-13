"""
This module contains class CourseInfoSplitter which
split a course's info string into a list of strings.
"""

import re

from python.splitter.string import StringSplitter
from python.checker.prereq import CourseChecker
from python.filter.string import StringFilterSpace

class CourseInfoSplitter:
    """
    A class to split a course's info string into a list of strings.
    """

    #############################################################################
    @classmethod
    def to_subj_num_suf(cls, s: str) -> list:
        """
        Split a string of Course's code into a list of [subject, number, suffix].
        """

        splits = StringSplitter.letter_and_num(s.upper())

        subject, number, suffix = [None, None, None]
        for split in splits:
            # If exists, subject has to come before number
            if split.isalpha() and not subject and not number:
                if CourseChecker.is_valid_subj(split):
                    subject = split
                else:
                    subject = ''

            # Number can exist by itself and a code has to have a number
            elif split.isdigit() and not number:
                if CourseChecker.is_valid_num(split):
                    number = split
                else:
                    return [None, None, None]

            # If exists, suffix has to be the last member
            elif number and not suffix:
                if CourseChecker.is_valid_suf(split):
                    suffix = split
                else:
                    suffix = ''
                break

        # Number is required for valid code
        if not number:
            return [None, None, None]

        if not subject:
            subject = ''

        if not suffix:
            suffix = ''

        return [subject, number, suffix]

    #############################################################################
    @staticmethod
    def to_num_suf(s: str) -> list:
        """
        Split a string of Course's number with suffix into a list of [number, suffix].
        """

        splits = StringSplitter.letter_and_num(s.upper())

        number, suffix = [None, None]
        for split in splits:
            # Number can exist by itself
            if split.isdigit() and not number:
                if CourseChecker.is_valid_num(split):
                    number = split
                else:
                    return [None, None]

            # If exists, suffix has to be the last member
            elif number and not suffix:
                if CourseChecker.is_valid_suf(split):
                    suffix = split
                else:
                    suffix = ''
                break

        # Number is required for valid value
        if not number:
            return [None, None]

        if not suffix:
            suffix = ''

        return [number, suffix]

    #############################################################################
    @staticmethod
    def to_codes(s: str) -> list:
        """
        Get a list of substring with course's code's format out of the original string.\n
        Noted: Encoded key's prefix "NESTEDSTR" is treated as a subject,
        making the complete key a valid course's code.\n

        EX: "Students have to take CSCI 2041 and 2021 or NESTEDSTR0, 3081W."\n
        ==> [ "CSCI2041", "AND2021", "NESTEDSTR0", "3081W" ]\n
        """

        # The regex pattern to get out acceptable code or partial code
        pattern = (
            '\b[A-Za-z]+\\s?\\d{2,4}[A-Za-z]*\b'  # Full code pattern (EX: CSCI 3081W)
            + '\b\\d{4}[A-Za-z]{0,1}*\b'  # No subject code pattern (EX: 3081W, 4041)
            + '\bNESTEDSTR\\d+\b'  # Encoded key pattern (EX: NESTEDSTR0)
        )

        # Get the list of matches strings
        course_codes = re.findall(pattern, s)

        for index, code in enumerate(course_codes):
            # Remove all space to follow CourseDog's course code format
            course_codes[index] = StringFilterSpace(code).process()

            # Convert all letters to uppercase
            course_codes[index] = course_codes[index].upper()

        return course_codes
