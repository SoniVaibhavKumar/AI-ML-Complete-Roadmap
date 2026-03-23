# For loop   in = membership operator
string = "hello"
for var in string :
    print(var)

# in = ckecks presence of the value
word = "hello"
if 'o' in word :
    print("o exists in word")

for i in range(5):
    print(i)

# finding how many i letter is there in the given word
word = "artificial intelligence"
count = 0
for ch in word :
    if(ch == 'i'):
        count += 1
print("count of i =", count)

# finding how many vowels are there in the given word : vowel count
word = "artificial"
count = 0
for ch in word:
    if(ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u'):
        count += 1
print("ans =",count)