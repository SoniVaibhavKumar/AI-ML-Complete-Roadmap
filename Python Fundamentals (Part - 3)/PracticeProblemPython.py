info = [
    ("Alice", "Math"),
    ("Bob", "Science"),
    ("Alice", "Science"),
    ("Charlie", "Math"),
    ("Bob", "Math"),
    ("Alice", "English"),
    ("Charlie", "English")
]

for name, course in info:
    print(name)
    print(course)
    print(name, course)

for name, course in info:
    if course == "English":
        print(name)

info1 = [
    ("Alice", "Math"),
    ("Bob", "Science"),
    ("Alice", "Science"),
    ("Charlie", "Math"),
    ("Bob", "Math"),
    ("Alice", "English"),
    ("Charlie", "English")
]

courses_set = set()
for item in info1:
    courses_set.add(item[1])

print(courses_set)

dict = {}
for name, course in info:
    if(dict.get(name) == None):
        dict.update({name : set()})
        dict[name].add(course)
    else :
        dict[name].add(course)
print(dict)