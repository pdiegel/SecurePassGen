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


if __name__ == "__main__":
    pgen = PasswordGenerator()
    pgen.generate_password()
