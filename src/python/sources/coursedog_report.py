"""
Classes to help handle Course Dog's Report.
"""
import copy

from python.sources.format import JSONHandler
from python.sources.coursedog import SubjectHandler
from python.checker.course import CourseChecker
from python.splitter.course import CourseInfoSplitter
from python.schema.definitions import PrereqFormat
from python.extractor.course import PrereqExtractor
from python.filter.course import PrereqFilterUidNotInShell

class CourseSystem(SubjectHandler):
    _ALL_COURSES_KEY = "allCourses"
    
    def __init__(self, school_id: str) -> None:
        super().__init__(school_id)

    def record_courses(self) -> str:
        coursepath = self.school.course_path
        
        courses = self.get_courses()
        JSONHandler.write_to_path(f"{coursepath}/{self._ALL_COURSES_KEY}.json", courses)
        
        general_courses = {}
        honors_courses = {}
        for cid, course in courses.items():
            if course["honors"]:
                honors_courses[cid] = copy.deepcopy(course)
            else:
                general_courses[cid] = copy.deepcopy(course)
            
        
        general_courses = self.get_general_courses(courses, general_courses)
        JSONHandler.write_to_path(f"{coursepath}/{self.school.general_key}.json", general_courses)
        
        honors_courses = self.get_honors_courses(courses, honors_courses)
        JSONHandler.write_to_path(f"{coursepath}/{self.school.honors_key}.json", honors_courses)
        
        return "++ CourseSystem: All courses data written successfully!"

    def get_honors_courses(self, courses: dict, honor_courses: dict):
        """
        Get courses that are either an honors course or have an honors course as their prerequisites.
        """
        res = {}
        for cid, course in courses.items():
            if course["honors"]:
                res[cid] = course
            else:
                p = PrereqFormat(course["prereq"])
                p = PrereqFilterUidNotInShell(p, honor_courses)
                p = PrereqExtractor.post_processing(p)
                
                if p:
                    res[cid] = course
            
        return res

    def get_general_courses(self, courses: dict, general_courses: dict):
        """
        Get a non-honors (general) courses, excluding their honors prerequisites.
        """
        for _, course in general_courses.items():
            p = PrereqFormat(course["prereq"])
            p = PrereqFilterUidNotInShell(p, general_courses)
            p = PrereqExtractor.post_processing(p)
            course["prereq"] = p
        
        return general_courses

    def get_courses(self) -> dict:
        shells = self.get_courseshells()
        
        courses = {}
        size = len(shells)
        interval = size // 100
        for i, cid in enumerate(shells):
            course = shells[cid]
            
            # Get prerequisites
            prereq = PrereqExtractor(course["info"], course["subject"], shells)
            prereq.extract()
            prereq = prereq.get_prereq()
            course["prereq"] = prereq  # Add a new field
            
            courses[cid] = course
            
            # Print progress
            if i % interval == 0:
                print(f"++ CourseSystem: {int(100 * i / size)}%")
        
        return courses

    def get_courseshells(self) -> dict:
        unique_field_vals = JSONHandler.get_from_path(self.school.unique_field_vals_path)
        shells = {}

        for course in self._all_courses_list:
            number, suffix = CourseInfoSplitter.split_num_suf(course["Course number"]) 
            
            libeds = self.get_valid_unique_vals(
                course["Twin Cities: Approved Liberal Education Requirement(s)"],
                unique_field_vals["Twin Cities: Approved Liberal Education Requirement(s)"]
            )
            attributes = self.get_valid_unique_vals(
                course["Course attributes"],
                unique_field_vals["Course attributes"]
            )
        
            # Map client's field to Coursedog report's field
            shells[course["PeopleSoft course ID"]] = {
                "id": course["PeopleSoft course ID"],
                "code": course["Code"],
                "subject": course["Course subject code"],
                "number": number,
                "honors": CourseChecker.is_honors_suf(suffix),
                "writing": course["Twin Cities: This course is approved as Writing Intensive"] == "Yes",
                "name": course["Course name"],
                "attribute": attributes,
                "libed": libeds,
                "info": course["Course description"]
            }
        
        return shells

    def get_valid_unique_vals(self, s: str, l: list[str]) -> list[str]:
        """
        Get all unique values from s that exists in l.
        """
        valids = set()
        for v in l:
            if v in s:
                valids.add(v)
        
        return list(valids) if len(valids) > 0 else None

class ProgramSystem:
    def __init__(self, school_id: str = None) -> None:
        pass
