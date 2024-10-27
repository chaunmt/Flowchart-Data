"""
This class contains multiple classes to help define new types for decorators (filter etc.).
"""

class StringComponent:
    """
    A string component class consists of a private string variable
    that can be wrapped in decorators like StringFilter's children class.
    """

    #####################################
    def __init__(
            self,
            s: str
        ) -> None:
        """
        Initialize a string object.
        """
        self._s = s

    #####################################
    def process(self) -> dict:
        """
        Process the object.
        """
        return self._s
