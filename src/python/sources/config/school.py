"""
This module contains a class that help handle the configuration of the schools.
"""

from pathlib import Path
from dataclasses import dataclass, field
from python.sources.config.file import FileHandler

@dataclass
class SchoolConfig:
    # Can be initialized
    school_id: str = "Default"

    # Fixed values
    base_dir: Path = field(default_factory=FileHandler.find_project_root, init = False)
    school_id_to_code: dict[str,str] = field(
        default_factory = lambda: {
            "umn_umntc_peoplesoft" : "UMNTC",
            "Default" : "Others"
        },
        init = False
    )

    @property
    def id(self) -> str:
        return self.school_id

    @property
    def code(self) -> str:
        return self.school_id_to_code[self.school_id]

    @property
    def general_key(self) -> str:
        return "general"

    @property
    def honors_key(self) -> str:
        return "honors"

    @property
    def data_path(self) -> Path:
        return self.base_dir / f"data/{self.code}"

    @property
    def course_path(self) -> Path:
        return self.data_path / "Course"

    @property
    def program_path(self) -> Path:
        return self.data_path / "Program"

    @property
    def all_subjects_path(self) -> Path:
        return self.data_path / "allSubjects.json"

    @property
    def raw_report_path(self) -> Path:
        return self.data_path / "Coursedog/coursedog_f2025report_06242025.csv"

    @property
    def unique_field_vals_path(self) -> Path:
        return self.data_path / "uniqueVals.json"
