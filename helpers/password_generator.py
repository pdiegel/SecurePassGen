import random
import string


class PasswordGenerator:
    def __init__(self):
        self.include_symbols = False
        self.include_numbers = True
        self.include_lowercase = True
        self.include_uppercase = True
        self.password_length = 15

    def generate_password(self) -> str:
        password_pool = []
        if self.include_symbols:
            password_pool += string.punctuation
        if self.include_numbers:
            password_pool += string.digits
        if self.include_lowercase:
            password_pool += string.ascii_lowercase
        if self.include_uppercase:
            password_pool += string.ascii_uppercase

        new_password = "".join(
            [random.choice(password_pool) for _ in range(self.password_length)]
        )

        return new_password

    def set_password_length(self, length: int) -> None:
        self.password_length = length

    def set_include_symbols(self, include_symbols: bool) -> None:
        self.include_symbols = include_symbols

    def set_include_numbers(self, include_numbers: bool) -> None:
        self.include_numbers = include_numbers

    def set_include_lowercase(self, include_lowercase: bool) -> None:
        self.include_lowercase = include_lowercase

    def set_include_uppercase(self, include_uppercase: bool) -> None:
        self.include_uppercase = include_uppercase


if __name__ == "__main__":
    password_generator = PasswordGenerator()
    print(password_generator.generate_password())
