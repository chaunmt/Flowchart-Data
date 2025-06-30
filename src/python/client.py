"""
This is the highest level where client would see.
"""

from python.sources.coursedog_report import CourseSystem, ProgramSystem

umn_id = "umn_umntc_peoplesoft"
course_sys = CourseSystem(umn_id)
program_sys = ProgramSystem(umn_id)

print(f"++ Client: Running {umn_id} CourseDog System...")
print(course_sys.record_courses())
print(f"++ Client: Finished.")