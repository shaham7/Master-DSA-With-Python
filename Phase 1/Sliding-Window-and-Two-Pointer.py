def sliding_window_example(arr, k):
    """
    Problem: Find maximum sum of k consecutive elements in array
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    # Step 1: Get first window sum
    window_sum = sum(arr[:k])
    max_sum = window_sum
    
    # Step 2: Slide window and update max
    for i in range(len(arr) - k):
        # Remove first element of previous window
        window_sum = window_sum - arr[i]
        # Add last element of current window
        window_sum = window_sum + arr[i + k]
        # Update max sum if required
        max_sum = max(max_sum, window_sum)
    
    return max_sum

def two_pointer_example(arr, target):
    """
    Problem: Find two numbers that add up to target
    Time Complexity: O(n) with sorted array
    Space Complexity: O(1)
    """
    # Step 1: Sort array (if not already sorted)
    arr.sort()
    
    # Step 2: Use two pointers from start and end
    left = 0
    right = len(arr) - 1
    
    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == target:
            return [arr[left], arr[right]]
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    
    return None

# Example usage:
# Sliding Window
arr1 = [1, 4, 2, 10, 2, 3, 1, 0, 20]
k = 4
max_sum = sliding_window_example(arr1, k)
print(f"Maximum sum of {k} consecutive elements: {max_sum}")

# Two Pointer
arr2 = [2, 7, 11, 15]
target = 9
result = two_pointer_example(arr2, target)
print(f"Two numbers that sum to {target}: {result}")