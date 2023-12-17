![Cryptwarden-logo](https://github.com/BerraLeet/CryptWarden/assets/86689476/0af79e23-2ba0-4478-942f-bc60120dcf1c)

# Crypt Warden
Password Generator in Python
# Table of Contents

- [Crypt Warden](#crypt-warden)
- [Table of Contents](#table-of-contents)
  - [Desctription](#desctription)
  - [Features](#features)
  - [Dependencies](#dependencies)
  - [Usage](#usage)
    - [Terminal](#terminal)
    - [GUI](#gui)
  - [License](#license)
  - [Contributing](#contributing)


## Desctription
Crypt Warden is a password generator application built using Tkinter, allowing users to create secure passwords with customizable options. Note that the first release of Crypt Warden is a password generator in Python and will be updated. User will have possibility to use ascii letters, ascii symbols and numbers in the password. A password will be generated with secrets module in random sequences from choosen number of characters. Recommendation for a strong and secure password is to use all options and as high character set as possible. GUI APP is using customtkinter module.

## Features 
GUI APP - Generate random passwords with customizable options.
Choose password length using a slider.
Include or exclude character sets (lowercase, uppercase, numbers, symbols).
Toggle dark mode for a different visual experience.
Features a copy to clipboard button

## Dependencies
1. Python 3
2. Tkinter framework
3. pip install packaging
4. pip install customtkinter
5. pip install pyperclip

## Usage
### Terminal
pw_generator is terminal based tool where user will be prompted a few inputs where first selecting number of characters (between 6-36). After user is promted question to add each character set. User need input of "y" for yes and "n" for no.
after password is generated free to copy from terminal.

### GUI
pw_gen_gui.py is GUI based on the customtkinter module which is extension for the tkinter framework. User choose by clicking on checkboxes with each character set. 
Also GUI have the copy to clipboard basically plug and play

## License 
This project is licensed under the MIT License.

## Contributing
Feel free to contribute to this project. If you have suggestions or find issues, please open an issue or submit a pull request.



