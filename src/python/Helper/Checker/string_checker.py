class StringChecker:
  """
  Perform checks on String type object.
  """
  @staticmethod
  def is_empty(s: str) -> bool:
    """
    Check whether a string is empty.
    """
    if s is None:
      return True

    return not s.strip()

  @staticmethod
  def has_number(s: str) -> bool:
    """
    Check whether a string contains any number.
    """
    return any(char.isdigit() for char in s)

  @staticmethod
  def has_letter(s: str) -> bool:
    """
    Check whether a string contains a any letter.
    """
    return any(char.isalpha() for char in s)
  
  @staticmethod
  def has_sign(s: str) -> bool:
    """
    Check whether a string contains a any sign.
    """
    return any(
      not char.isalnum() and
      not char.isspace() for char in s
    )

  @staticmethod
  def includes(s: str, substring: str) -> bool:
    """
    Check whether a string includes a specific substring.
    """
    return substring in s
