"""
This is a lower level interface for our CourseDog Data subsystems.
"""

from python.sources.api.coursedog.system import PrereqSystem, ProgramSystem

class PrereqSystemInterface:
    """
    """
    
    def init_op(self) -> str:
        """
        """
        
        return "Prerequisites System: Ready!"
    
    def get_all(cls) -> str:
        """
        """
    def get_subjects(self) -> str:
        """
        """
    def get_subject(self) -> str:
        """
        """
    def get_course(self) -> str:
        """
        """
    def get_sample(self) -> str:
        """
        """

class ProgramSystemInterface:
    """
    TODO
    """
    
    def init_op(self) -> str:
        """
        """
        
        return "Program System: Ready!"

    def get_all(self) -> str:
        """
        """
    def get_programs(self) -> str:
        """
        """
    def get_program(self) -> str:
        """
        """
    def get_sample(self) -> str:
        """
        """
