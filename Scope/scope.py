username= "sandip"
x=99
def f1():
    x=88
    def f2():
        print(x)
    f2()
f1()
print(x)

def c1(num):
    def c2(x):
        return x**num
    return c2
f=c1(2)
g=c1(3)

print(f(3))
print(g(3))
        