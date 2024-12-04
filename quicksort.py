# quick sort
def quick_sort(input):
    start = 0
    end = len(input) - 1
    quick_sort_rec(input, start, end)
    return input
    
def quick_sort_rec(input, start, end):
    if start < end:
        mid = partition(input, start, end)
        quick_sort_rec(input, start, mid - 1)
        quick_sort_rec(input, mid + 1, end)

def partition(input, start, end):
    pivot = input[start]
    left = start + 1
    right = end
    done = False
    while not done:
        while left <= right and input[left] <= pivot:
            left = left + 1
        while input[right] >= pivot and right >= left:
            right = right - 1
        if right < left:
            done = True
        else:
            temp = input[left]
            input[left] = input[right]
            input[right] = temp
    temp = input[start]
    input[start] = input[right]
    input[right] = temp
    return right

# Example usage
input = [29, 10, 14, 37, 13]
print("Original array:", input)
input = quick_sort(input)
print("Sorted array:", input)
