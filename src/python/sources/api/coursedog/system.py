"""
Classes to help handle Course Dog's API.
"""

from python.sources.format import JSONHandler
from python.checker.course import CourseChecker, PrereqChecker
from python.splitter.course import CourseInfoSplitter
from python.extractor.course import PrereqExtractor
from python.sources.config.school import SchoolConfigManager

class CourseSystem:
    """
    Handling Course Dog's API works for Courses.
    """
    # Course Dog's API variables
    _all_courses_key = "allCourses"
    _api_return_fields = (
        'institutionId,'
        + 'code,'
        + 'subjectCode,'
        + 'courseNumber,'
        + 'name,'
        + 'longName,'
        + 'description'
    )
    _api_limit = "infinity"

    def __init__(self, school_uid: str = None) -> None:
        """
        Initalize a CourseSystem object.
        """
        # Initialize necessary data and paths
        self._school_id = school_uid

        config = SchoolConfigManager(school_uid)
        self._school_key = config.get_school_key()
        self._data_path = config.get_data_path()
        self._course_path = config.get_course_path()
        self._program_path = config.get_program_path()
        self._general_key = config.get_general_key()
        self._honors_key = config.get_honors_key()

        self._all_subjects = JSONHandler.get_from_path.get(
            self._data_path / "allSubjects.json"
        )

    def get_api_input(self, subject_code: str = _all_courses_key, limit: str = _api_limit):
        """
        Get the API result for certain courses.
        """
        return JSONHandler.get_from_url(
            'https://app.coursedog.com/api/v1/cm/'  # API
            + self._school_id
            + '/courses/search/$filters?'  # Search courses
            + 'subjectCode=' + subject_code
            + '&returnFields=' + self.return_fields
            + '&limit=' + limit
        )

    def record_all_courses(self, is_honors: bool, subject: str = _all_courses_key):
        """
        Record all courses of a certain type (General, Honors) and subject.\n
        If no subject is passed, record all subjects.
        """
        # TODO record_all_courses(is_honors: bool) first
        # TODO get data from the corresponding file (general.json or honors.json)
        # TODO get only data of a specified subject
        # TODO record the data we get into specific subject json file

    def record_all_courses(self, is_honors: bool = None) -> None:
        """
        Record all courses of a certain type (General, Honors, or Either).
        """
        JSONHandler.write_to_path(
            self._course_path,
            self.get_all_related_courses(is_honors)
        )

    def get_all_related_courses(self, is_honors: bool = None) -> dict:
        """
        Get a dictionary of courses that belong to one of these type:
        - All courses.
        - Only general courses.
        - Only courses related to honors courses (including honors courses).
        """
        # TODO get_api_input() --> raw
        # TODO get_all_course_shells() --> format
        
        match is_honors:
            case None:  # Get all courses
                # TODO
                return
            case False:  # Get all general only courses with general only prerequisites
                return
            case True:  # Get all courses related to honors courses (including honors courses)
                return

    def get_all_course_shells(self, data: dict = get_api_input()) -> dict:
        """
        Get all CourseShell objects from the raw data and map them by uid.
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


