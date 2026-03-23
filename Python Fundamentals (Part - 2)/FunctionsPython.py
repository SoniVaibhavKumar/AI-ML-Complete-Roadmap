def hello():  # fnx definition
    print("Hello")
hello()  # fnx call


def sum(a, b):
    s = a + b
    return s
ans = sum(3, 4)           # we can also write
print(ans)                # print(sum(3, 4))

# User Input Average
def avg():
    aa = float(input("Enter number 1: "))
    ab = float(input("Enter number 2: "))
    ac = float(input("Enter number 3: "))
    average = (aa + ab + ac) / 3
    return average
print(avg())