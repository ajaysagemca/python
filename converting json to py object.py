import json
d={"cname":"python","fees":"50000"}
j=json.dumps(d)
print(j)
print(type(j))

print()
import json
d='[{"cname":"python","fees":"50000"}]'
j=json.loads(d)
print(j)
print(type(j))

