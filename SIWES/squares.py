# How to import functions from another file and manupulate it
from functions import square

for i in range(10):
    print(f"the square of {i} is {square(i)}")

# Or it can be done this way 
import functions

for i in range(10):
    print(f"the square of {i} is {functions.square(i)}")
    