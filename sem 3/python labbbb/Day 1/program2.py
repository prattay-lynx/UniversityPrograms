import cmath
a=int(input("Enter a number "))
b=int(input("Enter a number "))
c=int(input("Enter a number "))
dis = (b**2) - (4*a*c)
a1 = (-b-cmath.sqrt(dis))/(2 * a)
a2 = (-b+cmath.sqrt(dis))/(2 * a)
print('The roots are')
print(a1)
print(a2)