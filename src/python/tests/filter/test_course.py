"""
This module contains tests for course's filter.
"""

# pylint: disable=protected-access

import pytest
from ...schema.others import StringComponent
from ...filter.course import (
    CourseInfoNonPrereqFilter,
    PrereqFilter,
    PrereqFilterDuplicate,
    PrereqFilterEmpty,
    PrereqFilterUidNotInShell,
    PrereqFilterNonUid,
    PrereqFilterRedundantNest,
    PrereqFormat
)

class TestCourseInfoNonPrereqFilter:
    """
    This class contains tests for the CourseInfoNonPrereqFilter class.
    """

    def test_process(self):
        """
        This method contains tests for the process method.
        """
        # Define test cases with expected prerequisites extracted
        test_cases = [
            ("This course covers advanced topics. Prerequisites: CSCI1101, MATH2001",
             " csci1101, math2001"),

            ("Topics include data structures. Prereq: PHYS9999",
             " phys9999"),

            ("Advanced programming. No prerequisites required.",
             " required."),

            ("Basic concepts. Recommended: ENGL1102. Prerequisite: ENGL1101.",
             " engl1101."),

            ("Preparation includes MATH1001. Prerequisites:",
             "")
        ]

        for original_str, expected_str in test_cases:
            # Initialize StringComponent
            sf = StringComponent(original_str)

            # Check filter value
            sf = CourseInfoNonPrereqFilter(sf)  # Add a filter
            s = sf.process()                    # Process all nested filters

            # Assert value
            assert s == expected_str, (
                f"Failed for original string = '{original_str}'. "
                f"Processed string = '{s}' is not the same as expected '{expected_str}'."
            )

###############################################################################
class TestPrereqFilter():
    """
    This class contains tests for the PrereqFilter class.
    """

    @classmethod
    def setup_class(cls):
        """
        Initialize some variables to help test prerequesite filters
        """
        cls.p1 = {
            "and": [
                {
                    "or": [
                        "016224"
                    ]
                },
                "002408"
            ]
        }

        cls.p2 = {
            "or": [
                "004126",
                "802476",
                "789683",
                "005036"
            ]
        }

        cls.p3 = {
            "and": [
                "016186",
                {
                    "or": [
                        "004115",
                        "004114"
                    ]
                }
            ]
        }

    ###############################################################################
    def test_init(self):
        """
        This method contains tests for the init method.
        """
        # Correct type
        pf = PrereqFilter(PrereqFormat(self.p1))
        assert pf._prereq._prereq == self.p1

        pf = PrereqFilter(PrereqFormat(self.p2))
        assert pf._prereq._prereq == self.p2

        pf = PrereqFilter(PrereqFormat(self.p3))
        assert pf._prereq._prereq == self.p3

        # Wrong type
        with pytest.raises(TypeError):
            assert PrereqFilter(self.p1)
            assert PrereqFilter(True)
            assert PrereqFilter(None)
            assert PrereqFilter("[ajsdih kfj]")
            assert PrereqFilter(["asd", "983 0s"])


    ###############################################################################
    def test_prereq(self):
        """
        This method contains tests for the prereq method.
        """
        pf = PrereqFilter(PrereqFormat(self.p1))
        assert pf.prereq._prereq == self.p1

        pf = PrereqFilter(PrereqFormat(self.p2))
        assert pf.prereq._prereq == self.p2

        pf = PrereqFilter(PrereqFormat(self.p3))
        assert pf.prereq._prereq == self.p3

    ###############################################################################
    def test_process(self):
        """
        This method contains tests for the process method.
        """
        # Helper class to decorate the return value with keys
        class KeyDecorator(PrereqFilter):
            """
            This decorator adds a key to check the nested behavior
            of PrereqFilter's process method.
            """

            def process(self):
                """
                Add a key to the return component.
                """
                return {"processed" : self._prereq.process()}

        # Initialize variables
        nestedpreq = self.p1
        pf = PrereqFormat(self.p1)

        # Check nested value
        for _ in range(1, 6):
            pf = KeyDecorator(pf)                       # Neste decorator
            p = pf.process()                            # Process all nested decorator
            nestedpreq = {"processed" : nestedpreq}     # Expected value
            assert p == nestedpreq


