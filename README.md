# Enigma Machine Simulator

A Python-based simulation of the classic Enigma encryption machine, created for learning and experimenting with encryption concepts.

Features
🔐 Encryption and decryption
⚙️ Three rotors
🪞 Reflector mechanism
🔄 Automatic rotor rotation
✅ Input validation
💻 Command-line interface
🐍 Pure Python — no external libraries required
How It Works

Each character passes through three rotors and a reflector before being transformed into the encrypted character.

Input
  ↓
Rotor 1
  ↓
Rotor 2
  ↓
Rotor 3
  ↓
Reflector
  ↓
Rotor 3
  ↓
Rotor 2
  ↓
Rotor 1
  ↓
Output

The first rotor rotates after every character, while the other rotors rotate after completing a full cycle. This makes the encryption dependent on the position of each character.

Project Structure
.
├── enigma_machine.py
└── README.md

Main Components
EnigmaMachine — Handles the encryption system and machine configuration.
rotate_rotor() — Rotates the machine's rotors.
validate_message() — Validates user input.
encrypt_decrypt() — Encrypts or decrypts the message.
main() — Provides the command-line interface.
Installation

Make sure Python 3 is installed.

git clone https://github.com/your-username/your-repository.git
cd your-repository

No external dependencies are required.

Usage

Run:

python enigma_machine.py

Then enter your message:

Write the message you want to (de)crypt:
HELLO WORLD

The program will return the encrypted/decrypted message.

Technologies
Python 3
Object-Oriented Programming
Algorithms & Data Structures
Command-Line Interface
Note

This is an educational simulation inspired by the Enigma machine. It is not a historically accurate implementation and should not be used for real-world security or sensitive information.

Future Improvements
 ✅ Configurable rotor positions
 ✅ Plugboard support
 ✅ Historically accurate Enigma configuration
 ✅ Graphical User Interface
 ✅ Unit tests
