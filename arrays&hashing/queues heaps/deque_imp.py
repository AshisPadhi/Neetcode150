from collections import deque

# deququ can be used for stack implemention
# LIFO Last in first out. Both insertion and deleteion hapens from last.
# Useful for sliding window where you frequently add and remove elements from both ends.
# d = deque()

# d.append(2)
# d.append(8)
# d.append(13)
# d.append(3)
# d.append(5)

#print(d)

# d.pop() #pops from last
# print(d)

# d.popleft()#pops from first
# print(d)

# print(d[0])

# print(d[-1])

# print(d[-2])

# d.rotate(2) #moves each element forward by positions and the end element is lopped to start (Also just remove last two element and add to the beginning.)
# print(d)

# d.rotate(-2)

# print(d)

newd = deque([9,7,4,2,7], maxlen=5)
print(newd)

newd.append(28)
print(newd)

newd.clear() #clears the deque
print(newd)