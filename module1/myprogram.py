import function
area = function.calculate_square_area(5)
print(area)

"""
Q.to import as a another name

import functions as f
area = f.calculate_square_area(5)
print(area)
"""
"""
Q. if modules is in another sub folder

import modules.function as f
area = f.calculate_square_area(5)
print(area)
"""

"""
Q. if modules is in totally diffrent directory

import sys
sys.path.append("c:\code") #your module path
import functions as f
area = f.calculate_Square_area(10)
area = f.calculate_triangle_area(5,10)
print(area)

"""
