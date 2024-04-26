from typing import List, Union

class CourseShell:
  """
  CouseShell contains basic information of a course.
  """
  def __init__(
      self,
      uid_: str,
      code_: str,
      subject_: str,
      number_: str
    ):
    self.uid = uid_
    self.code = code_
    self.subject = subject_
    self.number = number_

class PrereqCourses:
  """
  This class is going to be a union of these type formats:\n
  - CourseShell,
  - List[CourseShell],
  - { 'and' : List[CourseShell] },
  - { 'or' : List[CourseShell] }
  """
  def __init__(
      self,
      courses_: Union[List['PrereqCourses'], dict, CourseShell]
    ):
    self = courses_

class PrereqList:
  def __init__(self, prereqList_: List[PrereqCourses]):
    self = prereqList_

class Course(CourseShell):
  """
  Course contains all information about a course.\n
  It includes CourseShell with additional fields.
  """
  def __init__(
      self,
      uid_: str,
      code_: str,
      subject_: str,
      number_: str,
      name_: str,
      longname_: str,
      info_: str,
      prereq_: PrereqList
    ):
    # Initialize CourseShell
    super().__init__(uid_, code_, subject_, number_)

    # Intialize Course
    self.name = name_
    self.longname = longname_
    self.info = info_
    self.prereq = prereq_
