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
        Delete all empty components in prereq component
        and return the new prereq.
        """

        prereq = cls.item

        if isinstance(prereq, list): # For list
            # Continuetively delete all empty component top down
            while True:
                # Delete all empty components from list
                prereq = list(filter(None, prereq))
                
                changed = False # Check whether a change happens
                for index, value in enumerate(prereq):
                    # Recursively filter nested value
                    new_prereq = cls.filter(value)
                    
                    if prereq[index] != new_prereq:
                        changed = True # A change happens
                        prereq[index] = new_prereq
                
                if not changed:
                    break

        elif isinstance(prereq, dict): # For dictionary ('and', 'or' logic)
            while True:
                # Delete all empty components from dictionary
                prereq = dict((k, v) for k, v in prereq.items() if v)
            
                changed = False # Check whether a change happens
                for key, value in prereq.items():
                    # Recursively filter nested value
                    newprereq = cls.filter(value)
                    
                    if prereq[key] != newprereq:
                        changed = True # A change happens
                        prereq[key] = cls.filter(value)
                        
                if not changed:
                    break
        
        return prereq

###############################################################################
class PrereqFilterRedundantArray(PrereqFilter):
    """
    This class filter out all redundant arrays in prereq.
    """

    def filter(cls):
        """
        Delete all redundant array in prereq component
        and return the new prereq.
        """
