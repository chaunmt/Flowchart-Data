from typing import TypeVar

T = TypeVar('T')

class Filter:
  """
  The base Filter class defines the wrapping interface for other filters.
  """
  allowed_type = T
  
  def __init__(self, item: T) -> None:
    """
    Initialize the item to be wrapped.
    """
    self._item = self.validate(item)

  @property
  def item(self) -> T:
    """
    The property object of the private variable _item.
    """
    return self._item

  def validate(self, item: T) -> T:
    """
    Validate the type of the item.
    """
    if not isinstance(item, self.allowed_type):
      raise TypeError(f"Item must be of type {self.allowed_type.__name__}")
    return item

  def process(self) -> T:
    """
    Filter _item and return its new value.
    """
    return self._item
