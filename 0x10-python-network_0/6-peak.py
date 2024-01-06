#!/usr/bin/python3
"Finds peak in list of unsorted int."


def find_peak(list_of_integers):
    "Finds peak in list of unsorted int."
    if not list_of_integers:
        return None

    l, h = 0, len(list_of_integers) - 1

    while l < h:
        mid = (l + h) // 2

        if list_of_integers[mid] > list_of_integers[mid + 1]:
            high = mid
        else:
            low = mid + 1
    return list_of_integers[low]
