def ydecorator(funk):
    def wrapper(a):
        b = []
        jami = 0
        for son in a:
            jami += son
            b.append(jami)
        return b
    return wrapper

@ydecorator
def natija(a):
    return a

# Misol:
a = [1, 2, 3, 4, 5]
b = natija(a)

print("a list", a)
print("b list", b)
