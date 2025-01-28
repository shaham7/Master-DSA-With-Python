def array_operations_demo():
    # 1. Initialize an array
    numbers = [1, 2, 3, 4, 5]
    print(f"Original array: {numbers}")
    
    # 2. Basic operations
    # Insertion at end - O(1)
    numbers.append(6)
    print(f"After append: {numbers}")
    
    # Insertion at specific index - O(n)
    numbers.insert(0, 0)
    print(f"After insert at beginning: {numbers}")
    
    # Deletion - O(n)
    numbers.remove(3)  # removes first occurrence of 3
    print(f"After removing 3: {numbers}")
    
    # 3. Accessing and updating - O(1)
    numbers[1] = 10
    print(f"After updating index 1: {numbers}")
    
    # 4. Slicing - O(k) where k is the slice size
    sub_array = numbers[2:4]
    print(f"Slice from index 2 to 4: {sub_array}")
    
    # 5. Common array patterns
    # Finding sum - O(n)
    total = sum(numbers)
    print(f"Sum of array: {total}")
    
    # Finding maximum - O(n)
    maximum = max(numbers)
    print(f"Maximum value: {maximum}")
    
    return numbers

# Let's run our demo
result = array_operations_demo()