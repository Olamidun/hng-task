# A program that calculates the area of a circle and approximates it to two decimal places
from math import pi

radius = float(input('Please enter the radius of the circle: '))

# formula for calculating area of a circle
area = pi*radius**2
# round is a function that approximates numbers to the decimal place of the number given as the second argument

approximated_area = round(area, 2)
print(f'The area of the circle is {approximated_area}, to 2 decimal place')