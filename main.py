class MyTuple(tuple):
    def __lt__(self, other):
        return self[0] < other[0] and self[1] < other[1]
    def __gt__(self, other):
        return self[0] > other[0] and self[1] > other[1]


input_ = '''64, 120
65, 100
70, 150
56, 90
75, 190
60, 95
'''

tuple_data = (MyTuple(eval(line)) for line in input_.splitlines())
sorted_data = sorted(tuple_data)

i = 1
while i < len(sorted_data):
    if (sorted_data[i-1] < sorted_data[i]):
        i += 1
    else:
        sorted_data.pop(i-1)

print(sorted_data)
