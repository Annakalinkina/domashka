import pytest
from string_utils import StringUtils


class TestStringUtils:

    def test_reverse_string(self):
        assert StringUtils.reverse_string("hello") == "olleh"
        assert StringUtils.reverse_string("world") == "dlrow"
        assert StringUtils.reverse_string("") == ""

    def test_reverse_string_invalid(self):
        with pytest.raises(ValueError):
            StringUtils.reverse_string(123)

    def test_is_palindrome(self):
        assert StringUtils.is_palindrome("level") is True
        assert StringUtils.is_palindrome("A man a plan a canal Panama") is True
        assert StringUtils.is_palindrome("hello") is False


    def test_count_vowels(self):
        assert StringUtils.count_vowels("hello") == 2
        assert StringUtils.count_vowels("sky") == 0
        assert StringUtils.count_vowels("") == 0

    def test_count_vowels_invalid(self):
        with pytest.raises(ValueError):
            StringUtils.count_vowels(123)


    def test_to_uppercase(self):
        assert StringUtils.to_uppercase("hello") == "HELLO"
        assert StringUtils.to_uppercase("WORLD") == "WORLD"

    def test_to_uppercase_invalid(self):
        with pytest.raises(ValueError):
            StringUtils.to_uppercase(123)