"""
This module contains class PrereqFilter which
filter prereq component and return its new result.
"""

from python.filter.filter import Filter
from python.schema.prereq import PrereqFormat

###############################################################################
class PrereqFilter(Filter):
    """
    This is the base class for all prereq filter classes.
    """

    allowed_type = PrereqFormat

###############################################################################
class PrereqFilterEmpty(PrereqFilter):
    """
    This class filter out all empty components in prereq.
    """

    def filter(cls):
        """
        Delete all empty components in prereq
        and return the new prereq.
        """

        prereq = cls.item

        if isinstance(prereq, list):
            # Filter all possible elements
            while True:
                # Delete all empty components from list
                prereq = list(filter(None, prereq))

                changed = False
                for index, value in enumerate(prereq):
                    # Recursively filter nested value
                    new_prereq = cls.filter(value)

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
                    new_prereq = cls.filter(value)

                    if prereq[key] != new_prereq:
                        changed = True
                        prereq[key] = new_prereq

                # If no value is changed, all values are filtered
                if not changed:
                    break

        return prereq

###############################################################################
class PrereqFilterRedundantNest(PrereqFilter):
    """
    This class filter out all redundant outer list and outer dictionary in prereq.
    """

    def filter(cls):
        """
        Delete all redundant outer lists and outer dictionaries in prereq
        and return the new prereq.
        """

        prereq = cls.item

        if isinstance(prereq, list):
            # Filter all possible elements
            while True:
                # Delete a redundant outer list
                if len(prereq) == 1:
                    prereq = prereq[0]

                changed = False
                for index, value in enumerate(prereq):
                    # Recursively filter nested value
                    new_prereq = cls.filter(value)

                    if prereq[index] != new_prereq:
                        changed = True
                        prereq[index] = new_prereq

                # If no value is changed, all values are filtered
                if not changed:
                    break

        elif isinstance(prereq, dict): # Logical operation 'and', 'or' and their value
            # Filter all possible elements
            while True:
                # Delete a redundant outer dictionary
                if len(prereq) == 1:
                    prereq = prereq[list(prereq.keys())[0]]

                changed = False
                for key, value in prereq.items():
                    # Recursively filter nested value
                    new_prereq = cls.filter(value)

                    if prereq[key] != new_prereq:
                        changed = True
                        prereq[key] = new_prereq

                # If no value is changed, all values are filtered
                if not changed:
                    break

        return prereq

###############################################################################
class PrereqFilterDuplicate(PrereqFilter):
    """
    This class filter out all duplicate elements of the same nested level in prereq.
    """

    def filter(cls):
        """
        Delete all duplicate elements of the same nested level in prereq
        and return the new prereq.
        """

        prereq = cls.item

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
                    new_prereq = cls.filter(value)

                    if prereq[index] != new_prereq:
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
                    if value not in res.items():
                        res[key] = value
                prereq = res

                changed = False
                for key, value in prereq.items():
                    # Recursively filter nested value
                    new_prereq = cls.filter(value)

                    if prereq[key] != new_prereq:
                        changed = True
                        prereq[key] = new_prereq

                # If no value is changed, all values are filtered
                if not changed:
                    break

        return prereq

###############################################################################
class PrereqFilterNonUid(PrereqFilter):
    """
    This class filter out all elements that are not in the form of a course's uid.\n
    """

    def filter(cls):
        """
        Delete all elements that are not in course's uid form
        and return the new prereq.
        """

        prereq = cls.item

        if isinstance(prereq, list):
            # Filter all possible elements
            while True:
                # Delete all non-uid elements from list
                res = []
                for value in prereq:
                    if value.isdigit():
                        res.append(value)
                prereq = res

                changed = False
                for index, value in enumerate(prereq):
                    # Recursively filter nested value
                    new_prereq = cls.filter(value)

                    if prereq[index] != new_prereq:
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
                    if value.isdigit():
                        res[key] = value
                prereq = res

                changed = False
                for key, value in prereq.items():
                    # Recursively filter nested value
                    new_prereq = cls.filter(value)

                    if prereq[key] != new_prereq:
                        changed = True
                        prereq[key] = new_prereq

                # If no value is changed, all values are filtered
                if not changed:
                    break

        return prereq
