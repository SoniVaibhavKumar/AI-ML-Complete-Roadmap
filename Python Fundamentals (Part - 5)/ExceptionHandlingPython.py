try:
    x = int(input("enter x: "))
    ans = 10/x

except ZeroDivisionError:
    print("Divide by zero not allowed")

except ValueError:
    print("Invalid input")

else :
    print(f"ans = {ans}")

finally:
    print("end of program")