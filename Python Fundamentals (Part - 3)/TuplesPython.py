# Tuples : Immutable sequence of values

tup = (1, 2, 3, 4, 5, "abc", 100.99)
print(tup)
print(len(tup))

# Slicing in tuples

tuple = (1, 2, 3, 4, 5)
print(tuple[0:3])

# Tuples 

tu = (1, 2, 3, 4, 5)
for val in tu:
    print(val)

sum = 0
for val in tu:
    sum += val
print(f"Sum of values is {sum}")

# t.index(val) : returns 1st occurence index
tupl = (1, 2, 3, 4, 2, 5, 2, 2)
print(tupl.index(4))

# t.count(val) : counts total occurences
print(tupl.count(2))