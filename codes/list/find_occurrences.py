my_list = [1, 2, 2, 3, 4, 4, 5]
count_dict = {}
for i in my_list:
    if i in count_dict:
        count_dict[i] += 1
    else:
        count_dict[i] = 1
print(count_dict)