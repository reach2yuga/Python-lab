#find missing number in a given array of 1 to n
# where one number is missing
a = [1,2,4,5,6,7,8,9,10]

def find_missing_number(arr):
    n = len(arr) + 1  # Since one number is missing
    total_sum = n * (n + 1) // 2  # Sum of first n natural numbers
    actual_sum = sum(arr)  # Sum of the given array
    return total_sum - actual_sum  # The missing number

result = find_missing_number(a)
print(f"The missing number is: {result}")