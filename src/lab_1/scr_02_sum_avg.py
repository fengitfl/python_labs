a = (input("a:"))
b = (input("b:"))
a=a.replace(",",".",1)
b=b.replace(",",".",1)
a=float(a)
b=float(b)
print(f"sum={(a+b):.2f}; avg={((a+b)/2):.2f}")


