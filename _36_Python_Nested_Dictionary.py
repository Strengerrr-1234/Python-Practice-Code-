course ={
    'php':{
        'duration':'3 months',
        'fees':15000
    },
    'java':{'duration':'2 months','fees':20000},
    'python':{'duration':'6 months','fees':25000}
}
print(course)
print(course['php'])
print(course['php']['fees'])

# for k,v in course.items():
#     print(k,v)

# for k,v in course.items():
#     print(k,v['duration'],v['fees'])


course['java']['fees']=200000
print(course['java']['fees'])
print(course)