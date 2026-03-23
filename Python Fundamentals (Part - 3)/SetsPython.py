# Sets : collection of unique elements

s = {1, 2, 2, 2, 3}
print(s)
print(len(s))


# add(val) adds a value

s.add(5)
print(s)

# remove(val) removes a value

s.remove(1)
print(s)

# clear() empties the set
# pop() removes a random value
# s1.union(s2)

s1 = {1, 2, 3, 4, 5}
s2 = {4, 5, 8, 9, 10}
print(s1.union(s2))

# s1.intersection(s2)

print(s1.intersection(s2))