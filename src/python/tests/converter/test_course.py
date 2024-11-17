"""
This module contains tests for course's converter.
"""

# pylint: disable=protected-access,invalid-name

import copy
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
        # We don't care about suffix if it's separated
        ("CSci 3081 W", "CSCI", "CSCI3081"),
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
            # Number is picked but is found to be invalid
            ["MATH1001", "CSCI3081W", "CSCI"]
        ),
    ])
    def test_info_to_course_codes(self, original, alter_subj, get_closest_subj, expected):
        """
        This method contains tests for the info_to_course_codes method.
        """
        result = CourseInfoConverter.info_to_course_codes(
            original, alter_subj, get_closest_subj)
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
    def test_course_code_to_uid(self, original, expected):
        """
        This method contains tests for the course_code_to_uid method.
        """
        result = CourseInfoConverter.course_code_to_uid(
            "umn_umntc_peoplesoft", original)
        assert result == expected, f"Expected '{expected}', got '{result}'"


class TestPrereqInfoConverter:
    """
    This class contains tests for the PrereqInfoConverter class.
    """
    @classmethod
    def setup_class(cls):
        """
        Initialze some helpful variables.
        """
        cls.school_uid = "umn_umntc_peoplesoft"
        cls.original = [
            {
                "info_string": "1913 or 1933 or instr consent",
                "alter_subj": "CSCI"
            },
            {
                "info_string": "at least C- in [PSTL 731 or PSTL 732]",
                "alter_subj": "MATH"
            },
            {
                # Info string is already pre-processed in extractor
                "info_string": "5651 or [Stat 5101 and 5052 and [CSCI 4041 or 2021]]",
                "alter_subj": "MATH"
            }
        ]

        cls.expect = [
            {
                "or": [
                    "809667",
                    "810346"
                ]
            },
            # Empties are filtered later in extractor
            {'and': [{'or': ['', '']}]},
            {
                "or": [
                    "004308",
                    {
                        "and": [
                            "006408",
                            "820085",
                            {
                                "or": [
                                    "003675",
                                    "003673"
                                ]
                            }
                        ]
                    }
                ]
            }
        ]

        cls.converts = []
        for s in cls.original:
            # Initialize
            cls.converts.append(PrereqInfoConverter(
                s["info_string"],
                s["alter_subj"],
                cls.school_uid
            ))

    def test_init(self):
        """
        This method contains tests for the init method.
        """
        # Iterate over each test case
        for i, info in enumerate(self.original):
            # Assert value
            assert self.converts[i]._prereq_str == info["info_string"]
            assert self.converts[i]._alter_subj == info["alter_subj"]
            assert self.converts[i]._school_uid == self.school_uid
            assert self.converts[i]._prereq == {}, (
                "Expected _prereq to be initialized as an empty dictionary"
            )

    def test_process(self):
        """
        This method contains tests for the process method.
        """
        # Iterate over each test cases
        for i, _ in enumerate(self.original):
            # Processed
            result = copy.deepcopy(self.converts[i])
            result.process()

            # Assert value
            assert result._prereq == self.expect[i], (
                f"Expected {self.expect[i]}, got {result._prereq}"
            )

    def test_get_prereq(self):
        """
        This method contains tests for the get_prereq method.
        """
        # Iterate over each test case
        for i, _ in enumerate(self.original):
            # Processed
            result = copy.deepcopy(self.converts[i])
            result.process()

            # Assert value
            assert result.get_prereq() == self.expect[i], (
                f"Expected {self.expect[i]}, got {result._prereq}"
            )

    def test_to_nested_ss(self):
        """
        This method contains tests for the to_nested_ss method.
        """
        # Define expected outputs for each info string from self.original
        expect_outputs = [
            # Expected output for "1913 or 1933 or instr consent"
            ["1913 or 1933 or instr consent"],

            # Expected output for "at least C- in [PSTL 731 or PSTL 732]"
            ["[PSTL 731 or PSTL 732]", "at least C- in NESTEDS0"],

            # Expected output for "5651 or [Stat 5101 and 5052 and [CSCI 4041 or 2021]]"
            ["[CSCI 4041 or 2021]", "[Stat 5101 and 5052 and NESTEDS0]", "5651 or NESTEDS1"]
        ]

        # Iterate over each test case
        for i, info in enumerate(self.original):
            # Convert an info string into a list of nested substrings
            converter = self.converts[i]
            nested_ss = converter.to_nested_ss(converter._prereq_str)

            # Assert value
            assert nested_ss == expect_outputs[i], (
                f"For input '{info['info_string']}', " +
                f"expected {expect_outputs[i]}, got {nested_ss}"
            )

    def test_to_nested_code_dict(self):
        """
        This method contains tests for the to_nested_code_dict method.
        """
        # Define expected outputs for each info string from self.original
        # Skip the last case because this method only work with one string
        expected_outputs = [
            # Expected output for "1913 or 1933 or instr consent"
            {"or": ["CSCI1913", "CSCI1933"]},

            # Expected output for "at least C- in [PSTL 731 or PSTL 732]"
            {"or": ["MATH", "MATH"]},
        ]

        # Iterate over each test case
        for i in range(0, 1):
            # Convert a string into a nested code dictionary
            converter = self.converts[i]
            nested_code_dict = converter.to_nested_code_dict(
                converter._prereq_str)

            # Assert value
            assert nested_code_dict == expected_outputs[i], (
                f"For input '{converter._prereq_str}', " +
                f"expected {expected_outputs[i]}, got {nested_code_dict}"
            )

    def test_to_nested_code_dicts(self):
        """
        This method contains tests for the to_nested_code_dict method.
        """
        # Define expected outputs for each info string from self.original
        # Skip the last case because this method only work with one string
        expected_outputs = [
            # Expected output for "1913 or 1933 or instr consent"
            [{"or": ["CSCI1913", "CSCI1933"]}],

            # Expected output for "at least C- in [PSTL 731 or PSTL 732]"
            [{'or': ['MATH', 'MATH']}, {'and': ['NESTEDS0']}],

            [{'or': ['CSCI4041', 'CSCI2021']}, {
                'and': ['STAT5101', 'STAT5052', 'NESTEDS0']}, {'or': ['MATH5651', 'NESTEDS1']}]
        ]

        # Iterate over each test case
        for i in range(0, 3):
            # Convert a string into a nested code dictionary
            converter = self.converts[i]
            nested_ss = converter.to_nested_ss(converter._prereq_str)
            print(nested_ss)
            nested_code_dicts = converter.to_nested_code_dicts(nested_ss)

            # Assert value
            assert nested_code_dicts == expected_outputs[i], (
                f"For input '{converter._prereq_str}', " +
                f"expected {expected_outputs[i]}, got {nested_code_dicts}"
            )

    def test_to_combined_logic_code_dict(self):
        """
        This method contains tests for the to_combined_logic_code_dict method.
        """
        # TODO

    def test_to_logic_uid_dict(self):
        """
        This method contains tests for the to_logic_uid_dict method.
        """
        # Iterate over each test case
        for i, info in enumerate(self.original):
            # Convert ...
            converter = self.converts[i]
            nested_ss = converter.to_nested_ss(converter._prereq_str)
            nested_code_dicts = converter.to_nested_code_dicts(nested_ss)
            logic_code_dict = converter.to_combined_logic_code_dict(
                nested_code_dicts)
            logic_uid_dict = converter.to_logic_uid_dict(logic_code_dict)

            # Assert value
            assert logic_uid_dict == self.expect[i], (
                f"For input '{info['info_string']}', " +
                f"expected {self.expect[i]}, got {logic_uid_dict}"
            )
