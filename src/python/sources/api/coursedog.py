"""
Classes to help handle Course Dog's API.
"""

import copy

from python.sources.format import JSONHandler
from python.checker.course import CourseChecker, PrereqChecker
from python.splitter.course import CourseInfoSplitter
from python.extractor.course import PrereqExtractor
from python.filter.course import PrereqFilterUidNotInShell
from python.schema.course import PrereqFormat
from python.sources.config.school import SchoolConfigManager

class SystemConfig():
    """
    Configuration for Course Dog's API system.
    """

    def __init__(self, school_uid: str = None):
        """
        Initalize a SystemConfig object.
        """
        # Stored school uid
        self._school_uid = school_uid

        # Stored necessary data info and paths
        config = SchoolConfigManager(school_uid)
        self._school_key = config.get_school_key()
        self._data_path = config.get_data_path()
        self._course_path = config.get_course_path()
        self._program_path = config.get_program_path()
        self._general_key = config.get_general_key()
        self._honors_key = config.get_honors_key()

class SubjectHandler(SystemConfig):
    """
    Handling Course Dog's API works for Subjects.
    """

    def __init__(self, school_uid: str = None):
        """
        Initalize a SubjectHandler object.
        """
        super().__init__(school_uid)
        self._all_subjects = JSONHandler.get_from_path(f"{self._data_path}/allSubjects.json")

    def record_all_subj(self) -> None:
        """
        Record all subjects' code and name of the school.
        """
        # TODO
        
        return "++ SubjectHandler: All subjects data written successfully!"

    def record_all_subj_num_uids(self) -> None:
        """
        Record all subject's num->uid maps to a json file.\n
        EX:
        {
            "AAS": {
                "1101": "797460",
                "1201": "803713"
            }
        }
        """
        # Get the mapping from subject to num->uid dict
        print(">>>>>> Generating course number to uid maps for subjects...")
        subj_lists = self.get_all_subj_num_uids(
            JSONHandler.get_from_path(f"{self._course_path}/{self._ALL_COURSE_KEY}Shells.json")
        )
        print(">>>>>> Successfully mapped course numbers to uids!")
        
        # Define file path and write to it
        filename = "subjectUidMaps.json"
        JSONHandler.write_to_path(f"{self._data_path}/{filename}", subj_lists)
        print(">>>>>> Subject maps written successfully!")
        
        return "++ SubjectHandler: All subjects' num->uid maps data written successfully!"

    def get_all_subj_num_uids(self, courses) -> dict:
        """
        Get a dictionary with subject as key and subject's num->uid maps as value from data.
        """
        if isinstance(courses, dict):
            courses = courses.values()

        # Create empty dicts for each subject
        mapping = { subj: {} for subj in self._all_subjects }
        for course in courses:
            # Get necessary data
            uid = course["uid"]
            num = course["number"]
            subj = course["subject"]
            subj_map = mapping.get(subj)

            # Map a subject's course number to its uid
            if subj_map is not None:
                subj_map[num] = uid

        return mapping

    def get_all_subjs(self) -> dict:
        """
        Get all subjects' code and name of the school.
        """
        # TODO

