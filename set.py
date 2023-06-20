x = {1, 2, 3}
d = {'1': 1, '4':4}
x.update(d)
d['2'] = 2
print(({'1':1, 1:'1'}))
print(d)
print(x)

data = {'1':1, '2':2, '3':3}

s =0

while data:
    s += data.popitem()[1]

print(s)
print(sum(d.values()))
print(dir(d))
print(dir([]))

v = d.values()

import json
data = json.loads('{"one" : 1, "two" : 2, "three" : 3}')
print(data['two'])
