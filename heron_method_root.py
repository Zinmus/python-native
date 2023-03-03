import sys

p = float(input("Give a number to find a root from: "))
e = float(input("Give a number for a precision: "))
if p < 0:
    print("Root number have to be >= 0.")
    sys.exit()
if e <= 0:
    print("Precision number have to be > 0.")
    sys.exit()

def algorithm(p, x, e):
    y = (x + (p/x))/2
    if x - (p/x) < e and (p/x) - x < e:
        return y
    else:
        return algorithm(p, y, e)

answer = algorithm(p, (p/2), e)
print("Answer: " + str(answer))
