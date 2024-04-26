class StringChecker:
  """
  A class to perform checks on String type object
  """

  @staticmethod
  def has_number(s: str) -> bool:
    """
    Check whether a string contains any number
    """
    return any(char.isdigit() for char in s)

  @staticmethod
  def has_letter(s: str) -> bool:
    """
    Check whether a string contains a any letter
    """
    return any(char.isalpha() for char in s)

  @staticmethod
  def includes(s: str, substring: str) -> bool:
    """
    Check whether a string includes a specific substring
    """
    return substring in s
