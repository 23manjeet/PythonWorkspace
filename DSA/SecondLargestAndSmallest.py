def secondSmallest(arr):
    min = float("inf")
    secondMin = float("inf")

    for a in arr:
        if a < min:
            min = a
        elif a > min and a < secondMin:
            secondMin = a
    return secondMin


def secondLargest(arr):
    pass


if __name__ == "__main__":
    arr = [1, 14, 12, 9, 18, 3]
    print("Second smallest= ", secondSmallest(arr))
    # print("Second largest= ",secondLargest(arr))
