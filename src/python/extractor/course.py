"""
Extractors for course system.
"""

from python.schema.course import PrereqFormat
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

class PrereqExtractor:
    """
    Extract logical dictionary of prerequisites from an info string.
    """

    def __init__(self, info_str: str, target_subj: str, is_honors: bool) -> None:
        """
        Initialize PrereqExtractor.
        """

        self._info_str = info_str
        self._target_subj = target_subj
        self._is_honors = is_honors
        self._prereq = {}

    def get_prereq(self) -> dict:
        """
        Return a prereq dictionary.
        """

        return self._prereq

    def extract(self) -> None:
        """
        Extract the prerequisite's logical dictionary from an info string.
        """

        self.pre_processing()

        prereq = PrereqInfoConverter(self._info_str, self._target_subj, self._is_honors)
        prereq.process()
        prereq = prereq.get_prereq()
        self._prereq = prereq

        self.post_processing()

    def pre_processing(self) -> None:
        """
        Process the prereq string before extracting its prereq dictionary.
        """

        # Locate the prereq string in info string
        s = StringComponent(self._info_str)
        s = CourseInfoNonPrereqFilter(s)
        s = s.process()

        # Standardize input string
        s = CourseInfoConverter.paren_to_square_bracket(s)
        s = CourseInfoConverter.sign_to_logical_op(s)
        s = CourseInfoConverter.combine_standalone_subject(s)

        self._info_str = s

    def post_processing(self) -> None:
        """
        Process the extracted prereq's dictionary:
        - Delete duplicates.
        - Delete non-uid members.
        - Delete redundant nest level.
        - Delete empty component (but keep one {} if prereq has no member).
        """

        p = PrereqFormat(self._prereq)
        p = PrereqFilterDuplicate(p)
        p = PrereqFilterNonUid(p)
        p = PrereqFilterRedundantNest(p)
        p = PrereqFilterEmpty(p)

        self._prereq = p.process()
