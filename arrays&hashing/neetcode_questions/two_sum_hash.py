def two_sum_hash(nums, target):
    seen={}
    res=[]
    for index,num in enumerate(nums):
        required = target - num
        if required in seen:

            res.append(index)
            res.append(seen[required])

            return res
        else:
            seen[num]=index
    return res


arr=[3,4,5,6]

print(two_sum_hash(arr,7))