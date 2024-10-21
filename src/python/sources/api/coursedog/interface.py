"""
This is a lower level interface for our CourseDog Data subsystems.
TODO Call for actual system work
"""

from python.sources.api.coursedog.system import CourseSystem, ProgramSystem

class CourseSystemInterface:
    """
    Interface for a system that manages and records courses data.\n
    Data is recording in their respective folder inside 'data' folder .
    """

    # All school ids that are used in our CourseSystem
    _SCHOOL_UIDS = "umn_umntc_peoplesoft"
    
    def __init__(self) -> None:
        # Store the CourseSystem instances for each school
        self._sys = {}

    def init_op(self) -> str:
        """
        Initializes the course system.
        """
        
        self._sys = CourseSystem(self._SCHOOL_UIDS)

        return "++ Course System: Ready!"
    
    def get_all(self, by_type: bool = True, by_subject: bool = False) -> str:
        """
        Record all courses data.\n
        Organize the data by subject or by type.\n
        We organize the data by type by default.
        """
        if by_subject:
           # TODO 
           return "++ Course System: Recorded all data by subject!"
        else:
            self._sys.record_all_shells_and_courses()
            return "++ Course System: Recorded all data by type!"
        
class ProgramSystemInterface:
    """
    Interface for a system that manages and records program data.\n
    Data is recorded in their respective folder inside the 'data' folder.
    """

    def init_op(self) -> str:
        """
        Initializes the program system.
        """

        return "++ Program System: Ready!"

    def get_all(self) -> str:
        """
        Records all program data information.
        """

        # TODO

        return "++ Program System: Recorded all program data."

    def get_program(self, program: str) -> str:
        """
        Records data for a specific program.
        """

        # TODO

        return f"++ Program System: Recorded data for program {program}."
