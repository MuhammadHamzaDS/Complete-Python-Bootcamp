import math

def jump_search(arr, target):
    n = len(arr)
    
    # Step size = √n
    step = int(math.sqrt(n))
    
    prev = 0
    
    # Finding the block where element may be present
    while prev < n and arr[min(step, n) - 1] < target:
        prev = step
        step += int(math.sqrt(n))
        
        if prev >= n:
            return -1
    
    # Linear search in identified block
    for i in range(prev, min(step, n)):
        if arr[i] == target:
            return i
    
    return -1


# Example usage
arr = [1, 3, 5, 7, 9, 11, 13, 15]
target = 11

result = jump_search(arr, target)

if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found")