class TestPrereqFilterEmpty:
    """
    This class contains tests for the PrereqFilterEmpty class.
    """
    @classmethod
    def setup_class(cls):
        """
        Initialize some variables to help test prerequesite filters
        """
        # Define different test cases that follow the PrereqFormat structure
        cls.test_cases = {
            # Case 1
            "valid": {
                "original": {
                    "and": [
                        "016186",
                        {
                            "or": ["004115", "004114"]
                        }
                    ]
                },
                "expected": {
                    "and": [
                        "016186",
                        {
                            "or": ["004115", "004114"]
                        }
                    ]
                }
            },
            # Case 2
            "redundant_structure": {
                "original": {
                    "and": [
                        "016186",
                        {
                            "or": ["004115", "004114"]
                        },
                        {"and": []}  # Redundant empty entry
                    ]
                },
                "expected": {
                    "and": [
                        "016186",
                        {
                            "or": ["004115", "004114"]
                        }
                    ]
                }
            },
            # Case 3
            "nested_empty": {
                "original": {
                    "and": [
                        {"or": []},  # Nested empty "or"
                        {"and": []}  # Nested empty "and"
                    ]
                },
                "expected": {}  # Should simplify to an empty structure
            },
            # Case 4
            "complex_mixed_empty": {
                "original": {
                    "and": [
                        {
                            "or": ["004126", {}]
                        },
                        {
                            "and": [
                                "002408",
                                {"or": []}
                            ]
                        },
                        "789683"
                    ]
                },
                "expected": {
                    "and": [
                        {
                            "or": ["004126"]
                        },
                        {
                            "and": ["002408"]
                        },
                        "789683"
                    ]
                }
            }
        }

    def test_process(self):
        """
        This method contains tests for the process method.
        """
        # Iterate over each test case
        for case_name, case_data in self.test_cases.items():
            # Initialize the PrereqFormat object
            pf = PrereqFormat(case_data["original"])

            # Check nested value
            for _ in range(1, 3):
                pf = PrereqFilterEmpty(pf)      # Nest filter
                p = pf.process()                # Process all nested filters

                # Assert value
                assert p == case_data["expected"], (
                    f"Failed for case '{case_name}'." +
                    f"Processed prereq = {p} is not the same as {case_data["expected"]}."
                )

class TestPrereqFilterRedundantNest:
    """
    This class contains tests for the PrereqFilterRedundantNest class.
    """
    @classmethod
    def setup_class(cls):
        """
        Initialize some variables to help test prerequesite filters
        """
        # Define different test cases that follow the PrereqFormat structure
        cls.test_cases = {
            # Case 1
            "single_item_list": {
                "original": ["004126"],     # Single item list
                "expected": ["004126"]      # Keep 1 nest
            },
            # Case 2
            "single_item_dict": {
                "original": {"and": {"or": "004126"}},  # Single-item nested dict
                "expected": {"or": "004126"}            # Keep 1 nest
            },
            # Case 3
            "multi_level_single_item_nesting": {
                "original": {"and": [{"or": [{"and": ["004126"]}]}]},  # Multi-level nesting
                "expected": {"and": ["004126"]}  # Should flatten to the closest nest
            },
            # Case 4
            "mixed_redundant_nesting": {
                "original": {
                    "and": [
                        {
                            "or": [
                                {"and": "016224"}
                            ]
                        }
                    ]
                },
                "expected": {"and": "016224"}  # Should recursively flatten to the closest nest
            },
            # Case 5
            "already_flattened": {
                "original": {
                    "and": [
                        "016224",
                        {"or": ["004115", "004114"]}
                    ]
                },
                "expected": {
                    "and": [
                        "016224",
                        {"or": ["004115", "004114"]}
                    ]
                }  # No change expected
            }
        }

    def test_process(self):
        """
        This method contains tests for the process method.
        """
        # Iterate over each test case
        for case_name, case_data in self.test_cases.items():
            # Initialize the PrereqFormat object
            pf = PrereqFormat(case_data["original"])

            # Check nested value
            for _ in range(1, 3):
                pf = PrereqFilterRedundantNest(pf)  # Nest filter
                p = pf.process()                    # Process all nested filters

                # Assert value
                assert p == case_data["expected"], (
                    f"Failed for case '{case_name}'." +
                    f"Processed prereq = {p} is not the same as {case_data["expected"]}."
                )

