import json
d='{"course_name":"python","fees":"500000"}'
j=json.loads(d)
print(j)
print(type(j))

print()

d={"course_name":"python","fees":"500000"}
j=json.dumps(d)
print(j)
print(type(j))