class CourseSystem(SubjectHandler):
    """
    Handling Course Dog's API works for Courses.
    """
    # Course Dog's API variables
    _ALL_COURSE_KEY = "allCourses"
    _API_RETURN_FIELDS = ",".join([
        "institutionId",
        "code",
        "subjectCode",
        "courseNumber",
        "name",
        "longName",
        "description",
    ])
    _API_LIMIT = "infinity"

    def __init__(self, school_uid: str = None) -> None:
        """
        Initalize a CourseSystem object.
        """
        super().__init__(school_uid)

    def record_all_courses(self, is_honors: bool, subject: str = _ALL_COURSE_KEY):
        """
        Record all courses of a certain type (general, honors) and subject.\n
        If no subject is passed, record all subjects.
        """
        # TODO record_all_courses(is_honors: bool) first
        # TODO get data from the corresponding file (general.json or honors.json)
        # TODO get only data of a specified subject
        # TODO record the data we get into specific subject json file

        return "++ CourseSystem: All courses data written successfully!"
    
    def record_all_shells_and_courses(self) -> str:
        """
        Record all courses of a certain type (general, honors, or either).
        """
        # Get raw input data from the API.
        raw = self.get_api_input()
        print(">>>>>> Got raw data!")

        # Get all courses shells and full data
        all_courses_shells = self.get_all_course_shells(raw)
        print(">>>>>> Got all courses shells data!")

        all_courses = self.get_all_courses(raw)
        print(">>>>>> Got all courses data!")

        # Get general courses shells and full data
        general_shells = self.get_all_course_shells(raw, False)
        print(">>>>>> Got general shells data!")

        general_courses = self.get_general_courses(general_shells, all_courses)
        print(">>>>>> Got general courses data!")

        # Honors courses structure is a little more complicated than other types.
        # Our honors.json and honorsShells.json need to include all courses
        # that need honors courses info ==> any honors related courses.
        # An honors related course is one that is either:
        # -- A courses of type honors (is_honors = True).
        # -- A courses with at least 1 honors course as its prereq.
        honors_courses = self.get_honors_courses(
            self.get_all_course_shells(raw, True), all_courses
        )
        print(">>>>>> Got honors courses data!")

        honors_shells = self.get_course_shell_data(honors_courses)
        print(">>>>>> Got honors shells data!")

        # Define full file paths and data to write into
        data_to_write = [
            (f"{self._ALL_COURSE_KEY}Shells.json", all_courses_shells),
            (f"{self._general_key}Shells.json", general_shells),
            (f"{self._honors_key}Shells.json", honors_shells),
            (f"{self._ALL_COURSE_KEY}.json", all_courses),
            (f"{self._general_key}.json", general_courses),
            (f"{self._honors_key}.json", honors_courses)
        ]

        # Write shells and courses data to path
        for file_name, data in data_to_write:
            JSONHandler.write_to_path(f"{self._course_path}/{file_name}", data)
            
        return "++ CourseSystem: All courses and shells data written successfully!"

    def get_honors_courses(self, honors_only_shells: dict, all_courses: dict):
        """
        Get all honors courses.
        """
        # Get honors courses
        honors_courses = {}
        for uid in all_courses:
            # If the course exists in honors only shells then it's an honors course
            if uid in honors_only_shells:
                honors_courses[uid] = all_courses[uid]
            else:
                # Get the course's prerequisites
                p = all_courses[uid]
                p = p["prereq"]

                if PrereqChecker.has_shared_uid(p, honors_only_shells):
                    honors_courses[uid] = all_courses[uid]

        return honors_courses

    def get_general_courses(self, general_shells: dict, all_courses: dict):
        """
        Get all general courses.
        """
        # Get honors courses
        general_courses = {}
        for uid in all_courses:
            # If the course exists in general shells then it's a general course
            if uid in general_shells:
                # Make a completely separate clone
                c =  copy.deepcopy(all_courses[uid])

                # Filter non general uids out of the course's prereq
                prereq = PrereqFormat(c["prereq"])
                prereq = PrereqFilterUidNotInShell(
                    prereq,
                    general_shells
                )
                prereq = prereq.process()
                c["prereq"] = prereq

                general_courses[uid] = c

        return general_courses

    def get_course_shell_data(self, courses: dict):
        """
        Get course shell data from a course.
        """
        shells = {}
        for uid, course in courses.items():  # Iterate over key-value pairs
            shells[uid] = {
                "uid": course["uid"],        # Access course details
                "code": course["code"],
                "subject": course["subject"],
                "number": course["number"],
                "honors": course["honors"]
            }
        return shells

    def get_api_input(self, subject_code: str = "", limit: str = _API_LIMIT) -> dict:
        """
        Get the API result for certain courses.
        """
        raw = JSONHandler.get_from_url(
            'https://app.coursedog.com/api/v1/cm/'  # API
            + self._school_uid
            + '/courses/search/$filters?'  # Search courses
            + 'subjectCode=' + subject_code
            + '&returnFields=' + self._API_RETURN_FIELDS
            + '&limit=' + limit
        )
        return raw["data"]

    def get_all_courses(
        self,
        raw_data: dict = None
    ) -> dict:
        """
        Get a dictionary of all courses.
        """
        # Get raw input data
        if raw_data is None:
            raw_data = self.get_api_input()

        # Get all related courses
        data = {}
        length = len(raw_data)
        interval = length // 100
        counter = 0
        for course in raw_data:
            # Split a course's number and its suffix
            number, suffix = CourseInfoSplitter.split_num_suf(course['courseNumber'])

            # Check course's type
            honors = CourseChecker.is_honors_suf(suffix)
            writing = CourseChecker.is_writing_suf(suffix)

            # Process info string into a logical dictionary of prerequisite courses
            prereq = PrereqExtractor(
                course['description'],
                course['subjectCode'],
                self._school_uid
            )
            prereq.extract()
            prereq = prereq.get_prereq()

            data[course['institutionId']] = {
                'uid' : course['institutionId'],
                'code' : course['code'],
                'subject' : course['subjectCode'],
                'number' : number,
                'honors' : honors,
                'writing' : writing,
                'name' : course['name'],
                'fullname' :  course['longName'],
                'info' : course['description'],
                'prereq' : prereq
            }

            # Checking the progress
            counter += 1
            if counter % interval == 0:
                print(f"Progress: {counter * 100 // length}%")

        return data

    def get_all_course_shells(self, data: dict = None, is_honors: bool = None) -> dict:
        """
        Get all CourseShell objects of a certain type (honors, general, either)
        from the raw data and map them by uid.\n
        (A CourseShell is a Course object without prereq information).\n
        EX: {
        "797460" : {
            "uid": "797460",
            "code": "AAS1101",
            "subject": "AAS",
            "number": "1101",
            "honors": false
        }}
        """
        # Get raw data input of all courses
        if data is None:
            data = self.get_api_input()

        # Get course shells
        shells = {}
        for course in data:
            # Split a course's number and its suffix
            number, suffix = CourseInfoSplitter.split_num_suf(course["courseNumber"])

            # Check course's type
            honors = CourseChecker.is_honors_suf(suffix)

            # Only get shells of a certain type
            if is_honors is None or honors == is_honors:
                # Map value to corresponding key
                shells[course["institutionId"]] = {
                    "uid" : course["institutionId"],
                    "code" : course["code"],
                    "subject" : course["subjectCode"],
                    "number" : number,
                    "honors" : honors
                }

        return shells

class ProgramSystem:
    """
    # TODO
    """
    
    def __init__(self, school_uid: str = None) -> None:
        pass
