def best_books(prices, k):
    max_total=0

    if len(prices) < k:
        return 0
    local_sum=sum(prices[:k])
    max_total = local_sum

    for i in range(len(prices)-k):
        local_sum=local_sum - prices[i] + prices[i+k]
        max_total=max(max_total,local_sum)

    return max_total
    
array_of_books=[10,20,23,21,11,15,8.12,25,13]

print(best_books(array_of_books,4))   

