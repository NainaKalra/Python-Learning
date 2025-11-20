#Write a recursive function to calculate the sum of first n natural numbers.
def sum_natural(n):
    if n == 0:            #base case
        return 0
    return n + sum_natural(n - 1)

# Test cases:

print(sum_natural(5))
print(sum_natural(15))

#Write a recursive function that counts the number of digits in a positive integer.

def count_digits(n):
    if n < 10:          # base case: single digit number
        return 1
    return 1 + count_digits(n//10)
#add 1 everytime we remove digit,until we have 1 digit left

# Test cases:
print(count_digits(1234))
print(count_digits(987654321))
print(count_digits(5))



#to check palindrome-
def is_palindrome(s):
    # preprocess: keep alphanumeric only, lowercase
    s = ''.join(ch.lower() for ch in s if ch.isalnum())

    # base cases
    if len(s) <= 1:
        return True

    # recursive case
    if s[0] != s[-1]:
        return False

    return is_palindrome(s[1:-1])

#Test cases:
print(is_palindrome("racecar")) 
print(is_palindrome("hello")) 
print(is_palindrome("a")) 

# Implement a recursive function to calculate x^n (x to the power n).
def power(x, n):
    if n == 0:      # base case
        return 1
    return x * power(x, n - 1)   # recursion step

# Test cases:
print(power(2, 5))
print(power(3, 0)) 
print(power(5, 3))

#Generate all binary strings of length n

def generate_binary_strings(n):
    result = []

    def helper(current):
        if len(current) == n:    # building full string
            result.append(current)
            return
        helper(current + "0")
        helper(current + "1")

    helper("")
    return result

# Test cases:
print(generate_binary_strings(2))
print(generate_binary_strings(1)) 

#Given a list of integers and a target sum, determine if there exists a subset that adds up to the target-

def subset_sum(nums, target, index=0):
# Base case:
    if target == 0:
        return True
    if index == len(nums):
        return False

    # first choice: include nums[index]
    if subset_sum(nums, target - nums[index], index + 1):
        return True

    # second choice: exclude nums[index]
    return subset_sum(nums, target, index + 1)

# Test cases:
print(subset_sum([3, 34, 4, 12, 5, 2], 9)) 
print(subset_sum([1, 2, 3, 4], 10))
print(subset_sum([1, 2, 3], 7))