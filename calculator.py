def addition(a, b):
    print(a + b)


def substraction(a, b):
    print(a - b)


def multiplication(a, b):
    print(a * b)


def division(a, b):
    print(a / b)


print("1.+")
print("2.-")
print("3.*")
print("4./")
ch = int(input("enter your choice"));
a = int(input("enter any no."));
b = int(input("enter any no."));
if ch == 1:
    print("Addition of a , b : ", addition(a, b))
elif ch == 2:
    print("Addition of a , b : ", substraction(a, b))
elif ch == 3:
    print("Addition of a , b : ", multiplication(a, b))
elif ch == 4:
    print("Addition of a , b : ", division(a, b))
