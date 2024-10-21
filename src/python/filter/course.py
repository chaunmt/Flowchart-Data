"""
This module contains filter classes related to course system.
"""

from python.schema.course import PrereqFormat
from python.filter.string import StringFilter
from python.splitter.string import StringSplitter
from python.sources.format import JSONHandler

###############################################################################
class CourseInfoNonPrereqFilter(StringFilter):
    """
    This class filter out all redundant part of info string that doesn't represent prerequisites.
    """

    def process(self) -> str:
        """
        Delete all redundant part of info string that doesn't represent prerequisites.
        """

        # Process all previous filters
        info = self._s.process()

        # Possible split patterns for prerequisites
        split_patterns = [
            "prereq:",
            "prerequisite:",
            "prerequisites:",
            "prereq",
            "prerequisite",
            "prerequisites"
        ]

        # Find a split pattern in info string
        split_pattern = "\n\n\n\n\n"
        for pattern in split_patterns:
            if pattern in info:
                split_pattern = pattern

        # Split prereq from info
        info = info.lower()
        splitted_info = StringSplitter.at_substring(info, split_pattern)

        # Combine all founded prereq into one string
        if len(splitted_info) > 1:
            prereq_string = '\n'.join(splitted_info[1:])
        else:
            prereq_string = ''

        return prereq_string

###############################################################################
class PrereqFilter(PrereqFormat):
    """
    This is the base class for all prereq filter classes.
    """

    _prereq : PrereqFormat = None

    def __init__(self, prereq: PrereqFormat) -> None:
        """
        Initialize the class instance.
        """
        super().__init__(prereq)
        self._prereq = prereq

    @property
    def prereq(self) -> PrereqFormat:
        """
        Get the prereq value.
        """
        return self._prereq

    def process(self) -> dict:
        """
        Process all filters.
        """
        return self._prereq.process()

###############################################################################
class PrereqFilterEmpty(PrereqFilter):
    """
    This class filter out all empty components in prereq.
    """

    def process(self) -> dict:
        """
        Delete all empty components in prereq
        and return the new prereq.
        """

        def rec_filter(prereq):
            """
            Recursively filter all nested level.
            """

            if isinstance(prereq, list):
                # Filter all possible elements
                while True:
                    # Delete all empty components from list
                    prereq = [item for item in prereq if item]

                    changed = False
                    for index, value in enumerate(prereq):
                        # Recursively filter nested value
                        new_prereq = rec_filter(value)

                        if prereq[index] != new_prereq:
                            changed = True
                            prereq[index] = new_prereq

                    # If no value is changed, all values are filtered
                    if not changed:
                        break

            elif isinstance(prereq, dict): # Logical operation 'and', 'or' and their value
                # Filter all possible elements
                while True:
                    # Delete all empty components from dictionary
                    prereq = dict((k, v) for k, v in prereq.items() if v)

                    changed = False
                    for key, value in prereq.items():
                        # Recursively filter nested value
                        new_prereq = rec_filter(value)

                        if value != new_prereq:
                            changed = True
                            prereq[key] = new_prereq

                    # If no value is changed, all values are filtered
                    if not changed:
                        break
            return prereq

        return rec_filter(self.prereq.process())

###############################################################################
class PrereqFilterRedundantNest(PrereqFilter):
    """
    This class filter out all redundant outer list and outer dictionary in prereq.
    """

    def process(self) -> dict:
        """
        Delete all redundant outer lists and outer dictionaries in prereq
        and return the new prereq.
        """

        def rec_filter(prereq):
            """
            Recursively filter all nested level.
            """

            if isinstance(prereq, list):
                # Filter all possible elements
                while True:
                    # Delete a redundant outer list (list of only 1 item)
                    if len(prereq) == 1:
                        if isinstance(prereq[0], (dict, list)):
                            prereq = prereq[0]
                            return rec_filter(prereq)

                    changed = False
                    for index, value in enumerate(prereq):
                        # Recursively filter nested value
                        new_prereq = rec_filter(value)

                        if value != new_prereq:
                            changed = True
                            prereq[index] = new_prereq

                    # If no value is changed, all values are filtered
                    if not changed:
                        break

            elif isinstance(prereq, dict): # Logical operation 'and', 'or' and their value
                # Filter all possible elements
                while True:
                    # Delete a redundant outer dictionary (dict of only 1 dict)
                    if len(prereq) == 1:
                        key = list(prereq.keys())[0]
                        if isinstance(prereq[key], dict):
                            prereq = prereq[key]

                    changed = False
                    for key, value in prereq.items():
                        # Recursively filter nested value
                        new_prereq = rec_filter(value)

                        if value != new_prereq:
                            changed = True
                            prereq[key] = new_prereq

                    # If no value is changed, all values are filtered
                    if not changed:
                        break
            return prereq

        return rec_filter(self.prereq.process())

