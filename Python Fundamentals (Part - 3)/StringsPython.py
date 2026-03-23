# Length of String

word = "Python"
print(len(word))

#Concatenation of two Strings

word1 = "I love "
word2 = "Python"
print(word1 + word2)

word3 = "I love "
word4 = "Python"
sentence = word3 + word4
print(sentence)

# Index

word5 = "Python"
print(word5[2])



#Slicing of strings

str = "Python"
print(str[2:4])
print(str[-4:-2])

#Formatting of strings

a = 5
b = 10
sum = a + b
print("Sum is {}".format(sum))
print("Sum of {} & {} is {}".format(a, b, sum))

print(f"Sum is {a} & {b} is {sum}")