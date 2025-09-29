"""
CS1350 – Week 2 Homework: NumPy Array Operations
Author: Naina Kalra:)
This homework covers creating and manipulating arrays with NumPy,
broadcasting, slicing, statistics, and comparing Python lists vs NumPy arrays.
"""

import numpy as np
import time

# Always set the random seed so results are reproducible
np.random.seed(1350)


# -------------------------------
# Problem 1: Array Creation and Basic Operations
# -------------------------------

def problem1():
    """
    Create different types of arrays and do some basic operations.
    """
    # a) 1D array from 10 to 50 with step 5
    arr1 = np.arange(10, 51, 5)

    # b) 2D array (3x4) filled with zeros
    arr2 = np.zeros((3, 4))

    # c) 3x3 identity matrix
    identity = np.eye(3)

    # d) 10 evenly spaced numbers between 0 and 5
    linspace_arr = np.linspace(0, 5, 10)

    # e) random array (2x5) values between 0 and 1
    random_arr = np.random.rand(2, 5)

    return arr1, arr2, identity, linspace_arr, random_arr


# -------------------------------
# Problem 2: Array Mathematics and Broadcasting
# -------------------------------

def problem2():
    """
    Show how broadcasting works with NumPy arrays.
    """
    arr_a = np.array([[1, 2, 3],
                      [4, 5, 6],
                      [7, 8, 9]])
    arr_b = np.array([10, 20, 30])

    # a) Add arr_b to each row of arr_a
    result_add = arr_a + arr_b

    # b) Multiply each column of arr_a by arr_b
    result_multiply = arr_a * arr_b

    # c) Square of all elements
    result_square = arr_a ** 2

    # d) Mean of each column
    column_means = np.mean(arr_a, axis=0)

    # e) Subtract column means (centering)
    centered_arr = arr_a - column_means

    return result_add, result_multiply, result_square, column_means, centered_arr


# -------------------------------
# Problem 3: Array Indexing and Slicing
# -------------------------------

def problem3():
    """
    Practice indexing and slicing arrays.
    """
    arr = np.arange(1, 26).reshape(5, 5)

    # a) Third row (index 2 since Python starts at 0)
    third_row = arr[2, :]

    # b) Last column
    last_column = arr[:, -1]

    # c) 2x2 subarray from the center
    center_subarray = arr[1:3, 1:3]

    # d) All elements greater than 15
    greater_than_15 = arr[arr > 15]

    # e) Replace even numbers with -1
    arr_copy = arr.copy()
    arr_copy[arr_copy % 2 == 0] = -1

    return third_row, last_column, center_subarray, greater_than_15, arr_copy


# -------------------------------
# Problem 4: Statistical Analysis
# -------------------------------

def problem4():
    """
    Do statistics with student scores using NumPy.
    """
    scores = np.array([[85, 90, 78, 92],
                       [79, 85, 88, 91],
                       [92, 88, 95, 89],
                       [75, 72, 80, 78],
                       [88, 91, 87, 94]])

    # a) average for each student (row-wise mean)
    student_averages = np.mean(scores, axis=1)

    # b) average for each test (column-wise mean)
    test_averages = np.mean(scores, axis=0)

    # c) highest score per student
    student_max_scores = np.max(scores, axis=1)

    # d) standard deviation for each test
    test_std = np.std(scores, axis=0)

    # e) students with average > 85 (boolean mask)
    high_performers = student_averages > 85

    return student_averages, test_averages, student_max_scores, test_std, high_performers


# -------------------------------
# Problem 5: Performance Comparison
# -------------------------------

def problem5():
    """
    Compare performance between Python lists and NumPy arrays.
    """
    size = 100000
    python_list = list(range(size))
    numpy_array = np.arange(size)

    # Python list squaring with list comprehension
    start_time = time.time()
    list_result = [x ** 2 for x in python_list]
    list_time = time.time() - start_time

    # NumPy array squaring (vectorized)
    start_time = time.time()
    array_result = numpy_array ** 2
    numpy_time = time.time() - start_time

    speedup = list_time / numpy_time

    return {
        'list_time': list_time,
        'numpy_time': numpy_time,
        'speedup': speedup,
        'conclusion': f"NumPy is {speedup:.1f}x faster than Python lists for this operation"
    }


# -------------------------------
# Bonus Challenge (Optional)
# -------------------------------

def bonus_challenge():
    """
    Simple image processing with NumPy.
    """
    image = np.random.randint(0, 256, size=(10, 10))

    # a) Normalize (0-1 range)
    normalized = image / 255.0

    # b) Brightness adjustment (+50, max 255)
    brightened = np.clip(image + 50, 0, 255)

    # c) Negative (invert values)
    negative = 255 - image

    # d) Threshold at 128
    thresholded = np.where(image > 128, 255, 0)

    return normalized, brightened, negative, thresholded


# -------------------------------
# Run tests
# -------------------------------

if __name__ == "__main__":
    print("Problem 1 Results:")
    print(problem1())

    print("\nProblem 2 Results:")
    print(problem2())

    print("\nProblem 3 Results:")
    print(problem3())

    print("\nProblem 4 Results:")
    print(problem4())

    print("\nProblem 5 Results:")
    print(problem5())

    # And this is to try the bonus:
    # print("\nBonus Challenge Results:")
    # print(bonus_challenge())
