import pytest
from string_utils import StringUtils


class TestStringUtils:

    @pytest.mark.parametrize(["input_data", "expected_data"], [("hello", "olleh"),
                                                               ("world", "dlrow"),
                                                               ("", "")])
    def test_reverse_string(self, input_data,expected_data):
        assert StringUtils.reverse_string(input_data) == expected_data


    def test_reverse_string_invalid(self):
        with pytest.raises(ValueError):
            StringUtils.reverse_string(123)

    @pytest.mark.parametrize(["input_data", "expected_data"], [("level", True),
                                                               ("A man a plan a canal Panama", True),
                                                               ("hello", False)])
    def test_is_palindrome(self,input_data, expected_data):
        assert StringUtils.is_palindrome(input_data) is expected_data

    @pytest.mark.parametrize(["input_data", "expected_data"], [("hello", 2),
                                                               ("sky", 0),
                                                               ("", 0)])
    def test_count_vowels(self,input_data, expected_data):
        assert StringUtils.count_vowels(input_data) ==expected_data

    def test_count_vowels_invalid(self):
        with pytest.raises(ValueError):
            StringUtils.count_vowels(123)

    @pytest.mark.parametrize(["input_data", "expected_data"], [("hello", "HELLO"),
                                                               ("WORLD", "WORLD"),
                                                               ])
    def test_to_uppercase(self,input_data, expected_data):
        assert StringUtils.to_uppercase(input_data) == expected_data


    def test_to_uppercase_invalid(self):
        with pytest.raises(ValueError):
            StringUtils.to_uppercase(123)
