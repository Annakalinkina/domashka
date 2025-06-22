class StringUtils:
    @staticmethod
    def reverse_string(s: str) -> str:
        """Возвращает перевернутую строку."""
        if not isinstance(s, str):
            raise ValueError("Input must be a string")
        return s[::-1]

    @staticmethod
    def is_palindrome(s: str) -> bool:
        """Проверяет, является ли строка палиндромом."""
        s = s.replace(" ", "").lower()
        return s == s[::-1]

    @staticmethod
    def count_vowels(s: str) -> int:
        """Считает количество гласных в строке."""
        if not isinstance(s, str):
            raise ValueError("Input must be a string")
        vowels = 'aeiouAEIOU'
        return sum(1 for char in s if char in vowels)

    @staticmethod
    def to_uppercase(s: str) -> str:
        """Возвращает строку в верхнем регистре."""
        if not isinstance(s, str):
            raise ValueError("Input must be a string")
        return s.upper()