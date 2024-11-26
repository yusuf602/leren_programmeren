from test_lib import *
from math import *
def calculate_cilinder_content(diameter, height):
    return round(pi* ((diameter/2)*(diameter/2)) * height, 1)



diameter = 8
height = 5
expect_content = 251.3
calculated_content = calculate_cilinder_content(diameter,height)
name = f'test diameter: {diameter} height: {height}'
test(name, expect_content, calculated_content )

calculated_content = calculate_cilinder_content(diameter,height)
name = f'test diameter: {diameter} height: {height}'
test(name, expect_content, calculated_content )

report ()