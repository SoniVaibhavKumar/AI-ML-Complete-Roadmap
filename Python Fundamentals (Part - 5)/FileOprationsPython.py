# f = open(r"C:\Users\91778\OneDrive\Documents\Apna College - Prime AI - ML\Python Fundamentals (Part - 5)\sample.txt", "w")
# f.write("Text to overwrite \n the complete data.")
# f.close()

# f = open(r"C:\Users\91778\OneDrive\Documents\Apna College - Prime AI - ML\Python Fundamentals (Part - 5)\sample.txt", "r")
# data = f.read()
# print(data)

# f = open(r"C:\Users\91778\OneDrive\Documents\Apna College - Prime AI - ML\Python Fundamentals (Part - 5)\sample.txt", "a")
# data = f.write("New text being appended\n to the file")
# print(data)

# f = open(r"C:\Users\91778\OneDrive\Documents\Apna College - Prime AI - ML\Python Fundamentals (Part - 5)\sample.txt", "r")
# data = f.read()
# print(data)

# f= open("sample2.txt", "x")
# f.write("some random text")
# f.close()

# with open(r"C:\Users\91778\OneDrive\Documents\Apna College - Prime AI - ML\Python Fundamentals (Part - 5)\sample.txt", "r") as f:
#     data = f.read()
#     print(data)
#     print(len(data))

# Deleting files

# import os
# os.remove(r"C:\Users\91778\OneDrive\Documents\Apna College - Prime AI - ML\sample2.txt")
data = True
line = 1
word = "Python"
with open(r"C:\Users\91778\OneDrive\Documents\Apna College - Prime AI - ML\Python Fundamentals (Part - 5)\sample.txt", "r") as f:
    while data:
        data = f.readline()
        if(word in data):
            print(f"{word} found at line {line}")
            break
        line += 1