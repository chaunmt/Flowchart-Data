"""
This module contains converters on prerequisites object .\n
It includes CourseInfoConverter and PrereqConverter.
"""

import re

from python.splitter.prereq import CourseInfoSplitter
from python.sources.format import JSONHandler

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
        
        if not alter_subj:
            raise ValueError("An alternative subject is required.")
        
        # Narrow down the info string with regex (first match only)
        code_pattern = r"([A-Za-z]+)?(\s+)?(\d{4})(\s+)?([A-Za-z]+)?"
        match = re.search(code_pattern, s)
        
        # Get possible acceptable subject, number, and suffix
        [subj, num, suf] = CourseInfoSplitter.code_into_subj_num_suf(match[0])
        
        if subj == "":
            subj = alter_subj
        
        return subj + num + suf
        
    
    #############################################################################
    def course_code_to_uid(codestr : str) -> str:
        """
        Convert a string of course's code into that course's uid.
        """
        
        subj_courses = JSONHandler.get_from_path("data/UMNTC/Course/General/allCourses.json")
        
        for course in subj_courses:
            if codestr == course.code:
                return course.uid
        
###############################################################################
class PrereqInfoConverter:
    """
    Convert objects into prerequisites type.
    """

    #############################################################################
    def to_nested_substrs(s : str) -> list:
        """
        Separated a string into a list of substrings by their nested level.\n
        A nested substring (a substring enclosed in square brackets) is replaced by
        a combination of "NESTEDS" + their index in the nested substring list.\n
        Their index is granted from inside out.\n
        
        EX: "A and (B and [C] or D)."\n
        ==> nested_ss[0] = "NESTEDS0" = "C"\n
        ==> nested_ss[1] = "NESTEDS1" = "B and NESTEDS0 or D"\n
        ==> nested_ss[2] = "NESTEDS2" = "A and NESTEDS1"\n
        """
    
    #############################################################################
    def to_nested_dict(nested_s : str) -> dict:
        """
        
        EX: nested_s = "A and B"\n
        ==> nested_dict = "and" : { "A", "B" }
        """
        
    #############################################################################
    def to_nested_dicts(nested_ss : list) -> list:
        """
        
        EX: nested_ss = [\n
            "A and B",
            "C or NESTEDS0"
        ]\n
        ==> nested_dicts = [\n
            "and" : { "A", "B" },\n
            "or" : { "C", "NESTEDS0" }\n
        ]
        """
    
    #############################################################################
    def to_combined_logical_dict(nested_dicts : list) -> dict:
        """
        
        EX: nested_dicts = [\n
            "and" : { "A", "B" },\n
            "or" : { "C", "NESTEDS0" }\n
        ]
        ==> logic_dict = {
            "or" : {
                "C",
                "and" : { "A", "B" }
            }
        }
        """

