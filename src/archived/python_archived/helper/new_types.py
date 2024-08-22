"""
This class contains multiple classes to help define new types.
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
    TODO
    An any type is used as a placeholder.\n
    A checker should be made to make sure only acceptable members are presented in this type.
    """

    #####################################
    def __init__(
            self,
            prereq_: any
        ):
        """
        Initialize a PrereqFormat object.
        """

        self.prereq = prereq_

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

###############################################################################
class ProgramShell:
    """
    ProgramShell contains basic information of a program.
    """

    #####################################
    def __init__(
            self,
            code_: str,
            name_: str,
            status_: str,
            type_: str,
            degree_granter_: str,
            classification_: str,
            diploma_: str,
            level_: str,
            accredited_: str,
            min_program_credit_: int,
            max_program_credit_: int,
            min_degree_credit_: int,
            max_degree_credit_: int
        ):
        """
        Initialize a ProgramShell object.
        """

        self.code = code_
        self.name = name_
        self.status = status_
        self.type = type_
        self.degree_granter = degree_granter_
        self.classification = classification_
        self.diploma = diploma_
        self.level = level_
        self.accredited = accredited_
        self.min_program_credit = min_program_credit_
        self.max_program_credit = max_program_credit_
        self.min_degree_credit = min_degree_credit_
        self.max_degree_credit = max_degree_credit_

    #####################################
    def __repr__(self):
        """
        String representation of a ProgramShell object.
        """

        return (
            f"ProgramShell(\n"
            f"  code = {self.code},\n"
            f"  name = {self.name},\n"
            f"  status = {self.status},\n"
            f"  type = {self.type},\n"
            f"  degree_granter = {self.degree_granter},\n"
            f"  classification = {self.classification},\n"
            f"  diploma = {self.diploma},\n"
            f"  level = {self.level},\n"
            f"  accredited = {self.accredited},\n"
            f"  min_program_credit = {self.min_program_credit},\n"
            f"  max_program_credit = {self.max_program_credit},\n"
            f"  min_degree_credit = {self.min_degree_credit},\n"
            f"  max_degree_credit = {self.max_degree_credit}\n"
            f")"
        )

###############################################################################
class Program(ProgramShell):
    """
    Program contains all information about a program.\n
    It includes ProgramShell with additional fields.
    """

    #####################################
    def __init__(
            self,
            code_: str,
            name_: str,
            status_: str,
            type_: str,
            degree_granter_: str,
            classification_: str,
            diploma_: str,
            level_: str,
            accredited_: str,
            min_program_credit_: int,
            max_program_credit_: int,
            min_degree_credit_: int,
            max_degree_credit_: int
        ):
        """
        Initialize a Program object.
        """

        # Initialize ProgramShell
        super().__init__(
            code_,
            name_,
            status_,
            type_,
            degree_granter_,
            classification_,
            diploma_,
            level_,
            accredited_,
            min_program_credit_,
            max_program_credit_,
            min_degree_credit_,
            max_degree_credit_
        )

        # TODO Intialize Program's additional fields

    #####################################
    def __repr__(self):
        """
        String representation of a Program object.
        """

        # TODO Represend Program's information
        pass
