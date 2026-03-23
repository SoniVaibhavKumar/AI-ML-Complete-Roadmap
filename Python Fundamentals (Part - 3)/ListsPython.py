marks = [99, 98, 89, 96, 100]
print(marks)
print(len(marks))
print(marks[4])

# Lists are mutable(Change of value is possible)
marks[2] = 91
print(marks)

#Lists can contain values of different datatypes and slicing of lists is possible
lists = [99, 99, 98, 89, 91, "abc", 100.99]
print(lists[:5])


# Append : Add one element at the end

nums = [1, 2, 3]
nums.append(4)
print(nums)

# Insert : Insert element at index value

nums.insert(2, 10)
print(nums)

# sort : Arranges in increasing order

nums.sort()
print(nums)

# reverse : Reverses order

nums.reverse()
print(nums)



# Loops in lists

numss = [1, 2, 3, 10, 4]
for val in numss:
    print(val)

# Find an element in lists

number = [1, 2, 3, 10, 4]
x = 10
idx = 0
for val in number:
    if(val == x):
        print(f"x found at position {idx}")
        break
    idx += 1