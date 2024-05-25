from Test.test_setup import *

class TestStringSplitter(TestString):
  """
  Test module string_splitter.
  """
  def test_at_index(self):
    assert_eq(
      StringSplitter.at_index(self.s1, 5),
      ['Hello,', ' world!']
    )
    assert_eq(
      StringSplitter.at_index(self.s1, 7),
      ['Hello, w', 'orld!']
    )
    assert_eq(
      StringSplitter.at_index(self.s2, 11),
      ['Python  is  ', ' fun!']
    )
    assert_eq(
      StringSplitter.at_index(self.s3, 3),
      ['12!3', ' !4.5']
    )
    assert_eq(
      StringSplitter.at_index(self.s3, 5),
      ['12!3 !', '4.5']
    )
    assert_eq(
      StringSplitter.at_index(self.s6, 3),
      ['!@#$', '%^&*()']
    )

  def test_at_substring(self):
    assert_eq(
      StringSplitter.at_substring(self.s1, ','),
      ['Hello', ' world!']
    )
    assert_eq(
      StringSplitter.at_substring(self.s1, 'world'),
      ['Hello, ', '!']
    )
    assert_eq(
      StringSplitter.at_substring(self.s2, ' '),
      ['Python', 'is', 'fun!']
    )
    assert_eq(
      StringSplitter.at_substring(self.s2, '  '),
      ['Python', 'is', ' fun!']
    )
    assert_eq(
      StringSplitter.at_substring(self.s3, '!'),
      ['12', '3 ', '4.5']
    )
    assert_eq(
      StringSplitter.at_substring(self.s3, '12!'),
      ['3 !4.5']
    )
    assert_eq(
      StringSplitter.at_substring(self.s4, '?S1'),
      ['C', '!0^1@']
    )
    assert_eq(
      StringSplitter.at_substring(self.s5, '^'),
      ['This ! is ? a ', ' test.']
    )
    assert_eq(
      StringSplitter.at_substring(self.s6, '*'),
      ['!@#$%^&', '()']
    )

  def test_at_first_type_occurrence(self):
    # Test wrong split_type
    self.assertRaises(
      ValueError,
      StringSplitter.at_first_type_occurrence, self.s1, 'word'
    )

    # Test splitting at the first letter occurrence
    assert_eq(
      StringSplitter.at_first_type_occurrence(self.s1, 'letter'),
      ['', 'Hello, world!']
    )
    assert_eq(
      StringSplitter.at_first_type_occurrence(self.s3, 'letter'),
      ['12!3 !4.5', None]
    )
    assert_eq(
      StringSplitter.at_first_type_occurrence(self.s4, 'letter'),
      ['', 'C?S1!0^1@']
    )

    # Test splitting at the first number occurrence
    assert_eq(
      StringSplitter.at_first_type_occurrence(self.s3, 'number'),
      ['', '12!3 !4.5']
    )
    assert_eq(
      StringSplitter.at_first_type_occurrence(self.s1, 'number'),
      ['Hello, world!', None]
    )
    assert_eq(
      StringSplitter.at_first_type_occurrence(self.s6, 'number'),
      ['!@#$%^&*()', None]
    )
    assert_eq(
      StringSplitter.at_first_type_occurrence(self.s4, 'number'),
      ['C?S', '1!0^1@']
    )

  def test_at_last_type_occurrence(self):
    # Test wrong split_type
    self.assertRaises(
      ValueError,
      StringSplitter.at_last_type_occurrence, self.s1, 'word'
    )

    # Test splitting at the last letter occurrence
    assert_eq(
      StringSplitter.at_last_type_occurrence(self.s1, 'letter'),
      ['Hello, world', '!']
    )
    assert_eq(
      StringSplitter.at_last_type_occurrence(self.s3, 'letter'),
      ['12!3 !4.5', None]
    )
    assert_eq(
      StringSplitter.at_last_type_occurrence(self.s4, 'letter'),
      ['C?S', '1!0^1@']
    )

    # Test splitting at the last number occurrence
    assert_eq(
      StringSplitter.at_last_type_occurrence(self.s3, 'number'),
      ['12!3 !4.5', None]
    )
    assert_eq(
      StringSplitter.at_last_type_occurrence(self.s1, 'number'),
      ['Hello, world!', None]
    )
    assert_eq(
      StringSplitter.at_last_type_occurrence(self.s6, 'number'),
      ['!@#$%^&*()', None]
    )
    assert_eq(
      StringSplitter.at_last_type_occurrence(self.s4, 'number'),
      ['C?S1!0^1', '@']
    )

  def test_code_into_subj_num_suffix_suffix(self):
    assert_eq(
      StringSplitter.code_into_subj_num_suffix(self.s1),
      [None, None, None]
    )
    assert_eq(
      StringSplitter.code_into_subj_num_suffix(self.s3),
      [None, None, None]
    )
    assert_eq(
      StringSplitter.code_into_subj_num_suffix(self.s7),
      [None, None, None]
    )
    assert_eq(
      StringSplitter.code_into_subj_num_suffix(self.s8),
      [None, '1', None]
    )
    assert_eq(
      StringSplitter.code_into_subj_num_suffix(self.s9),
      [None, '1239WAD12', None]
    )
    assert_eq(
      StringSplitter.code_into_subj_num_suffix(self.s10),
      ['CSCI', '3081', None]
    )
    assert_eq(
      StringSplitter.code_into_subj_num_suffix(self.s11),
      ['CSCI', '3081', 'W']
    )
    assert_eq(
      StringSplitter.code_into_subj_num_suffix(self.s12),
      ['CSCI', '3081', 'W']
    )

  def test_separate_number_suffix(self):
    assert_eq(
      StringSplitter.separate_number_suffix(self.s5),
      [None, None]
    )
    assert_eq(
      StringSplitter.separate_number_suffix(self.s7),
      [None, None]
    )
    assert_eq(
      StringSplitter.separate_number_suffix(self.s8),
      ['1', None]
    )
    assert_eq(
      StringSplitter.separate_number_suffix(self.s9),
      ['1239WAD12', None]
    )
    assert_eq(
      StringSplitter.separate_number_suffix(self.s10),
      ['CSCI3081', None]
    )
    assert_eq(
      StringSplitter.separate_number_suffix(self.s11),
      ['CSCI3081', 'W']
    )
    assert_eq(
      StringSplitter.separate_number_suffix(self.s12),
      ['CSCI3081', 'W']
    )
    assert_eq(
      StringSplitter.separate_number_suffix(self.s12),
      ['CSCI3081', 'W']
    )
