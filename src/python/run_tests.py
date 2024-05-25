"""
This file creates a test suites from test files in ./Test to run.
"""
import unittest

# Import test cases.

from Test.test_new_types import TestNewTypes

from Test.test_string_checker import TestStringChecker
from Test.test_string_splitter import TestStringSplitter
from Test.test_course_checker import TestCourseChecker

from Test.test_string_filter import TestStringFilter
from Test.test_course_filter import TestCourseFilter
from Test.test_prereq_filter import TestPrereqFilter

###############################################################################
# Create a test suite.
suite = unittest.TestSuite()

# Add specific test cases to the suite.

suite.addTest(unittest.makeSuite(TestNewTypes))

suite.addTest(unittest.makeSuite(TestStringChecker))
suite.addTest(unittest.makeSuite(TestStringSplitter))
suite.addTest(unittest.makeSuite(TestCourseChecker))

suite.addTest(unittest.makeSuite(TestStringFilter))
suite.addTest(unittest.makeSuite(TestCourseFilter))
suite.addTest(unittest.makeSuite(TestPrereqFilter))

# You can also add specific s if needed.

# suite.addTest(TestNewTypes('test_course_shell'))

###############################################################################
# Run the test suite.
runner = unittest.TextTestRunner()
runner.run(suite)
