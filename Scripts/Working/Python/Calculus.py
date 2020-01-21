#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3.7
import sympy

x = sympy.symbols('x')
dif = sympy.diff(sympy.cos(x),x)
print('The derivative of cos(x) is', dif) 

inte = sympy.integrate(-sympy.sin(x),x)
print('The integral of -sin(x) is', inte) 
