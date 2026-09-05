# Enigma Machine Simulator

A Python-based simulation of the classic Enigma encryption machine, built to demonstrate the concepts of substitution ciphers, rotors, reflector mapping, and rotor rotation.

The project provides a simple command-line interface where users can enter a message and receive its encrypted or decrypted version using the implemented Enigma mechanism.

Features
🔐 Encryption and decryption using the same algorithm
⚙️ Three configurable rotors
🔄 Automatic rotor rotation after each character
🪞 Reflector disk for reversible encryption
🔤 Support for alphabetic characters
␣ Support for spaces and apostrophes
✅ Input validation
💻 Simple command-line interface
🐍 Built entirely with Python
How It Works

The encryption process follows a structure inspired by the historical Enigma machine.

For each alphabetic character, the signal passes through:

Input Character
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
Encrypted Character

After processing each character, the first rotor rotates. The second and third rotors rotate after the first rotor completes a full cycle.

This changing rotor position means that the same input character can produce different output characters depending on its position in the message.

Example
Hi! Welcome to the Enigma Machine ฅʕ•̫͡•ʔฅ

Write the message you want to (de)crypt:
HELLO WORLD

(de)crypted message: ...

Running the program again with the resulting encrypted message and a fresh machine configuration can be used to reverse the encryption.

Project Structure
.
├── enigma_machine.py
└── README.md

The main implementation is contained in enigma_machine.py.

EnigmaMachine

The main class responsible for the encryption system.

It contains:

Character mappings
Three rotors
Reflector configuration
Rotor rotation logic
Input validation
Encryption/decryption logic
rotate_rotor()

Rotates a rotor by moving its first element to the end of the list.

validate_message()

Checks whether the provided message contains supported characters.

encrypt_decrypt()

Processes the message through the three rotors and reflector, while updating the rotor positions during the process.

Installation

Make sure Python 3 is installed on your system.

Clone the repository:

git clone https://github.com/your-username/your-repository.git

Navigate to the project directory:

cd your-repository

No external Python packages are required.

Usage

Run the program with:

python enigma_machine.py

Enter the message when prompted:

Write the message you want to (de)crypt:
HELLO WORLD

The program will return the processed message:

(de)crypted message: ...
Encryption & Decryption

The implementation uses a symmetric transformation. The same rotor and reflector configuration can be used for both encryption and decryption, provided the machine starts from the same initial configuration.

For example:

Original Message
       ↓
    Enigma
       ↓
Encrypted Message
       ↓
    Enigma
       ↓
Original Message

The rotor state is important. If the machine has already processed a message, its rotor positions have changed, so a new machine instance should be used when attempting to decrypt from the initial configuration.

Technologies
Python 3
Object-Oriented Programming
Lists & Dictionaries
String Manipulation
Algorithms & Data Structures
Command-Line Interface
Learning Objectives

This project was created to practice and demonstrate:

Object-oriented programming in Python
Designing classes and methods
Working with lists and dictionaries
Character mapping and substitution algorithms
Implementing reversible transformations
Understanding stateful algorithms
Input validation
Simulating mechanical encryption concepts with software
Important Note

This project is an educational simulation inspired by the Enigma machine and is not intended to be a historically accurate reproduction of the original German Enigma machines.

The rotor configurations, reflector mapping, character set, and stepping mechanism are custom implementations designed for learning and experimentation.

It should not be considered secure modern cryptography. The algorithm is intended for educational purposes rather than protecting sensitive information.

Future Improvements

Possible improvements include:

 ✅ Add configurable rotor settings
 ✅ Add support for different reflector configurations
 ✅ Implement historically accurate Enigma rotor wiring
 ✅ Add plugboard functionality
 ✅ Create a graphical user interface
 ✅ Add automated unit tests
 ✅ Improve error handling
 ✅ Add configurable initial rotor positions
 ✅ Support encryption/decryption through command-line arguments