class TestPrereqFilterDuplicate:
    """
    This class contains tests for the PrereqFilterDuplicate class.
    """
    @classmethod
    def setup_class(cls):
        """
        Initialize some variables to help test prerequesite filters
        """
        # Define different test cases that follow the PrereqFormat structure
        cls.test_cases = {
            # Case 1
            "simple_duplicates_in_list": {
                "original": ["004126", "004126", "802476"],
                "expected": ["004126", "802476"]
            },
            # Case 2
            "nested_duplicates_in_lists": {
                "original": {
                    "and": [
                        {"or": ["016224", "016224"]},
                        "002408",
                        "002408"
                    ]
                },
                "expected": {
                    "and": [
                        {"or": ["016224"]},
                        "002408"
                    ]
                }
            },
            # Case 3
            "mixed_structure_with_duplicates": {
                "original": {
                    "and": [
                        "016224",
                        {"or": ["004126", "004126"]},
                        "016224"
                    ],
                    "or": [
                        "789683",
                        "789683",
                        "005036"
                    ]
                },
                "expected": {
                    "and": [
                        "016224",
                        {"or": ["004126"]}
                    ],
                    "or": [
                        "789683",
                        "005036"
                    ]
                }
            },
            # Case 4
            "duplicates_separated_by_nests": {
                "original": {
                    "and": [
                        "016224",
                        {"or": ["004126", "004126", "789683"]},
                        "016224"
                    ],
                    "or": [
                        "789683",
                        "005036"
                    ]
                },
                "expected": {
                    "and": [
                        "016224",
                        {"or": ["004126", "789683"]}    # Different nests are different horizons
                    ],
                    "or": [
                        "789683",   # Both duplicates are kept
                        "005036"
                    ]
                }
            },
            # Case 5
            "already_unique_structure": {
                "original": {
                    "and": [
                        "016224",
                        {"or": ["004126", "789683"]}
                    ],
                    "or": [
                        "005036"
                    ]
                },
                "expected": {
                    "and": [
                        "016224",
                        {"or": ["004126", "789683"]}
                    ],
                    "or": [
                        "005036"
                    ]
                }  # Should remain unchanged
            }
        }

    def test_process(self):
        """
        This method contains tests for the process method.
        """
        # Iterate over each test case
        for case_name, case_data in self.test_cases.items():
            # Initialize the PrereqFormat object
            pf = PrereqFormat(case_data["original"])

            # Check nested value
            for _ in range(1, 3):
                pf = PrereqFilterDuplicate(pf)  # Nest filter
                p = pf.process()                    # Process all nested filters

                # Assert value
                assert p == case_data["expected"], (
                    f"Failed for case '{case_name}'." +
                    f"Processed prereq = {p} is not the same as {case_data["expected"]}."
                )


class TestPrereqFilterNonUid:
    """
    This class contains tests for the PrereqFilterNonUid class.
    """
    @classmethod
    def setup_class(cls):
        """
        Initialize some variables to help test prerequesite filters
        """
        # Define different test cases that follow the PrereqFormat structure
        cls.test_cases = {
            # Case 1
            "mixed_uid_non_uid_in_list": {
                "original": ["004126", "ABC101", "802476", "CourseName", 123],
                "expected": ["004126", "802476"]  # Only numeric strings remain
            },
            # Case 2
            "nested_structures_with_non_uids": {
                "original": {
                    "and": [
                        {"or": ["016224", "non-uid", "12345"]},
                        "002408",
                        "non-uid-text"
                    ]
                },
                "expected": {
                    "and": [
                        {"or": ["016224", "12345"]},
                        "002408"
                    ]
                }
            },
            # Case 3
            "all_non_uids": {
                "original": {
                    "and": [
                        "CourseABC", "non-numeric", {"or": ["not-a-uid"]},
                        {"and": ["NonUIDValue"]}
                    ]
                },
                "expected": {'and': [{'or': []}, {'and': []}]}
            },
            # Case 4
            "mixed_structure_with_nested_non_uids": {
                "original": {
                    "and": [
                        "016224",
                        {"or": ["004126", "Text123", "789683"]},
                        "InvalidString"
                    ],
                    "or": [
                        "not-a-uid",
                        "005036",
                        123
                    ]
                },
                "expected": {
                    "and": [
                        "016224",
                        {"or": ["004126", "789683"]}
                    ],
                    "or": [
                        "005036"
                    ]
                }
            },
            # Case 5
            "already_valid_structure": {
                "original": {
                    "and": [
                        "016224",
                        {"or": ["004126", "789683"]}
                    ],
                    "or": [
                        "005036"
                    ]
                },
                "expected": {
                    "and": [
                        "016224",
                        {"or": ["004126", "789683"]}
                    ],
                    "or": [
                        "005036"
                    ]
                }  # Should remain unchanged
            }
        }

    def test_process(self):
        """
        This method contains tests for the process method.
        """
        # Iterate over each test case
        for case_name, case_data in self.test_cases.items():
            # Initialize the PrereqFormat object
            pf = PrereqFormat(case_data["original"])

            # Check nested value
            for _ in range(1, 3):
                pf = PrereqFilterNonUid(pf)  # Nest filter
                p = pf.process()                    # Process all nested filters

                # Assert value
                assert p == case_data["expected"], (
                    f"Failed for case '{case_name}'." +
                    f"Processed prereq = {p} is not the same as {case_data["expected"]}."
                )

