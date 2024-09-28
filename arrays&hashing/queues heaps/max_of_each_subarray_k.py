def max_subarry_k(arr,k):
    i=0
    j=k
    final=[]
    
    while(j<= len(arr)):
        tmp=arr[i:j]
        print (f"tmp={tmp}")
        i+=1
        j+=1
        max_ele=max(tmp)
        final.append(max_ele)
    
    print(final)


arr=[7,2,10,5,3,1]

max_subarry_k(arr,3)
