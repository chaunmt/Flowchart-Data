"""
This module contains tests for string's filter.
"""

# pylint: disable=protected-access

import pytest
from ...filter.string import (
    StringComponent,
    StringFilter,
    StringFilterAlpha,
    StringFilterBracket,
    StringFilterNumeric,
    StringFilterSign,
    StringFilterSpace
)

class TestStringFilter():
    """
    This class contains tests for the StringFilter class.
    """

    ###############################################################################
    def test_init(self):
        """
        This method contains tests for the init method.
        """
        # Correct type
        sf = StringFilter(StringComponent("ayo"))
        assert sf._s._s == "ayo"

        sf = StringFilter(StringComponent("@$90 asfuh0 1-1 !"))
        assert sf._s._s == "@$90 asfuh0 1-1 !"

        # Wrong type
        with pytest.raises(TypeError) as _:
            assert StringFilter("just a string")
            assert StringFilter(10)
            assert StringFilter(True)
            assert StringFilter(None)

    ###############################################################################
    def test_value(self):
        """
        This method contains tests for the value method.
        """
        sf = StringFilter(StringComponent("ayo"))
        assert sf.value._s == "ayo"

        sf = StringFilter(StringComponent("@$90 asfuh0 1-1 !"))
        assert sf.value._s == "@$90 asfuh0 1-1 !"

    ###############################################################################
    def test_process(self):
        """
        This method contains tests for the process method.
        """
        # Helper class to decorate the return value with texts
        class TextDecorator(StringFilter):
            """
            This decorator adds a text to check the nested behavior
            of StringFilter's process method.
            """

            def process(self):
                """
                Add a text to the return component.
                """
                return f"Processed: {self._s.process()}"

        # Initialize variables
        neststr = "my string"
        sf = StringComponent(neststr)

        # Check nested value
        for _ in range(1, 6):
            sf = TextDecorator(sf)              # Neste decorator
            s = sf.process()                    # Process all nested decorator
            neststr = f"Processed: {neststr}"   # Expected value
            assert s == neststr

class TestStringFilterSpace():
    """
    This class contains tests for the StringFilterSpace class.
    """
    def test_process(self):
        """
        This method contains tests for the process method.
        """
        # Define a list of test strings and their expected outputs
        test_cases = [
            ("my string 123", "mystring123"),         # Contains spaces and numbers
            ("hello @world!", "hello@world!"),        # Contains spaces and special character
            ("  spaced out text  ", "spacedouttext")  # Leading, trailing, and multiple spaces
        ]

        # Iterate over each test case
        for original_str, expected_str in test_cases:
            # Initialize the StringComponent
            sf = StringComponent(original_str)

            # Check nested value
            for _ in range(1, 3):
                sf = StringFilterSpace(sf)          # Nest filter
                s = sf.process()                    # Process all nested filters

                # Assert value
                assert s == expected_str, (
                    f"Failed for original string = '{original_str}'." +
                    f"Processed string = '{s}' is not the same as '{expected_str}'."
                )

class TestStringFilterSign:
    """
    This class contains tests for the StringFilterSign class.
    """
    def test_process(self):
        """
        This method contains tests for the process method.
        """
        # Define a list of test strings and their expected outputs
        test_cases = [
            ("hello@world!", "helloworld"),            # Special character '@' and '!'
            ("greeting$%^", "greeting"),               # Multiple signs
            ("123 !@# abc", "123abc"),                 # Mixed with digits and letters
            ("  spaced out text  ", "spacedouttext")   # Leading, trailing, and multiple spaces
        ]

        # Iterate over each test case
        for original_str, expected_str in test_cases:
            # Initialize the StringComponent
            sf = StringComponent(original_str)

            # Check nested value
            for _ in range(1, 3):
                sf = StringFilterSign(sf)           # Nest filter
                s = sf.process()                    # Process all nested filters

                # Assert value
                assert s == expected_str, (
                    f"Failed for original string = '{original_str}'." +
                    f"Processed string = '{s}' is not the same as '{expected_str}'."
                )


class TestStringFilterBracket:
    """
    This class contains tests for the StringFilterBracket class.
    """
    def test_process(self):
        """
        This method contains tests for the process method.
        """
        # Define a list of test strings and their expected outputs
        test_cases = [
            ("text with (round) brackets", "text with round brackets"),
            ("{curly} and [square]", "curly and square"),
            ("(nested{brackets[example]})", "nestedbracketsexample")
        ]

        # Iterate over each test case
        for original_str, expected_str in test_cases:
            # Initialize the StringComponent
            sf = StringComponent(original_str)

            # Check nested value
            for _ in range(1, 3):
                sf = StringFilterBracket(sf)        # Nest filter
                s = sf.process()                    # Process all nested filters

                # Assert value
                assert s == expected_str, (
                    f"Failed for original string = '{original_str}'." +
                    f"Processed string = '{s}' is not the same as '{expected_str}'."
                )

class TestStringFilterAlpha:
    """
    This class contains tests for the StringFilterAlpha class.
    """
    def test_process(self):
        """
        This method contains tests for the process method.
        """
        # Define a list of test strings and their expected outputs
        test_cases = [
            ("hello123", "123"),          # Letters with digits
            ("ABCdef456", "456"),         # Mixed case letters with digits
            ("OnlyAlphaHere!", "!")       # Letters with a special character
        ]

        # Iterate over each test case
        for original_str, expected_str in test_cases:
            # Initialize the StringComponent
            sf = StringComponent(original_str)

            # Check nested value
            for _ in range(1, 3):
                sf = StringFilterAlpha(sf)          # Nest filter
                s = sf.process()                    # Process all nested filters

                # Assert value
                assert s == expected_str, (
                    f"Failed for original string = '{original_str}'." +
                    f"Processed string = '{s}' is not the same as '{expected_str}'."
                )

class TestStringFilterNumeric:
    """
    This class contains tests for the StringFilterNumeric class.
    """
    def test_process(self):
        """
        This method contains tests for the process method.
        """
        # TODO
