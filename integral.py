from math import exp
def f(x):
    return x*exp(-x) 

# Numerically Integrate f(x) from 0 to 50
intgrl=0.0
x=0
xmax=50
dx=0.0001
while x<xmax:
    intgrl+=dx*f(x)
    x+=dx
print("Integral=",intgrl,"error=",abs(1-intgrl))

# When changing the dx value to 0.0001, the error becomes a value near 10^-10
