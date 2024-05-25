from Test.test_setup import *

class TestNewTypes(TestString, TestPrereq):
  """
  Test module new_types
  """
  def setUp(self):
    TestString.setUp(self)
    TestCourse.setUp(self)
    TestPrereq.setUp(self)

  def tearDown(self):
    TestString.tearDown(self)
    TestCourse.tearDown(self)
    TestPrereq.tearDown(self)

  def test_course_shell(self):
    for index, shell in enumerate(self.course_shells):
      assert_eq(
        shell.uid,
        self.course_shell_data[index]['uid_']
      )
      assert_eq(
        shell.code,
        self.course_shell_data[index]['code_']
      )
      assert_eq(
        shell.subject,
        self.course_shell_data[index]['subject_']
      )
      assert_eq(
        shell.number,
        self.course_shell_data[index]['number_']
      )
      assert_eq(
        shell.honors,
        self.course_shell_data[index]['honors_']
      )

  def test_course(self):
    for index, course in enumerate(self.courses):
      assert_eq(
        course.uid,
        self.course_data[index]['uid_']
      )
      assert_eq(
        course.code,
        self.course_data[index]['code_']
      )
      assert_eq(
        course.subject,
        self.course_data[index]['subject_']
      )
      assert_eq(
        course.number,
        self.course_data[index]['number_']
      )
      assert_eq(
        course.honors,
        self.course_data[index]['honors_']
      )
      assert_eq(
        course.writingIntensive,
        self.course_data[index]['writingIntensive_']
      )
      assert_eq(
        course.name,
        self.course_data[index]['name_']
      )
      assert_eq(
        course.fullname,
        self.course_data[index]['fullname_']
      )
      assert_eq(
        course.info,
        self.course_data[index]['info_']
      )
      assert_eq(
        course.prereq,
        self.course_data[index]['prereq_']
      )

  def test_prereq_format(self):
    # Test single CourseShell
    assert_eq(
      self.p1.prereq.uid,
      '1'
    )
    assert_eq(
      self.p1.prereq.code,
      'CSC101'
    )
    assert_eq(
      self.p1.prereq.number,
      101
    )
    assert_eq(
      self.p1.prereq.honors,
      False
    )

    # Test List[CourseShell]
    for index, shell in enumerate(self.course_shells):
      assert_eq(self.p2.prereq[index], shell)

  def test_program_shell(self):
    # TODO
    pass

  def test_program(self):
    # TODO
    pass