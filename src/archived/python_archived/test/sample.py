"""
Sample file to test methods and classes.
"""

from python_archived.helper.checker.course_checker import CourseChecker
from python_archived.helper.course_info_splitter import CourseInfoSplitter
from python_archived.helper.string_splitter import StringSplitter

print(StringSplitter.letter_and_num('CSCI3081W'))
print(CourseChecker.is_valid_suf('W'))
print(CourseInfoSplitter.to_subj_num_suf('CSCI3081W'))
print(CourseInfoSplitter.to_num_suf('CSCI3081W'))
