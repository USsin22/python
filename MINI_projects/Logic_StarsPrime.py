


def print_pyramid(rows):
    for i in range(1, rows + 1):
        stars = '*' * (2 * i - 1)
        print(stars.center(2 * rows - 1))

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def main():
    print("Centered Pyramid of Stars & Prime Check")
    try:
        rows = int(input("Enter number of rows (e.g. 5): "))
        print_pyramid(rows)
        num = int(input("Enter a number to check if it's prime: "))
        if is_prime(num):
            print(f"{num} is a prime number.")
        else:
            print(f"{num} is not a prime number.")
    except ValueError:
        print("Please enter a valid integer.")

if __name__ == "__main__":
    main()
