import random
import string

print("===== PASSWORD GENERATOR =====")

# User Input
length = int(input("Enter the desired password length: "))

# Characters to be used in password
letters = string.ascii_letters
digits = string.digits
symbols = string.punctuation

all_characters = letters + digits + symbols

# Generate Password
password = ""

for i in range(length):
    password += random.choice(all_characters)

# Display Password
print("\nGenerated Password:")
print(password)