###############################################################################
class PrereqFilterDuplicate(PrereqFilter):
    """
    This class filter out all duplicate elements of the same nested level in prereq.
    """


    def process(self) -> dict:
        """
        Delete all duplicate elements of the same nested level in prereq
        and return the new prereq.
        """

        def rec_filter(prereq):
            """
            Recursively filter all nested level.
            """

            if isinstance(prereq, list):
                # Filter all possible elements
                while True:
                    # Delete all duplicate from list
                    res = []
                    for value in prereq:
                        if value not in res:
                            res.append(value)
                    prereq = res

                    changed = False
                    for index, value in enumerate(prereq):
                        # Recursively filter nested value
                        new_prereq = rec_filter(value)

                        if value != new_prereq:
                            changed = True
                            prereq[index] = new_prereq

                    # If no value is changed, all values are filtered
                    if not changed:
                        break

            elif isinstance(prereq, dict): # Logical operation 'and', 'or' and their value
                # Filter all possible elements
                while True:
                    # Delete all duplicate from dictionary
                    res = {}
                    for key, value in prereq.items():
                        if not key in res:
                            res[key] = value
                        if key in res and res[key] is not value:
                            res[key] = value
                    prereq = res

                    changed = False
                    for key, value in prereq.items():
                        # Recursively filter nested value
                        new_prereq = rec_filter(value)

                        if value != new_prereq:
                            changed = True
                            prereq[key] = new_prereq

                    # If no value is changed, all values are filtered
                    if not changed:
                        break
            return prereq

        return rec_filter(self.prereq.process())

###############################################################################
class PrereqFilterNonUid(PrereqFilter):
    """
    This class filter out all elements that are not in the form of a course's uid.\n
    """

    def process(self) -> dict:
        """
        Delete all elements that are not in course's uid form
        and return the new prereq.
        """

        def rec_filter(prereq):
            """
            Recursively filter all nested level.
            """

            if isinstance(prereq, list):
                # Filter all possible elements
                while True:
                    # Delete all non-uid elements from list
                    res = []
                    for value in prereq:
                        if isinstance(value, str) and value.isdigit():
                            res.append(value)
                        elif not isinstance(value, str):
                            res.append(value)
                    prereq = res

                    changed = False
                    for index, value in enumerate(prereq):
                        # Recursively filter nested value
                        new_prereq = rec_filter(value)

                        if value != new_prereq:
                            changed = True
                            prereq[index] = new_prereq

                    # If no value is changed, all values are filtered
                    if not changed:
                        break

            elif isinstance(prereq, dict): # Logical operation 'and', 'or' and their value
                # Filter all possible elements
                while True:
                    # Delete all non-uid elements from dictionary
                    res = {}
                    for key, value in prereq.items():
                        if isinstance(value, str) and value.isdigit():
                            res[key] = value
                        elif not isinstance(value, str):
                            res[key] = value
                    prereq = res

                    changed = False
                    for key, value in prereq.items():
                        # Recursively filter nested value
                        new_prereq = rec_filter(value)

                        if value != new_prereq:
                            changed = True
                            prereq[key] = new_prereq

                    # If no value is changed, all values are filtered
                    if not changed:
                        break
            return prereq

        return rec_filter(self.prereq.process())

###############################################################################
class PrereqFilterNonGeneralUid(PrereqFilter):
    """
    This class filter out all non-general (honors or others) course's uid.
    """

    def __init__(self, prereq: PrereqFormat, general_shells: dict):
        """
        Initialize the class instance.
        """
        super().__init__(prereq)
        self._general_shells = general_shells

    def process(self) -> dict:
        """
        Delete all non-general (honors or others) course's uid.
        """

        def rec_filter(prereq):
            """
            Recursively filter all nested level.
            """

            if isinstance(prereq, list):
                # Filter all possible elements
                while True:
                    # Delete all non-general uids from list
                    res = []
                    for value in prereq:
                        if isinstance(value, str) and value not in self._general_shells:
                            continue
                        res.append(value)
                    prereq = res

                    changed = False
                    for index, value in enumerate(prereq):
                        # Recursively filter nested value
                        new_prereq = rec_filter(value)

                        if value != new_prereq:
                            changed = True
                            prereq[index] = new_prereq

                    # If no value is changed, all values are filtered
                    if not changed:
                        break

            elif isinstance(prereq, dict): # Logical operation 'and', 'or' and their value
                # Filter all possible elements
                while True:
                    # Delete all non-general uids from dictionary
                    res = {}
                    for key, value in prereq.items():
                        if isinstance(value, str) and value not in self._general_shells:
                            continue
                        res[key] = value
                    prereq = res

                    changed = False
                    for key, value in prereq.items():
                        # Recursively filter nested value
                        new_prereq = rec_filter(value)

                        if value != new_prereq:
                            changed = True
                            prereq[key] = new_prereq

                    # If no value is changed, all values are filtered
                    if not changed:
                        break
            return prereq

        return rec_filter(self.prereq.process())
