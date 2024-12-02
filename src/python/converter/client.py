"""
This module contains the post-conversion to convert our object into the client's format.
"""

from python.schema.course import PrereqFormat

class FlowchartConverter:
    """
    Convert into a flowchart format.
    """

    def __init__(self, prereq: PrereqFormat) -> None:
        self._prereq = prereq

    def get_prereq(self) -> any:
        """
        Get the prereq object.
        """
        return self._prereq

    def convert(self) -> None:
        """
        Convert the prereq format into a flowchart format.
        """
        self._prereq = self.break_one_child_nest(self._prereq)
    
    def unconvert(self) -> None:
        """
        Convert the flowchart format back into the original format.
        """
        self._prereq = self.revert_one_child_nest(self._prereq)

    def break_one_child_nest(self, prereq: PrereqFormat) -> None:
        """
        Break all one child nest (dict or list of 1 member) into just that child.
        """
        if isinstance(prereq, dict) and len(prereq) == 1:
            key = list(prereq.keys())[0]
            if len(prereq[key]) == 1:
                return prereq[key][0]
        elif isinstance(prereq, list) and len(prereq) == 1:
            return prereq[0]
        
        return prereq

    def revert_one_child_nest(self, prereq: PrereqFormat) -> None:
        """
        Revert all one child nest (dict or list of 1 member) back into the original format.
        """
        # Current implementation is not needed if this conversion is done after all filters
        pass