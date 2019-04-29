def bubble_sort_1(collection):
    length = len(collection)
    for i in range(length - 1):
        for j in range(length - 1):
            if collection[j] > collection[j + 1]:
                collection[j], collection[j + 1] = collection[j + 1], collection[j]
    return collection


def bubble_sort_2(collection):
    length = len(collection)
    for i in range(length - 1):
        for j in range(length - 1 - i): # No need to for the sorted items
            if collection[j] > collection[j + 1]:
                collection[j], collection[j + 1] = collection[j + 1], collection[j]
    return collection


def bubble_sort_3(collection):
    length = len(collection)
    for i in range(length - 1):
        swapped = False
        for j in range(length - 1 - i):
            if collection[j] > collection[j + 1]:
                swapped = True
                collection[j], collection[j + 1] = collection[j + 1], collection[j]
        if not swapped: break   # No need to swap means all items have been in order
    return collection


if __name__ == '__main__':
    try:
        raw_input
    except NameError:
        raw_input = input
    user_input = input('Enter numbers separated by a comma:').strip()
    unsorted = [int(item) for item in user_input.split(',')]
    print(bubble_sort_3(unsorted))
