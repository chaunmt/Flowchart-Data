"""
This module contains filter classes related to course system:
- CourseInfoNonPrereqFilter
- PrereqFilter
- PrereqFilterEmpty
- PrereqFilterRedundantNest
- PrereqFilterDuplicate
- PrereqFilterNonUid
- PrereqFilterUidNotInShell
"""

from python.schema.course import PrereqFormat
from python.filter.string import StringFilter
from python.splitter.string import StringSplitter

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
        info = info.lower()

        # Possible split patterns for prerequisites
        split_patterns = [
            "prereq",
            "prereq:",
            "prerequisite",
            "prerequisite:",
            "prerequisites",
            "prerequisites:",
        ]

        # Find a split pattern in info string
        split_pattern = "\n\n\n\n\n"
        for pattern in split_patterns:
            if pattern in info:
                split_pattern = pattern

        # Split prereq from info
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
        # Only accept PrereqFormat object
        if not isinstance(prereq, PrereqFormat):
            raise TypeError(
                f"Expected a StringComponent instance for 's' instead of {type(prereq)}"
            )

        # Initialize
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
                            return rec_filter(prereq[0])

                    changed = False
                    for index, value in enumerate(prereq):
                        if isinstance(value, list):
                            if len(value) == 1:
                                prereq[index] = value[0]
                            else:
                                raise ValueError(
                                    "An important logical key ('and', 'or')" +
                                    f"is missing for the nest of this list: {value}"
                                )

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
                            return rec_filter(prereq[key])
                        if isinstance(prereq[key], list) and len(prereq[key]) == 1:
                            return rec_filter(prereq[key])

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

        p = rec_filter(self.prereq.process())

        # Make sure the final result is a PrereqFormat object
        if isinstance(p, list):
            p = { "and": p }

        return p

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
                        elif isinstance(value, (list, dict)):
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
                        elif isinstance(value, (list, dict)):
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
class PrereqFilterUidNotInShell(PrereqFilter):
    """
    This class filter out all course's uid that is not in the provided course shells.
    """

    def __init__(self, prereq: PrereqFormat, course_shells: dict):
        """
        Initialize the class instance.
        """
        super().__init__(prereq)
        self._shells = course_shells

    def process(self) -> dict:
        """
        Delete all non-general (honors or others) course's uid.
        """

        def rec_filter(prereq):
            """
            Recursively filter all nested level.
            """

            if isinstance(prereq, str) and prereq not in self._shells:
                return {}
            if isinstance(prereq, list):
                # Filter all possible elements
                while True:
                    # Delete all uids not belong in the provided course shells from the list
                    res = []
                    for value in prereq:
                        if isinstance(value, str) and value not in self._shells:
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
                    # Delete all uids not belong in the provided course shells from the dictionary
                    res = {}
                    for key, value in prereq.items():
                        if isinstance(value, str) and value not in self._shells:
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
