# Dictionary [key:value]   used when we have multiple variables and we need to
#                          collect and store in single format
# Mutable and Unordered

info = {
    "name" : "Satinder",
    "cgpa" : 9.2,
    "subjects" : ["maths", "science"],
    3.14 : "PI"
}
print(info)
print(info["name"])
info["cgpa"] = 9.6
print(info)

# Dictionary Methods

# d.keys() : returns all keys

dict_keys = info.keys()
print(dict_keys)

# d.values() : returns all values

dict_vals = info.values()
print(dict_vals)

# d.items() : return (key:value) pairs

print(info.items())

# d.get(val) : return val acc. to key

print(info.get("cgpa"))

# d.update(new_item) : adds new item to dict

info.update ({
    "city" : "Mumbai"
})

print(info)