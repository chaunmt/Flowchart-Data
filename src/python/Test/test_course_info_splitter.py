from Test.test_setup import *

class TestCourseInfoSplitter(TestString):
  """
  Test module course_info_splitter.
  """
  
  #############################################################################
  def test_code_into_subj_num_suf(self):
    assert_eq(
      CourseInfoSplitter.code_into_subj_num_suf(self.s1),
      [None, None, None]
    )
    assert_eq(
      CourseInfoSplitter.code_into_subj_num_suf(self.s3),
      [None, None, None]
    )
    assert_eq(
      CourseInfoSplitter.code_into_subj_num_suf(self.s7),
      [None, None, None]
    )
    assert_eq(
      CourseInfoSplitter.code_into_subj_num_suf(self.s8),
      [None, '1', None]
    )
    assert_eq(
      CourseInfoSplitter.code_into_subj_num_suf(self.s9),
      [None, '1239WAD12', None]
    )
    assert_eq(
      CourseInfoSplitter.code_into_subj_num_suf(self.s10),
      ['CSCI', '3081', None]
    )
    assert_eq(
      CourseInfoSplitter.code_into_subj_num_suf(self.s11),
      ['CSCI', '3081', 'W']
    )
    assert_eq(
      CourseInfoSplitter.code_into_subj_num_suf(self.s12),
      ['CSCI', '3081', 'W']
    )

  #############################################################################
  def test_separate_number_suffix(self):
    assert_eq(
      CourseInfoSplitter.separate_number_suffix(self.s5),
      [None, None]
    )
    assert_eq(
      CourseInfoSplitter.separate_number_suffix(self.s7),
      [None, None]
    )
    assert_eq(
      CourseInfoSplitter.separate_number_suffix(self.s8),
      ['1', None]
    )
    assert_eq(
      CourseInfoSplitter.separate_number_suffix(self.s9),
      ['1239WAD12', None]
    )
    assert_eq(
      CourseInfoSplitter.separate_number_suffix(self.s10),
      ['CSCI3081', None]
    )
    assert_eq(
      CourseInfoSplitter.separate_number_suffix(self.s11),
      ['CSCI3081', 'W']
    )
    assert_eq(
      CourseInfoSplitter.separate_number_suffix(self.s12),
      ['CSCI3081', 'W']
    )
    assert_eq(
      CourseInfoSplitter.separate_number_suffix(self.s12),
      ['CSCI3081', 'W']
    )

