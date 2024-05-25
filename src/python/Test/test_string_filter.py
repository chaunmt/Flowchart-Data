from Test.test_setup import *

class TestStringFilter(TestString):
  """
  Test cases for module string_filter
  """
  def test_string_filter_space(self):
    # Test for allowed type
    assert_eq(
      StringFilterSpace(self.s1).process(),
      'Hello,world!'
    )
    assert_eq(
      StringFilterSpace(self.s2).process(),
      'Pythonisfun!'
    )
    assert_eq(
      StringFilterSpace(self.s7).process(),
      ''
    )
    assert_eq(
      StringFilterSpace(self.s8).process(),
      '1'
    )
    assert_eq(
      StringFilterSpace(self.s9).process(),
      '1239WAD12'
    )

    # Test for disallowed type
    self.assertRaises(
      TypeError,
      StringFilterSpace, 12
    )
    self.assertRaises(
      TypeError,
      StringFilterSpace, None
    )

  def test_string_filter_signs(self):
    # Test for allowed type
    assert_eq(
      StringFilterSigns(self.s1).process(),
      'Hello and  world!'
    )
    assert_eq(
      StringFilterSigns(self.s6).process(),
      '!@#$%^ and *()'
    )
    assert_eq(
      StringFilterSigns(self.s14).process(),
      'CSCI 4041 or 3081 and 3081W or 2041 and 2021'
    )

    # Test for disallowed type
    self.assertRaises(
      TypeError,
      StringFilterSigns, 12
    )
    self.assertRaises(
      TypeError,
      StringFilterSigns, None
    )

  def test_string_filter_redundancy(self):
    # Test for allowed type
    assert_eq(
      StringFilterRedundancy(self.s2).process(),
      'Python  is   fun!'
    )
    assert_eq(
      StringFilterRedundancy(self.s3).process(),
      '12!3 !4.5'
    )
    assert_eq(
      StringFilterRedundancy(self.s4).process(),
      'C?S1!0^1'
    )
    assert_eq(
      StringFilterRedundancy(self.s7).process(),
      ''
    )
    assert_eq(
      StringFilterRedundancy(self.s8).process(),
      '   1'
    )

    # Test for disallowed type
    self.assertRaises(
      TypeError,
      StringFilterRedundancy, 12
    )
    self.assertRaises(
      TypeError,
      StringFilterRedundancy, None
    )