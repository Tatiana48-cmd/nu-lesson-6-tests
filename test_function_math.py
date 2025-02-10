import math
from function_math import const_sqrt, const, perpendicular, base

if round(math.pi, 5) != 3.14159:
    print("Failed")
elif math.sqrt(const_sqrt) != 3:
    print('Failed')
elif round(math.pow(const_sqrt, const), 3) != 990107.875:
    print('Failed')
elif math.hypot(perpendicular, base) != 5:
    print('Failed')
else:
    print("Success")