import sympy

x = sympy.symbols("x")

formula = sympy.Integral(sympy.sin(x)/(1+x**2), (x, 0, sympy.pi/2))
answer = formula.evalf()

print(answer)
