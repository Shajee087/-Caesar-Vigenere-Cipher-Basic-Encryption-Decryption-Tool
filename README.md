# Caesar Vigenere Cipher Basic Encryption Decryption Tool
A Python implementation of classical substitution ciphers, built to demonstrate the fundamental mechanics of data confidentiality: turning plaintext into ciphertext through mathematical/programmatic logic, and reversing the process losslessly.

**Overview**

Before implementing modern cryptographic protocols (AES, RSA, etc.), it's essential to understand the core principle they all share the IPO model: Plaintext (Input) → Algorithm + Key (Process) → Ciphertext (Output). This project implements that model at its most fundamental level using a Caesar cipher (single-key shift), with a bonus Vigenère cipher (multi-key, keyword-based) implementation for stronger obfuscation.

**Features**

Caesar Cipher Encrypt/decrypt text using a single numeric shift key.

Vigenère Cipher (bonus) Encrypt/decrypt using a repeating keyword, resistant to simple frequency analysis.

Edge-case handling Preserves spaces, punctuation, and numbers; correctly handles both uppercase and lowercase letters.

Frequency analysis demo Visualizes letter distribution in ciphertext to illustrate why Caesar cipher is cryptographically weak (pattern preservation).

Symmetric key design Same key encrypts and decrypts (E_n(x) = (x+n) % 26, D_n(x) = (x-n) % 26).

**How It Works**

Convert each character to its ASCII value (ord()).

Shift the value by the key, wrapping around the 26-letter alphabet using modular arithmetic (% 26).

Convert the shifted value back to a character (chr()).

Non-alphabetic characters pass through unchanged.

pythoncipher_char = chr((ord(char) - base + shift) % 26 + base).

**Usage**

bashpython3 

Encryption Decryption Tool.py

You'll be prompted to:

Choose a cipher method (Caesar or Vigenère).

Enter the text to encrypt.

Enter a shift key (Caesar) or keyword (Vigenère).

The tool then displays the plaintext, encrypted text, and decrypted text, confirming the round-trip is lossless.

**Security Note**

The Caesar cipher is included here for educational purposes only. Its key space is tiny (only 25 possible shifts), and it preserves the underlying letter-frequency pattern of the language, making it trivially breakable via brute force or frequency analysis. It is not suitable for real-world data protection modern systems use algorithms like AES-256, which rely on confusion, diffusion, and much larger key spaces.

**Tech Stack**

Python 3

Standard library only (collections.Counter for frequency analysis)

Key Skills Demonstrated

Encryption/decryption logic, modular arithmetic, ASCII manipulation, symmetric-key cryptography concepts, and secure coding practices for edge-case handling.
