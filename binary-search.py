'''
list of number stored in an array,
we will target a specifc value to find it from array
if the targeted value is in the array Return True
Else Return False 
'''

data = [1,3,5,1,6,89,45,276,45,9,42,8,4579,2,682,4679,2,57,3,89]
target = 8

def linear_search(data, target):
    
    for i in range (len(data)):
        if data[i] == target:
            return True
    
    return False

def binary_search_interative(data, target):
    low  = 0
    high = len(data) - 1
    
    while low <= high:
        mid = (low + high) //2
        if target == data[mid]: 
            True
        elif target < data[mid]:
            high = mid - 1
        else: 
            low = mid + 1
    return False

def binary_search_recursive(data, target, low, high):
    if low > high:
        return False
    else:
        mid = (low +  high) //2     
        if target == data[mid]:
            return True
        elif target < data[mid]:
            return binary_search_recursive(data, target, low, mid - 1)
        else:
            return binary_search_recursive(data, target, mid + 1, high)

print(binary_search_interative(data, target))
print(binary_search_recursive(data, target, 0, len(data)-1))