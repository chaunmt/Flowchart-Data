from Test.test_setup import *

class TestStringChecker(TestString):
  """
  Test module string_checker.
  """
  def test_has_number(self):
    assert StringChecker.has_number(self.s1) == False
    assert StringChecker.has_number(self.s3) == True
    assert StringChecker.has_number(self.s4) == True
    assert StringChecker.has_number(self.s5) == False
    assert StringChecker.has_number(self.s7) == False
    assert StringChecker.has_number(self.s8) == True

  def test_has_word(self):
    assert StringChecker.has_letter(self.s2) == True
    assert StringChecker.has_letter(self.s3) == False
    assert StringChecker.has_letter(self.s4) == True
    assert StringChecker.has_letter(self.s5) == True
    assert StringChecker.has_letter(self.s6) == False
    assert StringChecker.has_letter(self.s7) == False

  def test_includes(self):
    assert StringChecker.includes(self.s1, 'Hello') == True
    assert StringChecker.includes(self.s3, '123') == False
    assert StringChecker.includes(self.s4, '!0') == True
    assert StringChecker.includes(self.s6, '!@#$%^&*()') == True
    assert StringChecker.includes(self.s6, '!@#$%^&*() ') == False
    assert StringChecker.includes(self.s7, '') == True
    assert StringChecker.includes(self.s8, '') == True