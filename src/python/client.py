"""
This is what the highest level where client would see.
"""

from python.sources.api.facade import CourseDogFacade
from python.sources.api.coursedog import CourseSystem, ProgramSystem

school_uids = ["umn_umntc_peoplesoft"]

for id in school_uids:
    print(f"++ Client: Running {id} CourseDog System...")
    facade = CourseDogFacade(CourseSystem(id), ProgramSystem(id))

print(facade.operation())
