"""
triangle.py
Author: Jack Engel
"""
def classify_triangle(a, b, c):
    """
    Function classifies triangles with inputs as given lengths of sides
    """
    if a > 200 or b > 200 or c > 200:
        return 'InvalidInput'
    if a <= 0 or b <= 0 or c <= 0:
        return 'InvalidInput'
    if not(isinstance(a, int) and isinstance(b, int) and isinstance(c, int)):
        return 'InvalidInput'
    if (a >= (b + c)) or (b >= (a + c)) or (c >= (a + b)):
        return 'NotATriangle'
    if a == b and b == c:
        return 'Equilateral'
    if ((a ** 2) + (b ** 2) == (c ** 2)) or ((a ** 2) + (c ** 2) == (b ** 2)) or ((c ** 2) + (b ** 2) == (a ** 2)):
        return 'Right'
    if (a != b) and  (b != c) and (a != b):
        return 'Scalene'
    return 'Isosceles'
