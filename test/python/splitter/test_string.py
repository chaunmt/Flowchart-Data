
from src.python.splitter.string import StringSplitter

# Test StringSplitter class
class TestStringSplitter:

    def test_at_index(self):
        # Test case for the StringSplitter's at_index method
        assert StringSplitter.at_index("abcdef", 2) == ['abc', 'def']
        assert StringSplitter.at_index("abcdef", 0) == ['a', 'bcdef']
        assert StringSplitter.at_index("abcdef", 5) == ['abcdef', '']
        assert StringSplitter.at_index("a", 0) == ['a', '']
        assert StringSplitter.at_index("a", 4) == ['a', ''] #not sure if this is the intended functionality
        assert StringSplitter.at_index("", 2) == []
        
    def test_at_substring(self):
        assert StringSplitter.at_substring("hello world", " ") == ["hello", "world"]
        assert StringSplitter.at_substring("", " ") == []
        assert StringSplitter.at_substring("hello world", "x") == ["hello world"]
        assert StringSplitter.at_substring("apple|banana|cherry", "|") == ["apple", "banana", "cherry"]
        assert StringSplitter.at_substring("|apple|banana|", "|") == ["", "apple", "banana", ""]


    def test_at_first_type_occurrence(self):
        assert StringSplitter.at_first_type_occurrence("123abc456", "letter") == ["123", "abc456"]
        assert StringSplitter.at_first_type_occurrence("abc123def", "number") == ["abc", "123def"]
        assert StringSplitter.at_first_type_occurrence("123456", "letter") == ["123456", None]
        assert StringSplitter.at_first_type_occurrence("abcdef", "number") == ["abcdef", None]
        assert StringSplitter.at_first_type_occurrence("", "letter") == [None, None]

        # Test invalid split_type
        try:
            StringSplitter.at_first_type_occurrence("abc123", "symbol")
        except ValueError as e:
            assert str(e) == "split_type can only be either 'letter' or 'number'"


    def test_at_last_type_occurrence(self):
        assert StringSplitter.at_last_type_occurrence("123abc456", "letter") == ["123abc", "456"]
        assert StringSplitter.at_last_type_occurrence("abc123def", "number") == ["abc123", "def"]
        assert StringSplitter.at_last_type_occurrence("123456", "letter") == ["123456", None]
        assert StringSplitter.at_last_type_occurrence("abcdef", "number") == ["abcdef", None]
        assert StringSplitter.at_last_type_occurrence("", "letter") == [None, None]

        # Test invalid split_type
        try:
            StringSplitter.at_last_type_occurrence("abc123", "symbol")
        except ValueError as e:
            assert str(e) == "split_type can only be either 'letter' or 'number'"

    def test_to_letter_or_digit_substrs(self):
        assert StringSplitter.to_letter_or_digit_substrs("abc123def456") == ["abc", "123", "def", "456"]
        assert StringSplitter.to_letter_or_digit_substrs("abcdef") == ["abcdef"]
        assert StringSplitter.to_letter_or_digit_substrs("123456") == ["123456"]
        assert StringSplitter.to_letter_or_digit_substrs("") == []
        assert StringSplitter.to_letter_or_digit_substrs("abc123!@#def456") == ["abc", "123", "def", "456"]
