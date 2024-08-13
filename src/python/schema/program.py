"""
TODO
This class contains multiple classes to help define new types for programs.
"""

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
