"""
Classes to help handle Course Dog's API.
"""

import copy

from python.sources.format import JSONHandler
from python.checker.course import CourseChecker, PrereqChecker
from python.splitter.course import CourseInfoSplitter
from python.extractor.course import PrereqExtractor
from python.filter.course import PrereqFilterNonGeneralUid
from python.schema.course import PrereqFormat
from python.sources.config.school import SchoolConfigManager

class CourseSystem:
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

        # Initialize an object to handle the school"s subjects
        self._subject_handler  = SubjectHandler(
            JSONHandler.get_from_path(
                f"{self._data_path}/allSubjects.json"
            ),
            self._data_path
        )

    def record_all_courses(self, is_honors: bool, subject: str = _ALL_COURSE_KEY):
        """
        Record all courses of a certain type (general, honors) and subject.\n
        If no subject is passed, record all subjects.
        """
        # TODO record_all_courses(is_honors: bool) first
        # TODO get data from the corresponding file (general.json or honors.json)
        # TODO get only data of a specified subject
        # TODO record the data we get into specific subject json file

    def record_all_shells_and_courses(self) -> None:
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
        print(">>>>>> Course data written successfully!")
        
        # Finally, invoke the subject handler
        self._subject_handler.record_all_subj_uids(all_courses_shells)

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
                prereq = PrereqFilterNonGeneralUid(
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

    def get_api_input(self, subject_code: str = "", limit: str = _API_LIMIT) -> list:
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

class SubjectHandler():
    """
    # TODO
    """

    def __init__(self, all_subjs: dict, data_path):
        self._all_subjects = all_subjs
        self._data_path = data_path

    def record_all_subj_uids(self, courses) -> None:
        """
        Record all subjects' course uids to the subject file.\n
        `data` should be a dictionary mapping uids to Courses or CourseShells\n
        See `self.get_all_subj_uids()`
        """
        # Get the mapping from subject to num->uid dict
        print(">>>>>> Generating course number to uid maps for subjects...")
        subj_lists = self.get_all_subj_uids(courses)
        print(">>>>>> Successfully mapped course numbers to uids!")
        # Define file path and write to it
        filename = "subject_uids.json"
        JSONHandler.write_to_path(f"{self._data_path}/{filename}", subj_lists)
        print(">>>>>> Subject maps written successfully!")

    def get_subj_uids(self, subj: str, courses) -> list[str]:
        """
        Get a mapping of the subject's course numbers to uids from data.\n
        If you're fetching many, consider using `get_all_subj_uids()` instead\n
        `data` should be a dictionary mapping uids to Courses or CourseShells
        """
        return self.get_all_subj_uids(courses).get(subj)

    def get_all_subj_uids(self, courses) -> dict[str, dict[str, str]]:
        """
        Get a dict with subject as key and number->uid dict as value from data.\n
        `data` should be a dictionary mapping uids to Courses or CourseShells
        """
        if isinstance(courses, dict):
            courses = courses.values()
        failed = []
        # Create empty dicts for each subject
        mapping = { subj: {} for subj in self._all_subjects }
        for course in courses:
            uid = course["uid"]
            num = course["number"]
            subj = course["subject"]
            subj_map = mapping.get(subj)
            if subj_map is None:
                # failed.append((subj, num))
                pass
            else:
                subj_map[num] = uid
        # print(", ".join(failed))
        return mapping

class ProgramSystem:
    """
    # TODO
    """
