import json
json_str = '{"name" : "Vaibhav", "isTeacher" : true}'
py_obj = json.loads(json_str)
print(type(py_obj), py_obj)