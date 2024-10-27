"""
Unit tests for the course information splitting functionality in the CourseInfoSplitter class.
This module tests various methods that split course code strings into components
such as subject, number, and suffix. The tests cover different input scenarios including
valid course codes, edge cases, and invalid inputs to
ensure the correct behavior of the splitting logic.
"""

import pytest
from ...splitter.course import CourseInfoSplitter

class TestCourseInfoSplitter:
    """
    This class contains unit tests for the CourseInfoSplitter class.
    """

    def test_code_into_subj_num_suf(self):
        """
        Tests the code_into_subj_num_suf method of the CourseInfoSplitter class.
        """
        # Valid course code with subject, number, and suffix
        assert CourseInfoSplitter.code_into_subj_num_suf("TH1101W") == ["TH", "1101", "W"]
        # Valid course code with subject and number only
        assert CourseInfoSplitter.code_into_subj_num_suf("CSCI1001") == ["CSCI", "1001", ""]
        # Invalid course code with no number
        assert CourseInfoSplitter.code_into_subj_num_suf("CSCI") == ["", "", ""]
        # Invalid course code with invalid subject
        assert CourseInfoSplitter.code_into_subj_num_suf("1001W") == ["", "", ""]
        # Invalid course code with invalid number
        assert CourseInfoSplitter.code_into_subj_num_suf("CSCINUM") == ["", "", ""]

        # Testing test_code_into_subj_num_suf - Invalid course code with no number
        # This test passes with the current functionality
        assert CourseInfoSplitter.code_into_subj_num_suf("CSCI") == ["", "", ""]


        # Course code with special characters, expect valid splits
        assert CourseInfoSplitter.code_into_subj_num_suf("TH-1101W") == ["TH", "1101", "W"]
        # Course code with spaces, expect valid splits
        assert CourseInfoSplitter.code_into_subj_num_suf("TH 1101 W") == ["TH", "1101", "W"]
        # Course code with mixed case
        assert CourseInfoSplitter.code_into_subj_num_suf("tH1101w") == ["TH", "1101", "W"]


    def test_split_num_suf(self):
        """
        Tests the split_num_suf method of the CourseInfoSplitter class.
        """
        # Valid number and suffix
        assert CourseInfoSplitter.split_num_suf("1001H") == ["1001", "H"]
        # Valid number only
        assert CourseInfoSplitter.split_num_suf("1001") == ["1001", ""]
        # Invalid number
        assert CourseInfoSplitter.split_num_suf("NUM") == [None, None]
        # Invalid number with valid suffix
        assert CourseInfoSplitter.split_num_suf("NUMW") == [None, None]

        # Number with special characters, should still return valid splits
        assert CourseInfoSplitter.split_num_suf("1001-W") == ["1001", "W"]
        # Number with spaces, should still return valid splits
        assert CourseInfoSplitter.split_num_suf("1001 W") == ["1001", "W"]
        # Number with mixed case suffix
        assert CourseInfoSplitter.split_num_suf("1001w") == ["1001", "W"]
