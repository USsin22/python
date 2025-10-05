import math

def paint_calc(height, width, coverage_per_liter, can_size_liter):
    area = height * width
    liters_needed = area / coverage_per_liter
    cans_needed = math.ceil(liters_needed / can_size_liter)
    print(f"You'll need {liters_needed:.2f} liters of paint.")
    print(f"That's {cans_needed} cans of {can_size_liter}L each.")

test_h = float(input("Height of wall (m): "))
test_w = float(input("Width of wall (m): "))
coverage_per_liter = 10
can_size_liter = float(input("Can size (liter): "))

paint_calc(test_h, test_w, coverage_per_liter, can_size_liter)
