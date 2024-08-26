"""
This module contains converters on prerequisites object .\n
It includes CourseInfoConverter and PrereqConverter.
"""

import re

from python.splitter.course import CourseInfoSplitter
from python.sources.format import JSONHandler
from python.filter.course import PrereqFilterDuplicate, PrereqFilterEmpty, PrereqFilterRedundantNest

###############################################################################
class CourseInfoConverter():
    """
    Convert course's info string's format and value.
    """

    #############################################################################
    @staticmethod
    def sign_to_logical_op(s: str) -> str:
        """
        Convert some signs to their respective logical operation words.
        """

        s = s.replace(",", " and ")
        s = s.replace("/", " or ")
        s = s.replace("&", " and ")

        return s

    #############################################################################
    @staticmethod
    def paren_to_square_bracket(s: str) -> str:
        """
        Convert all parentheses into square brackets.
        """

        s.replace('(', '[')
        s.replace(')', ']')

        return s

    #############################################################################
    @staticmethod
    def info_to_course_code(s: str, alter_subj: str) -> str:
        """
        Convert an info string into a course's code form if possible.\n
        This method only returns the first code.\n
        An alternative course's subject is required. It will be used if no subject is found. \n
        EX:\n
        "CSci 3081 W" ==> "CSCI3081W" \n
        "csci 2021, csci 2041, and more" ==> "CSCI2021"\n
        "This is not a valid one :)" ==> "" \n
        """

        # Alternative subject is required.
        if not alter_subj:
            return ""

        # Narrow down the info string with regex (first match only)
        code_pattern = r"([A-Za-z]+)?(\s+)?(\d{4})(\s+)?([A-Za-z]+)?"
        match = re.search(code_pattern, s)

        # Get possible acceptable subject, number, and suffix
        [subj, num, suf] = CourseInfoSplitter.code_into_subj_num_suf(match[0])

        if subj == "":
            subj = alter_subj

        return subj + num + suf

    #############################################################################
    @classmethod
    def info_to_course_codes(cls, s: str, alter_subj: str, get_closest_subj: bool) -> list:
        """
        Get a list of substring with course's code's format out of the original string.\n
        An alternative course's subject is required. It will be used if no subject is found. \n
        If "get_closest_subj" is true, alter_subj will be replaced by
        the closest acceptable subject found.\n

        Noted: Nested string's encoded form ("NESTEDS0", ...) is a valid code.\n

        EX:\n
        s = "Students have to take CSCI 2041 and 2021 or NESTEDS0, 3081W."\n
        alter_subj = "CSCI"\n
        ==> [ "CSCI2041", "", "NESTEDS0", "CSCI3081W" ]\n
        """

        # The regex pattern to get out acceptable code or partial code
        patterns = [ # TODO IMPROVE PREFIX
            r'\b[A-Za-z]+\s?\d{2,4}[A-Za-z]\b'  # Full code pattern (EX: CSCI 3081W)
            , r'\b\d{4}[A-Za-z]{0,1}\b'  # No subject code pattern (EX: 3081W, 4041)
            , r'\bNESTEDS\d+\b'  # Encoded key pattern (EX: NESTEDSTR0)
        ]
        pattern = f'({patterns[0]}|{patterns[1]}|{patterns[2]})'

        # Get the list of matches strings
        course_codes = re.findall(pattern, s)

        for index, code in enumerate(course_codes):
            # Uniform all code's format and remove unacceptable codes.
            if not "NESTEDS" in code:
                course_codes[index] = cls.info_to_course_code(code, alter_subj)

            # Get closest subject.
            if get_closest_subj:
                [subj, num, suf] = (
                    CourseInfoSplitter.code_into_subj_num_suf(course_codes[index])
                )
                if subj != alter_subj:
                    alter_subj = subj

        return course_codes


    #############################################################################
    @staticmethod
    def course_code_to_uid(codestr : str) -> str:
        """
        Convert a string of course's code into that course's uid.
        """

        subj_courses = JSONHandler.get_from_path("D:/Dev/Project/Course-Flowchart-Data/data/UMNTC/Course/General/allCourses.json")

        for course in subj_courses:
            if codestr == course['code']:
                return course['uid']
        
        return codestr

