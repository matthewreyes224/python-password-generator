# Python Password Generator

A command-line password generator written in Python that uses the `secrets` module for cryptographically secure random character selection.

## Features

- Generates a 15-character password by default
- Supports custom password lengths of 15 characters or more
- Uses lowercase letters, uppercase letters, numbers, and punctuation
- Uses Python's `secrets` module instead of `random`
- Includes menu input validation and custom-length validation
- Allows repeated password generation without restarting the program

## Why `secrets`?

Python's `random` module is designed for simulations and general-purpose randomness. The `secrets` module is intended for security-sensitive values such as passwords, authentication tokens, and similar credentials.

## Requirements

- Python 3.6 or newer
- No third-party packages required

## Run the Program

Clone the repository and run:

```bash
python password_generator.py
```

The program presents the following menu:

```text
=== Password Generator ===

1. Generate 15 Character Password
2. Generate Custom Length Password
3. Exit
```

## Example

```text
Please choose 1, 2, or 3: 1

Your password is: [securely generated password]

Generate another password? (y/n):
```

## Security Notes

The generated password is created locally and is not stored by the program. Password generation uses `secrets.choice()`, which relies on a cryptographically secure source of randomness provided by the operating system.

This project is intended as a Python and cybersecurity portfolio project demonstrating secure random generation, input validation, loops, conditionals, exception handling, and use of Python's standard library.

## Author

Matthew Reyes
