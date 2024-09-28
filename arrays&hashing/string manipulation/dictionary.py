my_dict = {'a': 1, 'b': 2, 'c': 3}

#iterate over dictionary
# for key,value in my_dict.items():
#     print(f"Key: {key} & value : {value}")

for key in sorted(my_dict):
    print(f"{key}, {my_dict[key]}")