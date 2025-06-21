def f_g_raqamlar(n):
    a, b = 0, 1
    count = 0
    while count < n:
        yield a
        a, b = b, a + b
        count += 1

n = int(input("son kiriting "))
for son in f_g_raqamlar(n):
    print(son)
