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
        

    