
import random
import string

def generate_password(length=12, use_upper=True, use_lower=True, use_digits=True, use_symbols=True):
    chars = ''
    if use_upper:
        chars += string.ascii_uppercase
    if use_lower:
        chars += string.ascii_lowercase
    if use_digits:
        chars += string.digits
    if use_symbols:
        chars += string.punctuation
    if not chars:
        raise ValueError("No character types selected!")
    return ''.join(random.choice(chars) for _ in range(length))

def main():
    print("Welcome to the Password Generator!")
    try:
        length = int(input("Enter password length (default 12): ") or 12)
    except ValueError:
        length = 12
    use_upper = input("Include uppercase letters? (y/n, default y): ").lower() != 'n'
    use_lower = input("Include lowercase letters? (y/n, default y): ").lower() != 'n'
    use_digits = input("Include digits? (y/n, default y): ").lower() != 'n'
    use_symbols = input("Include symbols? (y/n, default y): ").lower() != 'n'
    try:
        password = generate_password(length, use_upper, use_lower, use_digits, use_symbols)
        print(f"\nGenerated password: {password}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
