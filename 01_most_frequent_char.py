from pprint import pprint
sentence = "This is a common interview question"


obj = {}

for char in sentence:
    if char.lower() in obj:
        obj[char.lower()] += 1
    else:
        obj[char.lower()] = 1

# print(obj)
pprint(obj)

max = 0
frequent = ''
for item in obj:
    if obj[item] > max:
        max = obj[item]
        frequent = item

print(frequent)

# another way to find the max frequent is to convert the dict into tuple and sort it
sorted_tuple_list = sorted(
    obj.items(), key=lambda keyvalue: keyvalue[1], reverse=True)
pprint(sorted_tuple_list)
# print("Most frequent char: ", sorted_tuple_list[-1])
