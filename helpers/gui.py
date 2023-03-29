import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from config import *
from helpers.password_generator import PasswordGenerator
import random
import string


class App(ttk.Window):
    def __init__(self):
        super().__init__()
        self.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
        row = 0
        column = 0
        self.checkbox_objects = {}
        self.show_password = ttk.BooleanVar()
        self.include_symbols = ttk.BooleanVar()
        self.include_numbers = ttk.BooleanVar()
        self.include_lowercase = ttk.BooleanVar()
        self.include_uppercase = ttk.BooleanVar()

        # Create a label
        label = ttk.Label(self, text="Password Generator")
        label.grid(row=row, column=column, columnspan=2, sticky=N)
        label.config(font=("Arial", 20))
        row += 1

        label = self.create_label(self, "Password Length", row, column)
        self.password_length = self.create_single_line_entry(
            self, "password_length", row, column
        )
        row += 1

        checkboxes = {
            "show_password": [self.show_password, "Show Password", ""],
            "include_symbols": [
                self.include_symbols,
                "Include Symbols",
                "( e.g. @#$% )",
            ],
            "include_numbers": [
                self.include_numbers,
                "Include Numbers",
                "( e.g. 123456 )",
            ],
            "include_lowercase": [
                self.include_lowercase,
                "Include Lowercase",
                "( e.g. abcdefgh )",
            ],
            "include_uppercase": [
                self.include_uppercase,
                "Include Uppercase",
                "( e.g. ABCDEFGH )",
            ],
        }

        for var_name, (
            checkbox_variable,
            checkbox_label,
            checkbox_description,
        ) in checkboxes.items():
            row += 1
            label = self.create_label(self, checkbox_label, row, column)

            checkbox = self.create_checkbox(
                self, checkbox_variable, checkbox_description, row, column
            )
            self.checkbox_objects[var_name] = checkbox

        row += 1
        self.create_button(
            self,
            "Generate Password",
            row,
            column,
            self.generate_password,
        )
        column += 1
        self.password = self.create_label(
            self, "Generated Password", row, column
        )

    def create_label(self, frame, text, row, column):
        """
        Create a text label and add it to a frame.
        """
        label = ttk.Label(frame, text=text)
        label.config(font=("Arial", 12))
        label.grid(row=row, column=column, sticky=W, padx=5, pady=5)
        return label

    def create_single_line_entry(
        self, frame: ttk.Frame, name, row, column
    ) -> ttk.Entry:
        """
        Create a single-line entry widget and add it to a frame.
        """
        entry = ttk.Entry(frame, name=name)
        entry.grid(row=row, column=column + 1, sticky=W, padx=15, pady=5)
        entry.config(font=("Arial", 12))
        return entry

    def create_checkbox(
        self, frame: ttk.Frame, variable, text, row, column
    ) -> ttk.Checkbutton:
        style = ttk.Style()
        style.configure("Custom.TCheckbutton", font=("Arial", 12))

        checkbox = ttk.Checkbutton(
            frame,
            text=text,
            cursor="plus",
            style="Custom.TCheckbutton",
            variable=variable,
        )
        checkbox.grid(row=row, column=column + 1, sticky=W, padx=15, pady=5)
        checkbox.invoke()
        checkbox.invoke()

        return checkbox

    def create_button(
        self, frame: ttk.Frame, text, row, column, command
    ) -> ttk.Button:
        button = ttk.Button(frame, text=text, command=command)
        button.grid(row=row, column=column, padx=5, pady=5, ipadx=15, ipady=5)
        return button

    def get_include_symbols(self):
        return self.include_symbols.get()

    def get_include_numbers(self):
        return self.include_numbers.get()

    def get_include_lowercase(self):
        return self.include_lowercase.get()

    def get_include_uppercase(self):
        return self.include_uppercase.get()

    def get_show_password(self):
        return self.show_password.get()

    def get_password_length(self):
        try:
            return int(self.password_length.get())
        except ValueError:
            raise ValueError("Password length must be an integer.")

    def generate_password(self) -> None:
        password_pool = []
        if self.get_include_symbols():
            password_pool += string.punctuation
        if self.get_include_numbers():
            password_pool += string.digits
        if self.get_include_lowercase():
            password_pool += string.ascii_lowercase
        if self.get_include_uppercase():
            password_pool += string.ascii_uppercase

        try:
            password_length = self.get_password_length()
            if password_length < 1:
                raise ValueError("Password length must be at least 1.")
        except ValueError as error:
            print(error)
            return ""

        if password_pool:
            new_password = "".join(
                [random.choice(password_pool) for _ in range(password_length)]
            )
            print(new_password)
            self.password.config(text=new_password)
        else:
            print("No characters selected")
