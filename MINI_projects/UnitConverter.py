def main():
    print("Welcome to the Unit Converter!")
    print("Select conversion type:")
    print("1. Length (meters <-> feet)")
    print("2. Weight (kilograms <-> pounds)")
    choice = input("Enter choice (1/2): ")

    if choice == "1":
        print("Length Conversion")
        print("a. Meters to Feet")
        print("b. Feet to Meters")
        sub_choice = input("Enter choice (a/b): ")
        value = float(input("Enter value: "))
        if sub_choice == "a":
            result = value * 3.28084
            print(f"{value} meters = {result:.2f} feet")
        elif sub_choice == "b":
            result = value / 3.28084
            print(f"{value} feet = {result:.2f} meters")
        else:
            print("Invalid choice.")
    elif choice == "2":
        print("Weight Conversion")
        print("a. Kilograms to Pounds")
        print("b. Pounds to Kilograms")
        sub_choice = input("Enter choice (a/b): ")
        value = float(input("Enter value: "))
        if sub_choice == "a":
            result = value * 2.20462
            print(f"{value} kilograms = {result:.2f} pounds")
        elif sub_choice == "b":
            result = value / 2.20462
            print(f"{value} pounds = {result:.2f} kilograms")
        else:
            print("Invalid choice.")
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
