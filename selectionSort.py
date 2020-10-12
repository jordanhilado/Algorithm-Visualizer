import time

def selection_sort(data, drawData, timeTick):
    for i in range(len(data)-1):

        min_idx = i
        for j in range(i+1, len(data)):
            if data[min_idx] > data[j]:
                min_idx = j

        data[i], data[min_idx] = data[min_idx], data[i]
        drawData(data, ['green' if x == j or x == j+1 else 'red' for x in range(len(data))] )
        time.sleep(timeTick)

    drawData(data, ['blue' for x in range(len(data))])