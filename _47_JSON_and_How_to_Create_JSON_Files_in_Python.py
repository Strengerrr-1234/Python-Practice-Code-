import json
d = {
    'course_name':'python',
    'fees':250000
}

f = json.dumps(d)

print(type(f))
print(f)