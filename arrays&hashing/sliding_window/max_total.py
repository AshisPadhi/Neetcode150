# Given an array of book prices. We can take 5 continuous books. We want to take 5 continous books where the price is maximum so as to increase our profit.
# First we solve with brute force
def best_books(prices, k):
    maxtotal=0
    # we iterate over the prices array and we go till the begining index of last window (n-k+1 (7-3+1=5))
    for i in range (len(prices)-k+1):
        total=sum(prices[i:i+k])
        if total>maxtotal:
            maxtotal=total
    return maxtotal

array_of_books=[10,20,23,21,11,15,8.12,25,13]

print(best_books(array_of_books,4))