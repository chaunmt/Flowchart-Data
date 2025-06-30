"""
Extractors for course system.
"""

from python.schema.definitions import PrereqFormat
from python.converter.course import PrereqInfoConverter
from python.converter.course import CourseInfoConverter
from python.filter.string import StringComponent
from python.filter.course import (
    CourseInfoNonPrereqFilter,
    PrereqFilterDuplicate,
    PrereqFilterEmpty,
    PrereqFilterNonUid,
    PrereqFilterRedundantNest
)
from python.converter.client import FlowchartConverter

class PrereqExtractor:
    """
    Extract logical dictionary of prerequisites from an info string.
    """

    def __init__(self, info_str: str, target_subj: str, courseshells: dict) -> None:
        self._info_str = info_str
        self._target_subj = target_subj
        self._prereq = {}
        self._courseshells = courseshells

    def get_prereq(self) -> dict:
        return self._prereq

    def extract(self) -> None:
        """
        Extract the prerequisite's logical dictionary from an info string.
        """

        self._prereq = self.pre_processing(self._info_str)

        prereq = PrereqInfoConverter(self._info_str, self._target_subj, self._courseshells)
        prereq.process()
        prereq = prereq.get_prereq()
        self._prereq = prereq

        self._prereq = self.post_processing(self._prereq)

    @staticmethod
    def pre_processing(s: str) -> str:
        """
        Process (standardize the format) the prereq string before extracting its prereq dictionary.
        """

        # Locate the prereq string in info string
        s = StringComponent(s)
        s = CourseInfoNonPrereqFilter(s)
        s = s.process()

        # Standardize input string
        s = CourseInfoConverter.paren_to_square_bracket(s)
        s = CourseInfoConverter.sign_to_logical_op(s)
        s = CourseInfoConverter.combine_standalone_subject(s)

        return s

    @staticmethod
    def post_processing(prereq: PrereqFormat | dict) -> dict:
        """
        Process (clean up) the a dictionary-typed prereq and return a PrereqFormat object.
        """
        
        p = prereq
        if isinstance(p, dict):
            p = PrereqFormat(p)

        # Filter the prereq dictionary
        while True:
            p = PrereqFilterNonUid(p)
            p = PrereqFilterDuplicate(p)
            p = PrereqFilterEmpty(p)
            p = PrereqFilterRedundantNest(p)

            pp = p.process()
            if pp == prereq:
                break
            prereq = pp
        
        # Convert to client's format
        client_format = FlowchartConverter(prereq)
        client_format.convert()
        prereq = client_format.get_prereq()
        
        return prereq
