import sys

a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))

if a == 0:
    if b == 0:
        if c == 0:
            print("Undetermined equation.")
            sys.exit()
        else:
            print("Contradictory equation.")
            sys.exit()
    else:
        x = -c/b
        print("Linear equation.")
        print("x = " + str(x))
        sys.exit()
else:
    delta = b*b - 4*a*c
    if delta < 0:
        print("No solutions in R.")
        sys.exit()
    elif delta == 0:
        x = -b/(2*a)
        print("One solution.")
        print("x1 = x2 = " + str(x))
        sys.exit()
    else:
        x1 = (-b-(delta**(1/2)))/(2*a)
        x2 = (-b+(delta**(1/2)))/(2*a)
        print("Two solutions.")
        print("x1 = " + str(x1))
        print("x2 = " + str(x2))
        sys.exit()
