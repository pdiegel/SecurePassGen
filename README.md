# Password Generator

This repository contains a simple yet customizable password generator application developed using Python and the ttkbootstrap library. The application generates random passwords based on user-selected criteria, such as password length and character types (symbols, numbers, lowercase and uppercase letters).

## Features

- User-friendly GUI
- Customizable password length
- Options to include/exclude:
  - Symbols (e.g., @#$%)
  - Numbers (e.g., 123456)
  - Lowercase letters (e.g., abcdefgh)
  - Uppercase letters (e.g., ABCDEFGH)

## Installation

1. Clone the repository:
`git clone https://github.com/username/password-generator.git`

2. Change to the project directory:
`cd password-generator`

3. Create a virtual environment:
`python -m venv venv`

4. Activate the virtual environment:

- On Windows:
    `venv\Scripts\activate`
- On Linux or macOS:
    `source venv/bin/activate`

5. Install the required packages:
`pip install -r requirements.txt`

## Usage

1. Run the application:
`python main.py`

2. Adjust the password criteria using the available options in the GUI.
3. Click the "Generate Password" button to generate a random password based on the selected criteria.
4. The generated password will be displayed in the "Generated Password" label.

## Repository Structure

- `main.py`: The main entry point of the application.
- `config.py`: Contains global configuration variables, such as window dimensions.
- `helpers/controller.py`: Contains the `Controller` class, which manages interactions between the GUI and the password generator.
- `helpers/gui.py`: Contains the `App` class, which represents the GUI for the password generator.
- `helpers/password_generator.py`: Contains the `PasswordGenerator` class, which generates random passwords based on the user's selected criteria.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT License](https://chat.openai.com/LICENSE)
