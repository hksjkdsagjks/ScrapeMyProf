import json

professors = []
for i in range(1, 691):
	f = open(str(i) + '.json', 'r')
	print(i)
	professors = professors + json.loads(f.read())

f = open('data.json', 'w')
f.write(json.dumps(professors))