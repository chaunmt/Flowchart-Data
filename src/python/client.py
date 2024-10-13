"""
This is what the highest level client would see.
"""

from python.sources.api.facade import CourseDogFacade
from python.sources.api.coursedog.interface import CourseSystemInterface, ProgramSystemInterface

# facade = CourseDogFacade(CourseSystemInterface(), ProgramSystemInterface())

# print(facade.operation())

from python.sources.api.coursedog.system import FileHandler

print(FileHandler.get_school_path('umn_umntc_peoplesoft'))