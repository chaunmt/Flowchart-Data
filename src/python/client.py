"""
This is what the highest level where client would see.
"""

from python.sources.api.facade import CourseDogFacade
from python.sources.api.coursedog.interface import CourseSystemInterface, ProgramSystemInterface

facade = CourseDogFacade(CourseSystemInterface(), ProgramSystemInterface())

print(facade.operation())
