from sympy import Sum
from sympy.abc import k
from sympy.core import oo

print(Sum((1/(k+1)), (k, -oo, 0)).doit())
# return Sum(1/(k**2 + 1), (k, -oo, 0)) but should return 1/2 + pi/(2*tanh(pi))
print(Sum((1/(k+1)), (k, 0, oo)).doit())
# return 1/2 + pi/(2*tanh(pi))