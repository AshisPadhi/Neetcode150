# def add(x,y) -> int:
#     return x+y

# #How lambda works
# # lmabda inputs: expression

# lambda_add= lambda x, y: x+y

# print(add(3,2))

# print(lambda_add(5,4))

data = [(1, 'apple'), (2, 'banana'), (3, 'orange')]

sorted_data=sorted(data, key= lambda data:data[1], reverse=True)

print(sorted_data)