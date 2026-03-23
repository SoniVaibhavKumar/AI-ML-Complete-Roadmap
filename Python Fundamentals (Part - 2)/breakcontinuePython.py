# Break

i = 1
while(i <= 10):
    if(i % 6 == 0) :
        break
    print(i)
    i = i + 1
print("Outside of the loop now.....")

# Continue

i = 1
while(i <= 10):
    if(i % 3 == 0) :
        i = i + 1
        continue
    print(i)
    i = i + 1
print("Outside of the loop now.....")

# odd nums

i = 1
while(i <= 10):
    print(i)
    i = i + 2

# odd nums using continue

i = 1
while(i <= 10):
    if(i % 2 == 0):
        i = i + 1
        continue
    print(i)
    i = i + 1