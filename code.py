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

# Testing the function 
print(sort(200, 100, 50, 10))   
print(sort(50, 50, 50, 25))   
print(sort(200, 200, 200, 25))  
print(sort(50, 50, 50, 5))     
