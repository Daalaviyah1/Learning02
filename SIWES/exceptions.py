# Using exceptions 
import sys

# exception condition when  invalid input occurs
try: 
    X = int(input("X: "))
    Y = int(input("Y: "))
except ValueError:
    print("Error: Invalid input")
    sys.exit(1)
    
# Using Exceptions condition when something happens  not to be correct
try:
    result = X / Y
except ZeroDivisionError:
    print("Error: Cannot devide by 0.")
    sys.exit(1)


print(f"{X} / {Y} = {result}")