"""
An n x n matrix is valid if every row and every column contains all the integers from 1 to n (inclusive)
Given an n x n integer matrix, return true if matrix is valid. Otherwise return false
"""

def check_if_valid(input_matrix):
    return False

if __name__ == "__main__":
    input_matrix = [[1,2,3],[2,3,1],[3,1,2]]
    input_matrix2 = [[1,2,3],[2,3,1],[3,2,1]]
    input_matrix3 = [
        [1, 2, 3, 4, 5],
        [2, 3, 4, 5, 1],
        [3, 4, 5, 1, 2],
        [4, 5, 1, 2, 3],
        [5, 1, 2, 3, 4]
    ]
    print(check_if_valid(input_matrix))
    print(check_if_valid(input_matrix2))
    print(check_if_valid(input_matrix3))
