# Write a program where you receive a number n. You have to consecutive numbers where the sum of these numbers is equal to n.
# find all possible solutions

def add_sum(index, arr, n) -> list:
    sum=0
    tmp=[]
    for i in range(index,n+1):
        sum = sum+i
        if sum < n:
            tmp.append(i)
        if sum == n:
            tmp.append(i)
            return tmp
        if sum > n:
            break
    return [] 

def sum_equals_n(n):
    final_sol=[]
    list_n = [ i for i in range(1,n+1)]

    #How to add condition in list comprehension
    # list_n = [i for i in range(n+1) if i!=0 ]

    j=0
    while (j<n):
        tmp=add_sum(j,list_n, n)
        if len(tmp)!=0:
            final_sol.append(tmp)
        j+=1
        


    print(final_sol)

sum_equals_n(21)
