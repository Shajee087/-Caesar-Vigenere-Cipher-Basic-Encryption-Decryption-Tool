def caesar_shift(text: str, shift: int) -> str:
    result = []

    for char in text:
        if char.isupper():
            base = ord('A')
            new_char = chr((ord(char) - base + shift) % 26 + base)
            result.append(new_char)
        elif char.islower():
            base = ord('a')
            new_char = chr((ord(char) - base + shift) % 26 + base)
            result.append(new_char)
        else:
            # Non-alphabetic: keep as-is (spaces, punctuation, numbers)
            result.append(char)

    return ''.join(result)

def caesar_encrypt(plaintext: str, shift: int) -> str:
    """Encrypts plaintext using a Caesar cipher with the given shift key."""
    return caesar_shift(plaintext, shift)

def caesar_decrypt(ciphertext: str, shift: int) -> str:
    """Decrypts ciphertext that was encrypted with the same shift key."""
    return caesar_shift(ciphertext, -shift)

def vigenere_shift(text: str, key: str, encrypt: bool = True) -> str:
    result = []
    key = key.upper()
    key_index = 0
    key_len = len(key)

    for char in text:
        if char.isalpha():
            # Each letter of the key gives a shift amount (A=0, B=1, ...)
            key_shift = ord(key[key_index % key_len]) - ord('A')
            if not encrypt:
                key_shift = -key_shift

            base = ord('A') if char.isupper() else ord('a')
            new_char = chr((ord(char) - base + key_shift) % 26 + base)
            result.append(new_char)
            key_index += 1  # only advance key on alphabetic characters
        else:
            result.append(char)

    return ''.join(result)

def vigenere_encrypt(plaintext: str, key: str) -> str:
    return vigenere_shift(plaintext, key, encrypt=True)

def vigenere_decrypt(ciphertext: str, key: str) -> str:
    return vigenere_shift(ciphertext, key, encrypt=False)

def frequency_analysis_demo(ciphertext: str):
    
    from collections import Counter
    letters_only = [c.upper() for c in ciphertext if c.isalpha()]
    freq = Counter(letters_only)
    total = sum(freq.values()) or 1

    print("\nFrequency Analysis of Ciphertext:")
    for letter, count in sorted(freq.items(), key=lambda x: -x[1]):
        pct = (count / total) * 100
        print(f"  {letter}: {'#' * count} ({pct:.1f}%)")

def main():
    print("=" * 40)
    print("Project 2: Encryption & Decryption Tool")
    print("=" * 40)
    print("\nChoose cipher method:")
    print("  1. Caesar Cipher (single shift key)")
    print("  2. Vigenère Cipher (keyword-based, bonus)")
    choice = input("Enter choice (1/2): ").strip()

    plaintext = input("\nEnter text to encrypt: ")

    if choice == "2":
        key = input("Enter keyword (letters only, e.g. 'KEY'): ").strip()
        encrypted = vigenere_encrypt(plaintext, key)
        decrypted = vigenere_decrypt(encrypted, key)
    else:
        shift = int(input("Enter shift key (e.g. 3): ").strip())
        encrypted = caesar_encrypt(plaintext, shift)
        decrypted = caesar_decrypt(encrypted, shift)

    print("\n--- Results ---")
    print(f"Plaintext : {plaintext}")
    print(f"Encrypted : {encrypted}")
    print(f"Decrypted : {decrypted}")
    print(f"Match Original? {decrypted == plaintext}")

    if choice != "2":
        frequency_analysis_demo(encrypted)

if __name__ == "__main__":
    main()