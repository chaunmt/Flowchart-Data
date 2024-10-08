"""
This module contains class NestedCourseConverter which contains
converters dedicated to encoded, decoded, and reformat our nested course info strings.
"""

from python_archived.helper.checker.string_checker import StringChecker
from python_archived.filter.string_filter import StringFilterBracket, StringFilterRedundancy

from python_archived.converter.prereq_logic_converter import PrereqLogicConverter

class NestedCourseConverter:
    """
    Converters dedicated to encoded, decoded, and reformat our nested course info strings.
    """

    #############################################################################
    @staticmethod
    def encoded_string(info: str) -> list:
        """
        This method transform a string into a list of encoded substrings with
        nested level but no logical operations ('and', 'or').\n
        Substrings enclosed in brackets will be changed into encoded strings.\n
        ##########################\n
        The encoded process is as follow:
            - Substring enclosed in brackets will be changed into a string with format:\n
            'NESTEDSTR' + their index in the encoded substrings list for decoding purpose.\n
            - The encoding process starts from inside out.\n
        ##########################\n
        EX: "Required CSCI 4041 and (CSCI 3081W, [MATH 2033/2021] or instructor consent)."\n
        ==> nested_str[0] = "NESTEDSTR0" = "MATH 2033/2021"\n
        ==> nested_str[1] = "NESTEDSTR1" = "CSCI 3081W, NESTEDSTR0 or instructor consent"\n
        ==> nested_str[2] = "Required CSCI 4041 and NESTEDSTR1"\n
        """

        # Filter info string's bracket
        info = StringFilterBracket(info).process()

        # Set up
        nested_strings = []
        open_brackets = []

        # Start encoding
        r = 0
        while r < len(info):
            # Record the open bracket's position
            if info[r] == '[':
                open_brackets.append(r)
            # Close bracket signifies time to encoded a substring
            elif info[r] == ']' and open_brackets:
                l = open_brackets.pop()
                enclosed_string = info[l:r + 1]

                # If this substring contains number, it contains a course's code
                if StringChecker.has_number(enclosed_string):
                    # Save the substring into nested_strings list
                    nested_strings.append(enclosed_string)

                    # Replace the substring with encoded key in the parent string
                    key = f'NESTEDSTR{len(nested_strings) - 1}'
                    info = info[:l] + key + info[r + 1:]
                    r = l + len(key) - 1
                else:
                    # Remove the substring if it is redundant
                    info = info[:l] + info[r + 1:]
                    r = l - 1
            r = r + 1

        # Add the leftover encoded info to the end of
        # the encoded list of nested substrings
        nested_strings.append(info)

        # Return the encoded info string and the list of nested encoded substring
        return nested_strings

    #############################################################################
    @classmethod
    def encoded(cls, info: str, target_course_subject: str) -> list:
        """
        The method is used to encoded an info string into
        a list of encoded objects with a nested logical structure.\n
        Redundant info will be removed as only course's info substrings are kept.\n
        ##########################\n
        EX: "Required CSCI 4041 and (CSCI 3081W, [MATH 2033/2021] or instructor consent)."\n
        ==> encoded_strings = [
            {
                "or" : {
                    "MATH2033",\n
                    "MATH2021"
                }
            },\n
            {
                "and" : {
                    "CSCI3081W",\n
                    "NESTEDSTR0"
                }
            },\n
            {
                "and" : {
                    "CSCI4041",\n
                    "NESTEDSTR1"
                }
            }
        ]
        """

        # Encoded the info string
        encoded_strings = cls.encoded_string(info)

        # Remove redundant part of the encoded info string
        last_index = len(encoded_strings) - 1

        encoded_strings[last_index] = (
            StringFilterRedundancy(encoded_strings[last_index]).process()
        )

        # Convert the list of encoded substrings into a structure of nested logical objects
        encoded_objs = []
        for index, encoded_string in enumerate(encoded_strings):
            encoded_objs[index] = (
                PrereqLogicConverter.logical_op_converter(
                    encoded_string,
                    target_course_subject
                )
        )

        return encoded_objs

    #############################################################################
    @classmethod
    def decoded(cls, info: str) -> list:
        """
        This method decodes the encoded info string into ... TODO
        """
        # TODO
