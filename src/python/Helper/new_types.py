from typing import List, Union

class CourseShell:
  def __init__(self, code: str, subject: str, id: str):
    self.code = code
    self.subject = subject
    self.id = id

class PrereqList(List[Union['PrereqFormat', CourseShell]]):
  """
  PrereqList can be either
  a list of PrereqFormat or a list of CourseShell
  """
  pass

class PrereqFormat:
  def __init__(self, and_: PrereqList = None, or_: PrereqList = None):
    self.and_ = and_ or []
    self.or_ = or_ or []

class Course(CourseShell):
  def __init__(
      self, code: str, subject: str, id: str,
      title: str, info: str, prereq: PrereqFormat):
    # Initialize CourseShell
    super().__init__(code, subject, id)

    # Intialize Course
    self.title = title
    self.info = info
    self.prereq = prereq
