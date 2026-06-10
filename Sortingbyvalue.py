d = {'a': 40, 'b': 10, 'c': 30, 'd': 20}

sorted_dict = dict(sorted(d.items(), key=lambda item: item[1]))

print("Sorted Dictionary:", sorted_dict)
