
def twoSum(nums, target):
    for index,num in enumerate(nums):
        res=[]
        required_num = target - num
        # list.index(ele) returns the index of element from an array
        if required_num in nums and nums.index(required_num) != index:
            #print(nums.index(required_num))
            res.append(index)
            res.append(nums.index(required_num))

            return res
    return None



arr=[3,4,5,6]

print(twoSum(arr,7))

