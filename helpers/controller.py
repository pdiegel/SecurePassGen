from helpers.gui import App
from helpers.password_generator import PasswordGenerator


class Controller:
    def __init__(self):
        self.app = App(self.generate_password)
        self.password_generator = PasswordGenerator()

    def get_app_inputs(self):
        password_length = self.app.get_password_length()
        self.password_generator.set_password_length(password_length)

        self.include_symbols = self.app.get_include_symbols()
        self.password_generator.set_include_symbols(self.include_symbols)

        self.include_numbers = self.app.get_include_numbers()
        self.password_generator.set_include_numbers(self.include_numbers)

        self.include_uppercase = self.app.get_include_uppercase()
        self.password_generator.set_include_uppercase(self.include_uppercase)

        self.include_lowercase = self.app.get_include_lowercase()
        self.password_generator.set_include_lowercase(self.include_lowercase)

    def generate_password(self):
        self.get_app_inputs()
        new_password = self.password_generator.generate_password()
        self.app.password.config(text=new_password)
