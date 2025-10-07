"""
Count Elements Greater Than Previous Average
Given an array of positive integers, return the number of elements that are strictly greater than the average of all previous elements. Skip the first element.
"""

def countResponseTimeRegressions(responseTimes):
    if len(responseTimes) <= 1:
        return 0
    
    cum_sum = responseTimes[0]
    average = cum_sum
    counter = 0
    
    for i in range(1, len(responseTimes)):
        if responseTimes[i] > average:
            print(average)
            counter += 1
        else:
            print("No")
        cum_sum += responseTimes[i]
        average = cum_sum / (i+1)
    
    return counter

input = [4, 100, 200, 150, 300, 5, 1000]
print(countResponseTimeRegressions(input))