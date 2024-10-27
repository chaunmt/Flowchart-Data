"""
This module contains converters on prerequisites object .\n
It includes CourseInfoConverter and PrereqConverter.
"""

import re

from python.checker.course import CourseInfoChecker
from python.splitter.course import CourseInfoSplitter
from python.sources.format import JSONHandler
from python.sources.config.school import SchoolConfigManager

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

        s = s.replace('(', '[')
        s = s.replace(')', ']')

        return s

    #############################################################################
    @staticmethod
    def combine_standalone_subject(s: str) -> str:
        """
        Convert something like "CSCI [3081W and 4041]" into "[CSCI 3081W and 4041]".
        """

        patterns = [
            r"([A-Za-z]+)(\s+)?(\[+)(\s+)?(\d+)",
            r"([A-Za-z]+)(\s+)?(:+)(\s+)?(\d+)",
            r"([A-Za-z]+)(\s+)?(\'+)(\s+)?(\d+)",
            r"([A-Za-z]+)(\s+)?(\"+)(\s+)?(\d+)",
            r"([A-Za-z]+)(\s+)?(\-+)(\s+)?(\d+)"
        ]

        # Substitute and combine the subject with the course numbers inside the brackets
        for pattern in patterns:
            s = re.sub(pattern, r"\3\1 \5", s)  # Use \1 for subject and \5 for course number

        # Return the modified string
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
        s = s.upper()
        pattern =  r'\b([A-Z]+)?(\s+)?(\d{2,4})([A-Z]{0,1})?\b'
        match = re.search(pattern, s)

        if not match:
            return ""

        # Get possible acceptable subject, number, and suffix
        [subj, num, suf] = CourseInfoSplitter.code_into_subj_num_suf(match.group())

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
        patterns = [
            r'\b([A-Za-z]+)?(\s+)?(\d{2,4})([A-Za-z]{0,1})?\b',  # Code pattern
            r'\b(NESTEDS)(\d+)\b'  # Encoded key pattern (EX: NESTEDS0)
        ]
        pattern = f'({patterns[0]}|{patterns[1]})'

        # Get the list of matches strings
        matches = re.findall(pattern, s)

        # Get the string of codes out of the matched tuples
        course_codes = [match[0] if match[0] else "" for match in matches]

        for index, code in enumerate(course_codes):
            # Uniform all code's format and remove unacceptable codes.
            if not "NESTEDS" in code:
                course_codes[index] = cls.info_to_course_code(code, alter_subj)

            # Get closest subject.
            if get_closest_subj:
                [subj, _, _] = (
                    CourseInfoSplitter.code_into_subj_num_suf(course_codes[index])
                )
                if CourseInfoChecker.is_valid_subj(subj) and subj != alter_subj:
                    alter_subj = subj

        return course_codes


    #############################################################################
    @staticmethod
    def course_code_to_uid(school_uid: str, codestr : str) -> str:
        """
        Convert a string of course's code into that course's uid.
        """
        # Get the school's config data
        config = SchoolConfigManager(school_uid)

        # Find the course shells json to cross-checked values
        # Only courses exist in this json file are deemed valid courses
        all_courses = JSONHandler.get_from_path(
            f"{config.get_course_path()}/allCoursesShells.json"
        )

        # if the codes are the same then they are the same course.
        for uid, course in all_courses.items():
            if codestr in (course['code'], course['code'][:-1]):
                return uid

        return ""

###############################################################################
class PrereqInfoConverter:
    """
    Convert objects into prerequisites type.
    """

    def __init__(self, s: str, alter_subj: str, school_uid: str) -> None:
        """
        Initialize the class instance.
        """
        self._prereq_str = s
        self._prereq = {}
        self._alter_subj = alter_subj
        self._school_uid = school_uid

    def process(self) -> dict:
        """
        Convert info string into a logical structured dictionary following PrereqFormat.
        """
        prereq = self._prereq_str
        prereq = self.to_nested_ss(prereq)
        prereq = self.to_nested_code_dicts(prereq)
        prereq = self.to_combined_logic_code_dict(prereq)
        prereq = self.to_logic_uid_dict(prereq)

        self._prereq = prereq

    def get_prereq(self):
        """
        Get the prereq dictionary value.
        """
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

        # Convert 'A or B' into { or : ['A', 'B'] }
        if "or" in s:
            return {
                "or" : CourseInfoConverter.info_to_course_codes(s, self._alter_subj, True)
            }

        # Convert 'A and B', 'A B' into { and : ['A', 'B'] }
        return {
            "and" : CourseInfoConverter.info_to_course_codes(s, self._alter_subj, True)
        }

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

        if not nested_code_dicts:
            nested_code_dicts.append({})

        return nested_code_dicts

    #############################################################################
    def to_combined_logic_code_dict(self, nested_code_dicts : list) -> dict:
        """
        Convert a list of nested logical course's codes dictionaries
        into one combined logical course's codes dictionary.\n

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

            # Prevent type error: prereq = 1 list
            if not isinstance(logic_code_dict, dict):
                return { 'and' : logic_code_dict }

            # Breaking all encoded keys into course's codes
            while True:
                if not isinstance(logic_code_dict, dict):
                    break

                # Start the decoding process
                decoded = False
                for _, values in logic_code_dict.items():
                    for vi, value in enumerate(values):
                        # Recursively traverse through all nested dictionary
                        if isinstance(value, dict):
                            values[vi] = rec_combine(nested_code_dicts, value)
                        elif isinstance(value, str):
                            # Decode the encoded key
                            if value.startswith("NESTEDS"):
                                index = int(value[7:])

                                # Replace encoded key with its actual value
                                values[vi] = nested_code_dicts[index]
                                decoded = True

                # If no more encoded key is found, no more decode is needed
                if not decoded:
                    break

            return logic_code_dict

        return rec_combine(nested_code_dicts, nested_code_dicts[-1])

    def to_logic_uid_dict(self, logic_code_dict : dict) -> dict:
        """
        Convert a logical course's codes dictionary
        into a logical course's uids dictionary.\n

        EX: logic_code_dict = {
            "or" : { "C", "and" : { "A", "B" } }
        }
        ==> logic_uid_dict = {
            "or" : {
                "054684987",
                "and" : { "065468458", "089841545" }
            }
        }
        """

        def rec_replace(values):
            """
            Recursively replace all course's codes into course' uids.
            """

            if isinstance(values, str):
                # Replace code with uid
                return CourseInfoConverter.course_code_to_uid(self._school_uid, values)

            # Recursively replace nested value in list
            if isinstance(values, list):
                return [rec_replace(value) for value in values]

            # Recursively replace nested value in dictionary
            if isinstance(values, dict):
                return {
                    key: rec_replace(value)
                    for key, value in values.items()
                }

            return values

        return rec_replace(logic_code_dict)
