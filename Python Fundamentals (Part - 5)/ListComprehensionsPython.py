squares = []
for i in range(6):
    squares.append(i*i)

print(squares)

sq = [i*i for i in range(6)]
print(sq)

nums = [-2, -3, 3, 4, -1, 7]
nums = [0 if val < 0 else val for val in nums]
print(nums)

words = ["hello", "python", "apnacollege"]
words = [val.upper() for val in words]
print(words)