"""
This module contains tests for course related checkers.
"""

import pytest
from ...checker.course import (
    CourseInfoChecker,
    CourseChecker,
    PrereqChecker,
    Course,
    CourseShell,
    PrereqFormat
)

class TestCourseInfoChecker:
    """
    This class contains tests for the CourseInfoChecker class.
    """

    def test_is_writing_suf(self):
        """
        This method contains tests for the is_writing_suf method.
        """
        assert CourseInfoChecker.is_writing_suf("W") == True
        assert CourseInfoChecker.is_writing_suf("V") == True
        assert CourseInfoChecker.is_writing_suf("H") == False
        assert CourseInfoChecker.is_writing_suf("") == False

    def test_is_honors_suf(self):
        """
        This method contains tests for the is_honors_suf method.
        """
        assert CourseInfoChecker.is_honors_suf("H") == True
        assert CourseInfoChecker.is_honors_suf("V") == True
        assert CourseInfoChecker.is_honors_suf("W") == False
        assert CourseInfoChecker.is_honors_suf("") == False

    def test_is_valid_subj(self):
        """
        This method contains tests for the is_valid_subj method.
        """
        assert CourseInfoChecker.is_valid_subj("AAS") == True
        assert CourseInfoChecker.is_valid_subj("CSCI") == True
        assert CourseInfoChecker.is_valid_subj("HISTO") == False
        assert CourseInfoChecker.is_valid_subj("") == False

    def test_is_valid_num(self):
        """
        This method contains tests for the is_valid_num method.
        """
        assert CourseInfoChecker.is_valid_num("1101") == True
        assert CourseInfoChecker.is_valid_num("0999") == False
        assert CourseInfoChecker.is_valid_num("abcd") == False
        assert CourseInfoChecker.is_valid_num("") == False
        assert CourseInfoChecker.is_valid_num(None) == False

    def test_is_valid_suf(self):
        """
        This method contains tests for the is_valid_suf method.
        """
        assert CourseInfoChecker.is_valid_suf("W") == True
        assert CourseInfoChecker.is_valid_suf("H") == True
        assert CourseInfoChecker.is_valid_suf("V") == True
        assert CourseInfoChecker.is_valid_suf("") == True
        assert CourseInfoChecker.is_valid_suf("A") == False


class BareTestCases:
    """
    Base class to provide shared test data for Course and Prereq tests.
    """

    @classmethod
    def setup_class(cls):
        """
        Initialize some test case variables.
        """

        # Create CourseShell objects for testing
        cls.shells = {
            "002189": CourseShell(
                uid_ = "002189",
                code_ = "CSCI4011",
                subject_ = "CSCI",
                number_ = "4011",
                honors_ = False
            ),
            "810347": CourseShell(
                uid_ = "810347",
                code_ = "CSCI2041",
                subject_ = "CSCI",
                number_ = "2041",
                honors_ = False
            ),
            "798385": CourseShell(
                uid_ = "798385",
                code_ = "ACCT2051H",
                subject_ = "ACCT",
                number_ = "2051",
                honors_ = True
            )
        }

        # Create Course objects for testing
        cls.courses = {
            "002189": Course(
                uid_= "002189",
                code_ = "CSCI4011",
                subject_ = "CSCI",
                number_ = "4011",
                honors_ = False,
                writing_ = False,
                name_ = "Form Lang & Autom.",
                fullname_ = "Formal Languages and Automata Theory",
                info_ = "Logical/mathematical...",
                prereq = {
                    "or": [
                        "810347"
                    ]
                }
            ),
            "810347": Course(
                uid_= "810347",
                code_ = "CSCI2041",
                subject_ = "CSCI",
                number_ = "2041",
                honors_ = False,
                writing_ = False,
                name_ = "Adv. Programming Principles",
                fullname_ = "Advanced Programming Principles",
                info_ = "Principles/techniques...",
                prereq = {
                    "and": [
                        {
                            "or": [
                                "809667",
                                "810346"
                            ]
                        },
                        "003672"
                    ]
                }
            ),
            "798385": Course(
                uid_= "798385",
                code_ = "ACCT2051H",
                subject_ = "ACCT",
                number_ = "2051",
                honors_ = True,
                writing_ = False,
                name_ = "Honors:  Intr Financial Rptg",
                fullname_ = "Honors: Introduction to Financial Reporting",
                info_ = "This course introduces...",
                prereq = {}
            )
        }

class TestCourseChecker(BareTestCases):
    """
    This class contains tests for the CourseChecker class.
    """

    def test_is_equal(self):
        """
        This method contains tests for the is_equal method.
        """

        # Test equality for CourseShell objects
        assert CourseChecker.is_equal(self.shells["002189"], self.shells["002189"]) is True
        assert CourseChecker.is_equal(self.shells["002189"], self.shells["810347"]) is False
        assert CourseChecker.is_equal(self.shells["810347"], self.shells["798385"]) is False

        # Test equality for Course objects
        assert CourseChecker.is_equal(self.courses["002189"], self.courses["002189"]) is True
        assert CourseChecker.is_equal(self.courses["002189"], self.courses["810347"]) is False
        assert CourseChecker.is_equal(self.courses["810347"], self.courses["798385"]) is False

        # Test equality across types
        assert CourseChecker.is_equal(self.shells["002189"], self.courses["002189"]) is False

        # Test invalid comparisons
        with pytest.raises(ValueError):
            CourseChecker.is_equal(None, self.shells["002189"])
            CourseChecker.is_equal(self.shells["002189"], "CSCI 4041")
            CourseChecker.is_equal("CSCI 2041", 1039)

class TestPrereqChecker(BareTestCases):
    """
    This class contains tests for the PrereqChecker class.
    """

    def test_has_shared_uid(self):
        """
        This method contains tests for the has_shared_uid method.
        """
        # Test with shared UIDs
        prereq1 = PrereqFormat(["002189", "810347"])
        assert PrereqChecker.has_shared_uid(prereq1.process(), self.shells) is True

        # Test with nested logical operators and shared UIDs
        prereq2 = PrereqFormat({"and": ["810347", {"or": ["798385", "999999"]}]})
        assert PrereqChecker.has_shared_uid(prereq2.process(), self.shells) is True

        # Test with no shared UIDs
        prereq3 = PrereqFormat(["123456", {"or": ["654321", "111111"]}])
        assert PrereqChecker.has_shared_uid(prereq3.process(), self.shells) is False

        # Test with empty prerequisites
        prereq4 = PrereqFormat({})
        assert PrereqChecker.has_shared_uid(prereq4.process(), self.shells) is False

        # Test with a mix of valid and invalid UIDs
        prereq5 = PrereqFormat(["002189", "654321", {"and": ["810347", "888888"]}])
        assert PrereqChecker.has_shared_uid(prereq5.process(), self.shells) is True
