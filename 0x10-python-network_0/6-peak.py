#!/usr/bin/python3
"""finds a peak in a list of unsorted integers"""


def find_peak(list_of_integers):
    """func - args = list_of_integers calls peak_worker"""
    if not list_of_integers:
        return None
    low = 0
    high = len(list_of_integers) - 1
    return peak_worker(list_of_integers, low, high)


def peak_worker(arr, low, high):
    """gets the mid of low and high checks if arr[mid] is > arr[mid+1] works
    the left side of mid recursivly """
    if low == high:
        return arr[low]
    mid = (low + high) // 2
    if arr[mid] > arr[mid + 1]:
        return peak_worker(arr, low, mid)
    return peak_worker(arr, mid + 1, high)
