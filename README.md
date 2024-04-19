# Password Manager Application

This is a simple password manager application built using Python's Tkinter library.

## Dependencies

- **Python 3.x**: Ensure you have Python 3.x installed on your system. You can download it from the [official Python website](https://www.python.org/downloads/).
- **Tkinter**: Tkinter is included with most Python installations, so you shouldn't need to install it separately.

## Usage

1. Clone or download this repository to your local machine.
2. Open a terminal or command prompt.
3. Navigate to the directory where you saved the application files.
4. Run the following command to launch the application:
  python password_manager.py

## Instructions for Windows

No additional dependencies or modifications are required to run this application on Windows.

## Instructions for Linux

To run this application on Linux, you might need to make a couple of adjustments:

- **File Paths**: Update file paths if necessary. Ensure that any file paths specified in the code (`3D Lock Icon.png`, `data.txt`) are correct for your Linux file system.
- **Executable Permission**: If you encounter permission issues when running the application, ensure that the Python script has executable permission. You can grant executable permission using the following command:
  chmod +x password_manager.py


## Instructions for macOS

This application should run on macOS without any modifications. Ensure that you have Python 3.x installed on your system.

## Functionality

This password manager application allows users to store and manage their website credentials securely. It provides the following features:

### 1. Generate Password

Users can generate strong and random passwords for their accounts by clicking the "Generate Password" button. The generated password includes a combination of letters (both uppercase and lowercase), numbers, and symbols.

### 2. Save Password

Users can save their website credentials by entering the website URL, their email or username, and the password generated or manually entered. Upon clicking the "Add" button, the application prompts the user to confirm the details before saving them to a file named `data.txt`.

### 3. Security Disclaimer

**Please Note:** This password manager does not use encryption and is not secure for storing sensitive information. It is intended for educational purposes only and should not be used to manage important passwords or confidential data.

### 4. Cross-Platform Compatibility

The application is designed to run on multiple platforms including Windows, Linux, and macOS. Instructions for running the application on different platforms are provided in the README.

### 5. User Interface

The user interface is built using Tkinter, providing a simple and intuitive interface for users to interact with the application. Users can easily navigate through the fields to enter their website credentials and generate passwords.



