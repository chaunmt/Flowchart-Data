"""
This module contains tests for course's converter.
"""

import pytest
from ...converter.course import (
    CourseInfoConverter,
    PrereqInfoConverter
)

class TestCourseInfoConverter:
    """
    This class contains tests for the CourseInfoConverter class.
    """
    
    #############################################################################
    @pytest.mark.parametrize("original, expected", [
        # Case 1
        ("Math101, CS101", "Math101 and  CS101"),
        # Case 2
        ("Math101/CS101", "Math101 or CS101"),
        # Case 3
        ("Math101 & CS101", "Math101  and  CS101"),
        # Case 4
        ("Bio101, Chem101 & Phys101", "Bio101 and  Chem101  and  Phys101"),
        # Case 5
        ("/", " or "),
    ])
    def test_sign_to_logical_op(self, original, expected):
        """
        This method contains tests for the sign_to_logical_op method.
        """
        result = CourseInfoConverter.sign_to_logical_op(original)
        assert result == expected, f"Expected '{expected}', got '{result}'"
    
    #############################################################################
    @pytest.mark.parametrize("original, expected", [
        # Case 1
        ("CSCI (3081W) and (4041)", "CSCI [3081W] and [4041]"),
        # Case 2
        ("(Math101)", "[Math101]"),
        # Case 3
        ("No parentheses here", "No parentheses here"),
        # Case 4
        ("(Multiple) (Paren) (Sets)", "[Multiple] [Paren] [Sets]"),
        # Case 5
        ("CS101)", "CS101]"),
    ])
    def test_paren_to_square_bracket(self, original, expected):
        """
        This method contains tests for the paren_to_square_bracket method.
        """
        result = CourseInfoConverter.paren_to_square_bracket(original)
        assert result == expected, f"Expected '{expected}', got '{result}'"
    
    #############################################################################
    @pytest.mark.parametrize("original, expected", [
        # Case 1
        ("CSCI [3081W and 4041]", "[CSCI 3081W and 4041]"),
        # Case 2
        ("CSCI [2041]", "[CSCI 2041]"),
        # Case 3
        ("No subject here", "No subject here"),
        # Case 4
        ("CSCI - 3081W", "-CSCI 3081W"),
        # Case 5
        ("CSCI: 2041", ":CSCI 2041"),
    ])
    def test_combine_standalone_subject(self, original, expected):
        """
        This method contains tests for the combine_standalone_subject method.
        """
        result = CourseInfoConverter.combine_standalone_subject(original)
        assert result == expected, f"Expected '{expected}', got '{result}'"
    
    #############################################################################
    @pytest.mark.parametrize("original, alter_subj, expected", [
        # Case 1
        ("CSci 3081 W", "CSCI", "CSCI3081"),  # We don't care about suffix if it's separated
        # Case 2
        ("csci 2021, csci 2041", "CSCI", "CSCI2021"),
        # Case 3
        ("Math 101", "MATH", "MATH"),  # The number is invalid --> skip it first
        # Case 4
        ("Invalid string", "CSCI", ""),
        # Case 5
        ("BIO 1101", "BIOL", "BIOL1101"),
    ])
    def test_info_to_course_code(self, original, alter_subj, expected):
        """
        This method contains tests for the info_to_course_code method.
        """
        result = CourseInfoConverter.info_to_course_code(original, alter_subj)
        assert result == expected, f"Expected '{expected}', got '{result}'"
    
    #############################################################################
    @pytest.mark.parametrize("original, alter_subj, get_closest_subj, expected", [
        # Case 1
        (
            "CSCI 2041 and 2021 or NESTEDS0, MATH 1501, 3081W",
            "CSCI",
            False,  # Don't get closest subject
            ["CSCI2041", "CSCI2021", "NESTEDS0", "MATH1501", "CSCI3081W"]
        ),
        # Case 2
        (
            "BIOLOGY 101 and CHEM 102",
            "BIOL",
            True,   # Get closest subject
            ["BIOL", "BIOL"]    # CHEM isn't chosen because code is invalid by regex
        ),
        # Case 3
        (
            "BIOLOGY 101 and CHEM 1022",
            "BIOL",
            True,   # Get closest subject
            ["BIOL", "CHEM1022"]
        ),
        # Case 4
        (
            "NESTEDS1, NESTEDS2",
            "CSCI",
            False,  # Don't get closest subject
            ["NESTEDS1", "NESTEDS2"]
        ),
        # Case 5
        (
            "MATH 1001, CSCI 3081W, 101",
            "MATH",
            True,   # Get closest subject
            ["MATH1001", "CSCI3081W", "CSCI"]   # Number is picked but is found to be invalid
        ),
    ])
    def test_info_to_course_codes(self, original, alter_subj, get_closest_subj, expected):
        """
        This method contains tests for the info_to_course_codes method.
        """
        result = CourseInfoConverter.info_to_course_codes(original, alter_subj, get_closest_subj)
        assert result == expected, f"Expected '{expected}', got '{result}'"
    
    #############################################################################
    # Parameterized test cases
    @pytest.mark.parametrize("original, expected", [
        ("CHEM4352", "004137"),     # Found in mock data
        ("CHEM4411", "004142"),     # Found in mock data
        ("CSCI9999", ""),   # Not in mock data
        ("11011010", ""),   # Not in mock data
        ("MATHMATH", ""),   # Not in mock data
    ])
    def test_course_code_to_uid(mock_for_course_code_to_uid, original, expected):
        """
        This method contains tests for the course_code_to_uid method.
        """
        result = CourseInfoConverter.course_code_to_uid("umn_umntc_peoplesoft", original)
        assert result == expected, f"Expected '{expected}', got '{result}'"

class TestPrereqInfoConverter:
    """
    This class contains tests for the PrereqInfoConverter class.
    """

    def test_init(self):
        """
        This method contains tests for the init method.
        """
    def test_process(self):
        """
        This method contains tests for the process method.
        """
    def test_get_prereq(self):
        """
        This method contains tests for the get_prereq method.
        """
    def test_to_nested_ss(self):
        """
        This method contains tests for the to_nested_ss method.
        """
    def test_to_nested_code_dict(self):
        """
        This method contains tests for the to_nested_code_dict method.
        """
    def test_to_nested_code_dicts(self):
        """
        This method contains tests for the to_nested_code_dicts method.
        """
    def test_to_combined_logic_code_dict(self):
        """
        This method contains tests for the to_combined_logic_code_dict method.
        """
    def test_to_logic_uid_dict(self):
        """
        This method contains tests for the to_logic_uid_dict method.
        """
