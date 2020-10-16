import time
import random
'''
# making the test array
input_array = []
for i in range(10000):
    input_array.append(random.randint(0, 100000))
'''

# setting up some variables
prefix_sum = [0] * 10


def counting_sort(array, exponent, drawData, timetick):
    output = [0] * len(array)

    # records the occurrence for each digit into prefix_sum array
    for i in range(len(array)):
        prefix_sum[int((array[i] / exponent) % 10)] += 1

    # calculate the prefix_sum of the occurrences
    for i in range(1, 10):
        prefix_sum[i] = prefix_sum[i - 1] + prefix_sum[i]

    # build the output array
    for eachNumber in reversed(array):
        prefix_sum[int((eachNumber / exponent) % 10)] -= 1
        output[prefix_sum[int((eachNumber / exponent) % 10)]] = eachNumber

    # copy the output array to input array
    for i in range(len(array)):
        if sorted(array) == array:
            break
        else:
            array[i] = output[i]
            drawData(array, ['green' if x == i else 'red' for x in range(len(array))])
            time.sleep(timetick)

    # clear the prefix_sum and counter totals
    for i in range(len(prefix_sum)):
        prefix_sum[i] = 0


def radix_sort(array, drawData, timeTick):
    # helps determine the amount of times to perform counting sort
    max_digits = max(array)

    # used later in program to get a specific digit of a number
    exponent = 1

    # calls counting sort for every possible digit
    while max_digits / exponent > 0:
        counting_sort(array, exponent, drawData, timeTick)
        exponent *= 10

    drawData(array, ['blue' for x in range(len(array))])


'''
if __name__ == '__main__':
    radix_sort(input_array)
'''
