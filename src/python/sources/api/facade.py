"""
Facade is the simplest interfaces for our subsystems.
The Facade delegates the client requests to the appropriate objects within the subsystem.
The Facade is also responsible for managing their lifecycle.
All of this shields the client from the undesired complexity of the subsystems.
"""

from python.sources.api.coursedog.interface import PrereqSystemInterface, ProgramSystemInterface

class CourseDogFacade:
    """
    Provides a simple interface to a more complex CourseDog Data subsystems' interface.
    """

    def __init__(
        self,
        prereqsys: PrereqSystemInterface,
        programsys: ProgramSystemInterface
    ) -> None:
        """
        Provide the Facade with existing subsystem objects or
        force the Facade to create them on its own.
        """

        self._prereqsys = prereqsys or PrereqSystemInterface()
        self._programsys = programsys or ProgramSystemInterface()

    def operation(self) -> str:
        """
        Convenient shortcuts to the sophisticated functionality of the subsystems.
        """

        res = []
        res.append("Course Dog Facade initializes subsystems:")
        res.append(self._prereqsys.init_op())
        res.append(self._programsys.init_op())
        res.append("Course Dog Facade orders subsystems to perform the action:")
        # res.append(self._prereqsys.get_all())
        res.append(self._prereqsys.get_subjects()) # Exclude allCourses

        return "\n".join(res)