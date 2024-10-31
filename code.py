def sort(width, height, length, mass):
    # Calculate volume
    volume = width * height * length
    
    # Determine if package is bulky
    is_bulky = volume >= 1_000_000 or width >= 150 or height >= 150 or length >= 150
    
    # Determine if package is heavy
    is_heavy = mass >= 20
    
    # Sorting logic based on criteria
    if is_heavy and is_bulky:
        return "REJECTED"
    elif is_heavy or is_bulky:
        return "SPECIAL"
    else:
        return "STANDARD"

# Testing the function with sample inputs
print(sort(200, 100, 50, 10))   # Expected output: "SPECIAL" (bulky due to large width)
print(sort(50, 50, 50, 25))     # Expected output: "SPECIAL" (heavy due to mass)
print(sort(200, 200, 200, 25))  # Expected output: "REJECTED" (both heavy and bulky)
print(sort(50, 50, 50, 5))      # Expected output: "STANDARD" (neither bulky nor heavy)
