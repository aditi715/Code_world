def search_fraud_balances(balences, target):
    left = 0
    right = len(balences) -1 

    while left <= right:
        mid = left +  (right- left) // 2
        if balences[mid] == target:
            return mid
        elif balences[mid] < target:
            left =  mid + 1
        else: 
            right = mid -1

        return -1


if __name__ == "__main__":
    sorted_data = [-1, 0, 3, 5,9,12] 
    print( search_fraud_balances(sorted_data, 9))
    print( search_fraud_balances(sorted_data, 2))