###############################################################################
class PrereqInfoConverter:
    """
    Convert objects into prerequisites type.
    """
    def __init__(self, s : str, alter_subj : str) -> None:
        # Standardize input string
        s = CourseInfoConverter.paren_to_square_bracket(s)
        s = CourseInfoConverter.sign_to_logical_op(s)

        self._prereq_str = s
        self._prereq = {}
        self._alter_subj = alter_subj

    def process(self) -> dict:
        prereq = self._prereq_str
        prereq = self.to_nested_ss(prereq)
        prereq = self.to_nested_code_dicts(prereq)
        prereq = self.to_combined_logic_code_dict(prereq)

        self._prereq = prereq

    def get_prereq(self):
        return self._prereq

    #############################################################################
    def to_nested_ss(self, s : str) -> list:
        """
        Separated a string into a list of substrings by their nested level.\n
        A nested substring (a substring enclosed in square brackets) is replaced by
        a combination of "NESTEDS" + their index in the nested substring list
        (index is granted from inside out).\n

        This process can be referred to as "encoding".
        As such, the combination mentioned above is called "encoded key"
        and the string results from this process can be referred to as "encoded string".\n

        EX: "A and (B and [C] or D)."\n
        ==> nested_ss[0] = "NESTEDS0" = "C"\n
        ==> nested_ss[1] = "NESTEDS1" = "B and NESTEDS0 or D"\n
        ==> nested_ss[2] = "NESTEDS2" = "A and NESTEDS1"\n
        """

        # Keep track of the nested substrings and the open brackets' positions
        nested_ss = []
        open_brackets = []

        r = 0
        while r < len(s):
            # Record the open bracket's position
            if s[r] == '[':
                open_brackets.append(r)

            # Close bracket signifies time to extract a nested substring
            elif s[r] == ']' and open_brackets:
                l = open_brackets.pop()
                nested_s = s[l:r + 1]

                # Save the substring into the nested substrings list
                nested_ss.append(nested_s)

                # Replace the substring with the encoded key in the parent string
                key = f'NESTEDS{len(nested_ss) - 1}'
                s = s[:l] + key + s[r + 1:]
                r = l + len(key) - 1

            r = r + 1

        # Append the latest encoded string into our nested substrings list
        nested_ss.append(s)

        return nested_ss

    #############################################################################
    def to_nested_code_dict(self, s : str) -> dict:
        """
        Convert a string into a logical dictionary of course's codes
        based on the logical operation keyword found.\n

        For ambiguous case like multiple "and", "or".
        Operation "and" will be prioritized.\n

        EX: s = "A and B"\n
        ==> nested_code_dict = "and" : { "A", "B" }
        """

        # Convert 'A and B' into { and : ['A', 'B'] }
        if "and" in s:
            return {
                "and" : CourseInfoConverter.info_to_course_codes(s, self._alter_subj, True)
            }

        # Convert 'A or B' into { or : ['A', 'B'] }
        if "or" in s:
            return {
                "or" : CourseInfoConverter.info_to_course_codes(s, self._alter_subj, True)
        }

        # Convert 'A B' into ['A', 'B']
        return CourseInfoConverter.info_to_course_codes(s, self._alter_subj, True)

    #############################################################################
    def to_nested_code_dicts(self, nested_ss : list) -> list[dict]:
        """
        Convert a list of nested (encoded) substrings into a list of
        nested logical course's codes dictionaries.\n

        EX: nested_ss = [\n
            "A and B",
            "C or NESTEDS0"
        ]\n
        ==> nested_code_dicts = [\n
            "and" : { "A", "B" },\n
            "or" : { "C", "NESTEDS0" }\n
        ]
        """

        nested_code_dicts = []

        for s in nested_ss:
            d = self.to_nested_code_dict(s)
            nested_code_dicts.append(d)
        
        if nested_code_dicts == []:
            nested_code_dicts.append({})

        return nested_code_dicts

    #############################################################################
    def to_combined_logic_code_dict(self, nested_code_dicts : list) -> dict:
        """
        Convert a list of nested logical course's codes dictionaries
        into one combined logical course's codes dictionaryy.\n

        EX: nested_code_dicts = [\n
            "and" : { "A", "B" },\n
            "or" : { "C", "NESTEDS0" }\n
        ]
        ==> logic_code_dict = {
            "or" : {
                "C",
                "and" : { "A", "B" }
            }
        }
        """

        def rec_combine(nested_code_dicts : list[dict], current_dict : dict) -> dict:
            # The top level of all nests is the last dictionary in the nest list
            logic_code_dict = current_dict or {}

            # Breaking all encoded keys into actual course's codes
            while True:
                decoded = False
                
                if isinstance(logic_code_dict, dict):
                    for k, values in logic_code_dict.items():
                        for vi, value in enumerate(values):
                            if isinstance(value, dict):
                                values[vi] = rec_combine(nested_code_dicts, value)
                            elif isinstance(value, str):
                                if value.startswith("NESTEDS"):
                                    index = int(value[7:])

                                    # Replace encoded key with its actual value
                                    values[vi] = nested_code_dicts[index]
                                    decoded = True
                                else:
                                    values[vi] = CourseInfoConverter.course_code_to_uid(value)

                # If no more encoded key is found, no more decode is needed
                if not decoded:
                    break

            return logic_code_dict
        
        return rec_combine(nested_code_dicts, nested_code_dicts[-1])
