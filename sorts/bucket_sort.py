from bubble_sort import bubble_sort_3
import math

DEFAULT_BUCKECT_SIZE = 5


def bucket_sort(collection, bucket_size=DEFAULT_BUCKECT_SIZE):
    if (len(collection) == 0):
        return 'You don\'t have any item in array'

    minVal = collection[0]
    maxVal = collection[0]

    # Find the min and max value
    for i in range(len(collection)):
        if collection[i] < minVal:
            minVal = collection[i]
        elif collection[i] > maxVal:
            maxVal = collection[i]

    # Initialize buckets
    bucket_count = math.floor((maxVal - minVal) / bucket_size) + 1

    buckets = []
    for i in range(0, bucket_count):
        buckets.append([])

    # Put values to buckets
    for i in range(len(collection)):
        buckets[math.floor((collection[i] - minVal) / bucket_size)].append(collection[i])

    sortedArray = []
    for i in range(len(buckets)):
        bubble_sort_3(buckets[i])

        for j in range(len(buckets[i])):
            sortedArray.append(buckets[i][j])

    return sortedArray


if __name__ == '__main__':
    sortedArray = bucket_sort([12, 23, 4, 5, 3, 2, 12, 81, 56, 95])
    print(sortedArray)
