import sympy
from sympy.parsing.latex import parse_latex


def preview(s1,s2):
    userid = input()
    s_expr = input()
    print(s_expr)

    expr = parse_latex(s_expr)

    sympy.preview(expr, viewer='file', euler=False, filename=userid+"penis.png")
