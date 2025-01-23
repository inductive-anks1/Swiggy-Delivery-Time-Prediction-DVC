def secondLargest(arr, n):
    max = arr[0]
    sec_max = -1
    
    for i in range(len(arr)):
        if arr[i] > max:
            max = arr[i]
            sec_max = max
    return sec_max

arr = [1, 2, 3, 4, 5]
n = len(arr)

print(largestElement(arr, n))