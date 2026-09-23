"""
Find the Smallest Missing Positive Integer
Given an unsorted array of integers, find the smallest positive integer not present in the array in O(n) time and O(1) extra space.
"""
import time
import random
input_list = [random.randint(-1000, 100000) for _ in range(500000)]


def findSmallestMissingPositive_naive(orderNumbers):
    orderNumbers.sort()
    result = 1

    for n in orderNumbers:
        if n == result:
            result += 1

    return result

start = time.time()
print(findSmallestMissingPositive_naive(input_list))
end = time.time()
print("Execution time:", end - start)

def findSmallestMissingPositive_optimized(orderNumbers):
    n = len(orderNumbers)
    visited = [False for _ in range(n)]

    for number in orderNumbers:
        if number > 0 and number<=n:
            visited[number - 1] = True

    for a in range(len(visited)):
        if visited[a] == False:
            return a + 1

start = time.time()
print(findSmallestMissingPositive_optimized(input_list))
end = time.time()
print("Execution time:", end - start)

"""
The third case works by assigning each element to the corresponding index and then finding the first element in which the index and the element do not match
"""

def findSmallestMissingPositive_optimized_space(orderNumbers):

    if len(orderNumbers) == 0:
        return 1
    
    for i in range(len(orderNumbers)):

        while True:
            if orderNumbers[i] == i+1:
                break
            if orderNumbers[i] > 0 and orderNumbers[i] <= len(orderNumbers):
                number_to_switch = orderNumbers[i]
                number_to_take = orderNumbers[number_to_switch - 1]
                if number_to_switch != number_to_take:
                    orderNumbers[i] = number_to_take
                    orderNumbers[number_to_switch - 1] = number_to_switch
                else:
                    break
            else:
                break
    
    for i in range(len(orderNumbers)):
        if orderNumbers[i] != i+1:
             return i + 1
    
    return len(orderNumbers) + 1

start = time.time()
print(findSmallestMissingPositive_optimized_space([1]))
print("Execution time:", end - start)

