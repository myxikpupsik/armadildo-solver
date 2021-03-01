import sympy
from sympy.parsing.sympy_parser import parse_expr

def preview(s1,s2):
    """
    derivatives of the form y' or d/dx y needs to be converted to something like
    diff(y(x),x)
    """
    userid = s1
    s_expr = s2
    print(s_expr)

    expr = parse_latex(s_expr)

    sympy.preview(expr, viewer='file', euler=False, filename=userid+"penis.png")
    return expr

def ode(expr):
    return sympy.dsolve(expr)
