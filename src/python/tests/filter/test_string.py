"""
This module contains tests for string's filter.
"""

import pytest
from ...filter.string import StringFilter

class TestStringFilter():
    """
    This class contains tests for the StringFilter class.
    """
    
    def test_init():
        """
        """
        with pytest.raises(ValueError) as e:
            assert StringFilter(10)