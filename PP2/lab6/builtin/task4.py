import time
import math

def sqrt_after_milliseconds(number, milliseconds):
   
    time.sleep(milliseconds / 1000)
    
    return math.sqrt(number)

number = int(input("Enter a number: "))
milliseconds = int(input("Enter milliseconds: "))

result = sqrt_after_milliseconds(number, milliseconds)

print(f"Square root of {number} after {milliseconds} milliseconds is {result}")