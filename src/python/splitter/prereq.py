"""
This module contains class CourseInfoSplitter which
split a course's info string into a list of strings.
"""

import re

from python.splitter.string import StringSplitter
from python.checker.prereq import CourseChecker

class CourseInfoSplitter:
    """
    A class to split a course's info string into a list of strings.
    """

    #############################################################################
    @classmethod
    def code_into_subj_num_suf(cls, s: str) -> list:
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
    def split_num_suf(s: str) -> list:
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
