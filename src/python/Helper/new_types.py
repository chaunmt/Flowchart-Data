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
    self.uid = uid_
    self.code = code_
    self.subject = subject_
    self.number = number_
    self.honors = honors_
  
  #####################################
  def __repr__(self):
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
    self.prereq = prereq_
  
  #####################################
  def __repr__(self):
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
      writingIntensive_: bool,
      name_: str,
      fullname_: str,
      info_: str,
      prereq_: PrereqFormat
    ):
    # Initialize CourseShell
    super().__init__(uid_, code_, subject_, number_, honors_)

    # Intialize Course's additional fields
    self.writingIntensive = writingIntensive_
    self.name = name_
    self.fullname = fullname_
    self.info = info_
    self.prereq = prereq_
  
  #####################################
  def __repr__(self):
    return (
      f"Course(\n"
      f"  uid = {self.uid},\n"
      f"  code = {self.code},\n"
      f"  subject = {self.subject},\n"
      f"  number = {self.number},\n"
      f"  honors = {self.honors},\n"
      f"  writingIntensive = {self.writingIntensive},\n"
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
      degreeGranter_: str,
      classification_: str,
      diploma_: str,
      level_: str,
      accredited_: str,
      minProgramCredit_: int,
      maxProgramCredit_: int,
      minDegreeCredit_: int,
      maxDegreeCredit_: int
    ):
    self.code = code_
    self.name = name_
    self.status = status_
    self.type = type_
    self.degreeGranter = degreeGranter_
    self.classification = classification_
    self.diploma = diploma_
    self.level = level_
    self.accredited = accredited_
    self.minProgramCredit = minProgramCredit_
    self.maxProgramCredit = maxProgramCredit_
    self.minDegreeCredit = minDegreeCredit_
    self.maxDegreeCredit = maxDegreeCredit_
  
  #####################################
  def __repr__(self):
    return (
      f"ProgramShell(\n"
      f"  code = {self.code},\n"
      f"  name = {self.name},\n"
      f"  status = {self.status},\n"
      f"  type = {self.type},\n"
      f"  degreeGranter = {self.degreeGranter},\n"
      f"  classification = {self.classification},\n"
      f"  diploma = {self.diploma},\n"
      f"  level = {self.level},\n"
      f"  accredited = {self.accredited},\n"
      f"  minProgramCredit = {self.minProgramCredit},\n"
      f"  maxProgramCredit = {self.maxProgramCredit},\n"
      f"  minDegreeCredit = {self.minDegreeCredit},\n"
      f"  maxDegreeCredit = {self.maxDegreeCredit}\n"
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
      degreeGranter_: str,
      classification_: str,
      diploma_: str,
      level_: str,
      accredited_: str,
      minProgramCredit_: int,
      maxProgramCredit_: int,
      minDegreeCredit_: int,
      maxDegreeCredit_: int
    ):
    # Initialize ProgramShell
    super().__init__(
      code_,
      name_,
      status_,
      type_,
      degreeGranter_,
      classification_,
      diploma_,
      level_,
      accredited_,
      minProgramCredit_,
      maxProgramCredit_,
      minDegreeCredit_,
      maxDegreeCredit_
    )

    # TODO Intialize Program's additional fields
  
  #####################################
  def __repr__(self):
    # TODO Represend Program's information
    pass