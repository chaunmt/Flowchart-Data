"""
Classes to help handle Course Dog's related information.
"""

from python.sources.format import JSONHandler, CSVHandler
from python.sources.config.school import SchoolConfig

class SystemConfig():
    """
    Configuration for Course Dog's API system.
    """

    def __init__(self, school_id: str = None):
        self.school = SchoolConfig(school_id=school_id)

class SubjectHandler(SystemConfig):
    """
    Handling Course Dog's API works for Subjects.
    """

    def __init__(self, school_id: str = None):
        super().__init__(school_id)
        self._all_subjects = JSONHandler.get_from_path(f"{self.school.data_path}/allSubjects.json")
        self._all_courses_list = CSVHandler.get_json_from_path(self.school.raw_report_path)

    def record_all_subj_num_uids(self) -> None:
        """
        Record all subject's num->uid maps to a json file.\n
        EX:
        {
            "AAS": {
                "1101": "797460",
                "1201": "803713"
            }
        }
        """
        # Get the mapping from subject to num->uid dict
        print(">>>>>> Generating course number to uid maps for subjects...")
        subj_lists = self.get_all_subj_num_uids(
            JSONHandler.get_from_path(f"{self.school.course_path}/{self._ALL_COURSE_KEY}Shells.json")
        )
        print(">>>>>> Successfully mapped course numbers to uids!")

        # Define file path and write to it
        filename = "subjectUidMaps.json"
        JSONHandler.write_to_path(f"{self.school.data_path}/{filename}", subj_lists)
        print(">>>>>> Subject maps written successfully!")

        return "++ SubjectHandler: All subjects' num->uid maps data written successfully!"

    def get_all_subj_num_uids(self, courses) -> dict:
        """
        Get a dictionary with subject as key and subject's num->uid maps as value from data.
        """
        if isinstance(courses, dict):
            courses = courses.values()

        # Create empty dicts for each subject
        mapping = { subj: dict() for subj in self._all_subjects }
        for course in courses:
            # Get necessary data
            uid = course["uid"]
            honor = course["honors"]
            num = course["number"]
            subj = course["subject"]
            subj_map = mapping.get(subj)

            # Map a subject's course number (including an H for honors) to its uid
            index = f"{num}{"H" if honor else ""}"
            if subj_map is not None:
                subj_map[index] = uid

        return mapping
