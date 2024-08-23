"""
This is a lower level interface for our CourseDog Data subsystems.
TODO Call for actual system work
"""

from python.sources.api.coursedog.system import CourseSystem, ProgramSystem

class CourseSystemInterface:
    """
    Interface for a system that manages and retrieves courses data.\n
    Data is recording in their respective folder inside 'data' folder .
    """

    def init_op(self) -> str:
        """
        Initializes the course system.
        """

        return "Course System: Ready!"

    def get_all(cls) -> str:
        """
        Retrieves all course data information.
        """
        
        # TODO

        return "Course System: Retrieved all data."

    def get_subjects(self) -> str:
        """
        Retrieves course data of all subjects.
        """
        
        # TODO

        return "Course System: Retrieved all subjects' course data."

    def get_subject(self, subj: str) -> str:
        """
        Retrieves course data of a subject.
        """
        
        # TODO

        return f"Course System: Retrieved course data for subject {subj}."

    def get_course(self, course_uid: str) -> str:
        """
        Retrieves a course data.
        """
        
        # TODO

        return f"Course System: Retrieved course data for course {course_uid}."

class ProgramSystemInterface:
    """
    Interface for a system that manages and retrieves program data.\n
    Data is recorded in their respective folder inside the 'data' folder.
    """

    def init_op(self) -> str:
        """
        Initializes the program system.
        """

        return "Program System: Ready!"

    def get_all(self) -> str:
        """
        Retrieves all program data information.
        """
        
        # TODO

        return "Program System: Retrieved all program data."

    def get_program(self, program: str) -> str:
        """
        Retrieves data for a specific program.
        """
        
        # TODO

        return f"Program System: Retrieved data for program {program}."
