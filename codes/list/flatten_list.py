my_list = [[1, 2], [3, 4], [5, 6]]
flat_list = [item for sublist in my_list for item in sublist]
print(flat_list)