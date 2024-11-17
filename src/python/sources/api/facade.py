"""
Facade is the simplest interfaces for our subsystems.
The Facade delegates the client requests to the appropriate objects within the subsystem.
The Facade is also responsible for managing their lifecycle.
All of this shields the client from the undesired complexity of the subsystems.
"""

from python.sources.api.coursedog import CourseSystem, ProgramSystem

class CourseDogFacade:
    """
    Provides a simple interface to a more complex CourseDog Data subsystems.
    """

    def __init__(
        self,
        coursesys: CourseSystem,
        programsys: ProgramSystem
    ) -> None:
        """
        Provide the Facade with existing subsystem objects or
        force the Facade to create them on its own.
        """

        self._coursesys = coursesys or CourseSystem()
        self._programsys = programsys or ProgramSystem()

    def operation(self) -> str:
        """
        Convenient shortcuts to the sophisticated functionality of the subsystems.
        """

        res = []
        res.append(self._coursesys.record_all_shells_and_courses())
        res.append(self._coursesys.record_all_subj_num_uids())
        res.append("++ Course Dog Facade: Subsystems' actions performed!")

        return "\n".join(res)
