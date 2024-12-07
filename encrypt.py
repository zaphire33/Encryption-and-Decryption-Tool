import random
import string
import json

class SimpleEncryptionTool:
    def __init__(self):
        self.key = {}

    def generate_key(self):
        chars = list(string.ascii_letters + string.digits + string.punctuation)
        shuffled_chars = chars[:]
        random.shuffle(shuffled_chars)
        self.key = dict(zip(chars, shuffled_chars))
        with open("encryption_key.json", "w") as file:
            json.dump(self.key, file)
        print("Encryption key generated and saved as 'encryption_key.json'.")

    def load_key(self):
        try:
            with open("encryption_key.json", "r") as file:
                self.key = json.load(file)
            print("Encryption key loaded successfully.")
        except FileNotFoundError:
            print("Key file not found. Generate a new key first.")

    def encrypt(self, message):
        if not self.key:
            print("No key found. Please generate or load a key first.")
            return None
        encrypted = "".join([self.key.get(char, char) for char in message])
        print(f"Encrypted Message: {encrypted}")
        return encrypted

    def decrypt(self, encrypted_message):
        if not self.key:
            print("No key found. Please generate or load a key first.")
            return None
        reverse_key = {v: k for k, v in self.key.items()}
        decrypted = "".join([reverse_key.get(char, char) for char in encrypted_message])
        print(f"Decrypted Message: {decrypted}")
        return decrypted

if __name__ == "__main__":
    tool = SimpleEncryptionTool()

    while True:
        print("\nOptions:")
        print("1. Generate Encryption Key")
        print("2. Load Encryption Key")
        print("3. Encrypt a Message")
        print("4. Decrypt a Message")
        print("5. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            tool.generate_key()
        elif choice == "2":
            tool.load_key()
        elif choice == "3":
            message = input("Enter the message to encrypt: ").strip()
            tool.encrypt(message)
        elif choice == "4":
            encrypted_message = input("Enter the message to decrypt: ").strip()
            tool.decrypt(encrypted_message)
        elif choice == "5":
            print("Exiting Encryption Tool. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
