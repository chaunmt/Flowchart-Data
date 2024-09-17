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

    def __init__(self) -> None:
        # Note: We only work with UMNTC
        # For future extension, id should be passed and checked from facade
        self._UMNTC_ID = 'umn_umntc_peoplesoft'

    def init_op(self) -> str:
        """
        Initializes the course system.
        """
        
        self._sys = CourseSystem(self._UMNTC_ID)

        return "++ Course System: Ready!"
    
    def get_all(self, is_by_subject: bool, is_by_type: bool) -> str:
        """
        Record all courses data.\n
        Organize the data by subject or by type.
        """
        
        if is_by_subject == is_by_type:
            return "++ Course System: Please choose only 1 way to organize data!"
        
        if is_by_subject:
            self.get_subjects(False)    # Get general courses
            self.get_subjects(True)     # Get honors courses
            return "++ Course System: Recorded all data by subject!"
        
        if is_by_type:
            # TODO self.get_subject('allCourses', True)
            # TODO modify get_subject for all honors courses to include all courses related to honors courses
            self.get_general()
            self.get_honors()
            return "++ Course System: Recorded all data by type!"    
    
    def get_general(self) -> str:
        """
        Record all general courses.
        """
        
        self._sys.get_general_courses_output_json()
        
        return "++ Course System: Recorded general courses." 

    def get_honors(self) -> str:
        """
        Record all honors courses and courses with honors prerequisites.
        """
        
        #TODO self._sys.get_honors_courses_output_json()
        
        return "++ Course System: Recorded honors courses"

    def get_subjects(self, is_honors: bool) -> str:
        """
        Records course data of all subjects.
        """
        
        self._sys.get_subject_courses_output_json('allCourses', is_honors)
        
        subjs = self._sys.get_all_subjects_list_json()
        for subj in subjs:
            self.get_subject(subj, is_honors)

        honors_type = "general"
        if is_honors:
            honors_type = "honors"

        return f"++ Course System: Recorded all subjects' {honors_type} course data."

    def get_subject(self, subject_code: str, is_honors: bool) -> str:
        """
        Records course data of a subject by the subject's code and its honors type.
        """

        if subject_code != 'allCourses':
            subject_code = subject_code.upper()
        self._sys.get_subject_courses_output_json(subject_code, is_honors)

        honors_type = "general"
        if is_honors:
            honors_type = "honors"

        return f"++ Course System: Recorded {honors_type} course data for subject {subject_code}."

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
