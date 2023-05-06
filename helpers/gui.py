import ttkbootstrap as ttk
from ttkbootstrap.constants import W, N
from config import WINDOW_HEIGHT, WINDOW_WIDTH


class App(ttk.Window):
    """This class represents the GUI for the application."""

    def __init__(self, password_generator):
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
        self.password_generator = password_generator

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
            self.password_generator,
        )
        column += 1
        self.password = self.create_label(
            self, "Generated Password", row, column
        )

    def create_label(
        self,
        frame,
        text,
        row,
        column,
    ) -> ttk.Label:
        """Creates and returns a tkinter text label."""
        label = ttk.Label(frame, text=text)
        label.config(font=("Arial", 12))
        label.grid(row=row, column=column, sticky=W, padx=5, pady=5)
        return label

    def create_single_line_entry(
        self,
        frame: ttk.Frame,
        name,
        row,
        column,
    ) -> ttk.Entry:
        """Creates and returns a tkinter entry widget."""
        entry = ttk.Entry(frame, name=name)
        entry.grid(row=row, column=column + 1, sticky=W, padx=15, pady=5)
        entry.config(font=("Arial", 12))
        return entry

    def create_checkbox(
        self,
        frame: ttk.Frame,
        variable,
        text,
        row,
        column,
    ) -> ttk.Checkbutton:
        """Creates and returns a tkinter checkbox widget."""
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
        self,
        frame: ttk.Frame,
        text,
        row,
        column,
        command,
    ) -> ttk.Button:
        """Creates and returns a tkinter button widget."""
        button = ttk.Button(frame, text=text, command=command)
        button.grid(row=row, column=column, padx=5, pady=5, ipadx=15, ipady=5)
        return button

    def get_include_symbols(self) -> bool:
        """Returns a boolean value indicating if symbols should be
        included in the password."""
        return self.include_symbols.get()

    def get_include_numbers(self) -> bool:
        """Returns a boolean value indicating if numbers should be
        included in the password."""
        return self.include_numbers.get()

    def get_include_lowercase(self) -> bool:
        """Returns a boolean value indicating if lowercase letters
        should be included in the password."""
        return self.include_lowercase.get()

    def get_include_uppercase(self) -> bool:
        """Returns a boolean value indicating if uppercase letters
        should be included in the password."""
        return self.include_uppercase.get()

    def get_show_password(self) -> bool:
        """Returns a boolean value indicating if the password should be
        shown."""
        return self.show_password.get()

    def get_password_length(self) -> int:
        """Returns the password length as an integer."""
        try:
            return int(self.password_length.get())
        except ValueError:
            raise ValueError("Password length must be an integer.")

        else:
            print("No characters selected")
