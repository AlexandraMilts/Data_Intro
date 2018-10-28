import math   # This will import math module
#def magnitude(a,b):
    #return round(math.sqrt(a**2+b**2), 3)



def vector_dot_two(x,y,z,r):
    if (x*z+y*r) == 0:
        return 'orthogonal'
    if round(x/z, 3) == round(y/r, 3):
        return 'parallel'
    else:
        return 'null'


def vector_dot_three(a,b,c,d,e,f):
    if (a*d+b*e+c*f) == 0:
        return 'orthogonal'
    if round(a/d, 3) == round(b/e, 3) == round(c/f, 3):
        return 'parallel'
    else:
        return 'null'


print(vector_dot_two(-7.579, -7.88, 22.737, 23.64))
print(vector_dot_three(-2.029, 9.97, 4.172, -9.231, -6.639, -7.245))
print(vector_dot_three(-2.328, -7.284, -1.214, -1.821, 1.072, -2.94))
print(vector_dot_two(2.118, 4.827, 0, 0))