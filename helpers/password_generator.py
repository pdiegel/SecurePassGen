import random
import string


class PasswordGenerator:
    """This class is used to generate a random password based on the
    selected character types and password length."""

    def __init__(self):
        self.include_symbols = False
        self.include_numbers = True
        self.include_lowercase = True
        self.include_uppercase = True
        self.password_length = 15

    def generate_password(self) -> str:
        """Returns a randomly generated password based on the password
        length and the selected character types."""
        password_pool = []
        if self.include_symbols:
            password_pool += string.punctuation
        if self.include_numbers:
            password_pool += string.digits
        if self.include_lowercase:
            password_pool += string.ascii_lowercase
        if self.include_uppercase:
            password_pool += string.ascii_uppercase

        if password_pool != []:
            new_password = "".join(
                [
                    random.choice(password_pool)
                    for _ in range(self.password_length)
                ]
            )
        else:
            new_password = "No characters selected"

        return new_password

    def set_password_length(self, length: int) -> None:
        """Sets the password length."""
        self.password_length = length

    def set_include_symbols(self, include_symbols: bool) -> None:
        """Sets the include_symbols boolean attribute."""
        self.include_symbols = include_symbols

    def set_include_numbers(self, include_numbers: bool) -> None:
        """Sets the include_numbers boolean attribute."""
        self.include_numbers = include_numbers

    def set_include_lowercase(self, include_lowercase: bool) -> None:
        """Sets the include_lowercase boolean attribute."""
        self.include_lowercase = include_lowercase

    def set_include_uppercase(self, include_uppercase: bool) -> None:
        """Sets the include_uppercase boolean attribute."""
        self.include_uppercase = include_uppercase


if __name__ == "__main__":
    """This is used to test the PasswordGenerator class."""
    password_generator = PasswordGenerator()
    print(password_generator.generate_password())
