# def selection_sort(arr):
#     n = len(arr)
#     for i in range(n):
#         min_index = i  # assume current index is minimum
#         for j in range(i + 1, n):
#             if arr[j] < arr[min_index]:
#                 min_index = j  # update if a smaller element is found
#         arr[i], arr[min_index] = arr[min_index], arr[i]  # swap

# # Example usage
# arr = [64, 25, 12, 22, 11]
# selection_sort(arr)
# print("Sorted array:", arr)

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i  # Assume current element is the minimum
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j  # Found smaller element
        arr[i], arr[min_index] = arr[min_index], arr[i]  # Swap

# ----- Get input from user -----
user_input = input("Enter numbers separated by spaces: ")

# Convert input string to list of integers
arr = list(map(int, user_input.strip().split()))

# Sort the array
selection_sort(arr)

# Display result
print("Sorted array:", arr)
