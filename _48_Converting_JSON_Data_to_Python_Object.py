import json
d ='{"cname":"python","fees":"12000","duration":"2 months"}'

x = json.loads(d)
print(type(x))
print(x)

for a in x:
    print(a,x[a])

