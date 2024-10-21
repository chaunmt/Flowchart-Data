"""
This module contains classes that help handle the configuration of different schools.
"""

from python.sources.config.file import FileHandler

class SchoolConfigManager:
    """
    Manages the configuration for different schools.
    This class handles paths, keys, and any school-specific data.
    """

    # Get the project's root path
    _base_dir = FileHandler.find_project_root()

    # Map school's uid to abbreviated key
    _school_uid_to_key = {
        "umn_umntc_peoplesoft" : "UMNTC",
        "Default" : "Others"
    }

    def __init__(self, school_uid: str = "Default"):
        """
        Initializes the configuration manager with the correct settings for the given school.
        """
        # Get school key
        school_key = self._school_uid_to_key.get(
            school_uid,
            self._school_uid_to_key["Default"])  # If no uid found, use the default uid

        # Build school's config data
        self._config = self.build_config(school_key)

    def build_config(self, school_key: str) -> dict:
        """
        Builds a configuration dictionary with
        common paths and school-specific subfolders.
        """
        base_path = self._base_dir / f"data/{school_key}"
        return {
            "school_key": school_key,
            "data_path": base_path,
            "course_path": base_path / "Course/",
            "program_path": base_path / "Program/",
            "general_key": "general",
            "honors_key": "honors"
        }

    def get_school_key(self) -> str:
        """
        Get school key from config data. It is usually the abbreviation of the school's uid.
        """
        return self._config["school_key"]

    def get_data_path(self) -> str:
        """
        Get the path to the data folder.
        """
        return self._config["data_path"]

    def get_course_path(self) -> str:
        """
        Get the path to the course folder.
        """
        return self._config["course_path"]

    def get_program_path(self) -> str:
        """
        Get the path to the program folder.
        """
        return self._config["program_path"]

    def get_general_key(self) -> str:
        """
        Get the general key.
        """
        return self._config["general_key"]

    def get_honors_key(self) -> str:
        """
        Get the honors key.
        """
        return self._config["honors_key"]