class TestPrereqFilterUidNotInShell:
    """
    This class contains tests for the PrereqFilterUidNotInShell class.
    """
    @classmethod
    def setup_class(cls):
        """
        Initialize some variables to help test prerequesite filters
        """
        # Define course shells for this test
        cls.shells = {
            "004137": {
                "uid": "004137",
                "code": "CHEM4352",
                "subject": "CHEM",
                "number": "4352",
                "honors": False
            },
            "004139": {
                "uid": "004139",
                "code": "CHEM4361",
                "subject": "CHEM",
                "number": "4361",
                "honors": False
            },
            "004142": {
                "uid": "004142",
                "code": "CHEM4411",
                "subject": "CHEM",
                "number": "4411",
                "honors": False
            },
            "004144": {
                "uid": "004144",
                "code": "CHEM4412",
                "subject": "CHEM",
                "number": "4412",
                "honors": False
            }
        }

        # Define different test cases that follow the PrereqFormat structure
        cls.test_cases = {
            # Case 1
            "mixed_valid_and_invalid_uids": {
                "original": ["004137", "002222", "004100", "004142"],
                "expected": ["004137", "004142"]  # Only UIDs in the provided course shells remain
            },
            # Case 2
            "nested_structure_with_invalid_uids": {
                "original": {
                    "and": [
                        {"or": ["004139", "101102", "SPEC300"]},
                        "004144",
                        "005500"  # Not in the provided course shells
                    ]
                },
                "expected": {
                    "and": [
                        {"or": ["004139"]},
                        "004144"
                    ]
                }
            },
            # Case 3
            "all_invalid_uids": {
                "original": {
                    "and": [
                        "101101", "202202", {"or": ["301103"]},
                        {"and": ["301301"]}
                    ]
                },
                "expected": {
                    "and": [
                        {"or": []},
                        {"and": []}
                    ]
                }
            },
            # Case 4
            "already_valid_structure": {
                "original": {
                    "and": [
                        "004137",
                        {"or": ["004139", "004142"]}
                    ],
                    "or": [
                        "004144"
                    ]
                },
                "expected": {
                    "and": [
                        "004137",
                        {"or": ["004139", "004142"]}
                    ],
                    "or": [
                        "004144"
                    ]
                }  # Should remain unchanged
            }
        }

    def test_process(self):
        """
        This method contains tests for the process method.
        """
        # Iterate over each test case
        for case_name, case_data in self.test_cases.items():
            # Initialize the PrereqFormat object
            pf = PrereqFormat(case_data["original"])

            # Check nested value
            for _ in range(1, 3):
                pf = PrereqFilterUidNotInShell(pf, self.shells)     # Nest filter
                p = pf.process()                                    # Process all nested filters

                # Assert value
                assert p == case_data["expected"], (
                    f"Failed for case '{case_name}'." +
                    f"Processed prereq = {p} is not the same as {case_data["expected"]}."
                )
