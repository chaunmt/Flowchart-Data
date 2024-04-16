class StringChecker:
  """
  A class to perform string check
  """

  @staticmethod
  def has_number(s: str) -> bool:
    """
    Check whether a string contains any number
    """
    return any(char.isdigit() for char in s)

  @staticmethod
  def has_word(s: str, word: str) -> bool:
    """
    Check whether a string contains a specific word
    """
    return word in s

  @staticmethod
  def includes(s: str, substring: str) -> bool:
    """
    Check whether a string includes a specific substring
    """
    return substring in s
