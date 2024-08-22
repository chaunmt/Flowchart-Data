"""
This class contains multiple classes to help define new types for prerequisites.
"""

class CourseShell:
    """
    CouseShell contains basic information of a course.
    """

    #####################################
    def __init__(
            self,
            uid_: str,
            code_: str,
            subject_: str,
            number_: str,
            honors_: bool,
        ):
        """
        Initialize a CourseShell object.
        """

        self.uid = uid_
        self.code = code_
        self.subject = subject_
        self.number = number_
        self.honors = honors_

    #####################################
    def __repr__(self):
        """
        String representation of a CourseShell object.
        """

        return (
            f"CourseShell(\n"
            f"  uid = {self.uid},\n"
            f"  code = {self.code},\n"
            f"  subject = {self.subject},\n"
            f"  number = {self.number},\n"
            f"  honors = {self.honors}\n"
            f")"
        )

###############################################################################
class PrereqFormat:
    """
    PrereqFormat is a dictionary of courses' uid\n
    with or without their nested logical operation ('and', 'or').\n
    """

    #####################################
    def __init__(
            self,
            prereq_: dict
        ):
        """
        Initialize a PrereqFormat object.
        """

        # Call the error-checking method
        self.check_errors(prereq_)

        self.prereq = prereq_

    #####################################
    def check_errors(self, prereq_: dict):
        """
        Error checking method to validate the structure of prereq_.
        """

        for k, v in prereq_.items():
            # Check if the key is valid ('and' or 'or')
            if k not in ["and", "or"]:
                raise ValueError(
                    f"Invalid prereq's key '{k}' found. Allowed keys are 'and' or 'or'."
                )

            if (
                # Check if the value is a list
                not isinstance(v, list) or
                # Check if the value's strings representing uid numbers
                not all(isinstance(uid, str) and uid.isdigit() for uid in v)
            ):
                raise ValueError(
                    f"The value for key '{k}' must be a list of numeric strings."
                )

    #####################################
    def __repr__(self):
        """
        String representation of a PrereqFormat object.
        """

        return (
            f"PrereqFormat(\n"
            f"  prereq = {self.prereq}\n"
            f")"
        )

###############################################################################
class Course(CourseShell):
    """
    Course contains all information about a course.\n
    It includes CourseShell with additional fields.
    """

    #####################################
    def __init__(
            self,
            uid_: str,
            code_: str,
            subject_: str,
            number_: str,
            honors_: bool,
            writing_intensive_: bool,
            name_: str,
            fullname_: str,
            info_: str,
            prereq_: PrereqFormat
        ):
        """
        Initialize a Course object.
        """

        # Initialize CourseShell
        super().__init__(uid_, code_, subject_, number_, honors_)

        # Intialize Course's additional fields
        self.writing_intensive = writing_intensive_
        self.name = name_
        self.fullname = fullname_
        self.info = info_
        self.prereq = prereq_

    #####################################
    def __repr__(self):
        """
        String representation of a Course object.
        """

        return (
            f"Course(\n"
            f"  uid = {self.uid},\n"
            f"  code = {self.code},\n"
            f"  subject = {self.subject},\n"
            f"  number = {self.number},\n"
            f"  honors = {self.honors},\n"
            f"  writing_intensive = {self.writing_intensive},\n"
            f"  name = {self.name},\n"
            f"  fullname = {self.fullname},\n"
            f"  info = {self.info},\n"
            f"  prereq = {self.prereq}\n"
            f")"
        )
