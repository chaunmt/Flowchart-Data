from typing import TypeVar

T = TypeVar('T')

class Filter:
  """
  The base Filter class defines the wrapping interface for other filters
  """

  # The component to be wrapped
  _component = None

  def __init__(self, component: T) -> None:
    """
    Initialize the component to be wrapped
    """
    self._component = component

  @property
  def component(self) -> T:
    """
    The property object of the private variable _component
    """
    return self._component

  def operation(self, item: T) -> T:
    """
    Filter _component with an operation and return its new value
    """
    return self._component.operation()