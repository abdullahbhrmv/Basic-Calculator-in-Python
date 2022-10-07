def qoshish(a, b):
    return a + b

def ayirish(a, b):
    return a - b

def kopaytirish(a, b):
    return a * b

def bolish(a, b):
    return a / b

print("Kalkulyator")
print("1 + qoshish")
print("2 - ayirish")
print("3 * kopaytirish")
print("4 / bolish")

tanlov = input("Tanlang 1/2/3/4: ")

a = (input("a sonini kiriting: "))
b = (input("b sonini kiriting: "))

if tanlov == "1":
    print(qoshish(a, b))

elif tanlov == "2":
    print(a, "-", b, "=", ayirish(a, b))

elif tanlov == "3":
    print(kopaytirish(a, b))

elif tanlov == "4":
    print(bolish(a, b))

else:
    print("Noto'g'ri tanlov")