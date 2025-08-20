"""
An n x n matrix is valid if every row and every column contains all the integers from 1 to n (inclusive)
Given an n x n integer matrix, return true if matrix is valid. Otherwise return false
"""

def check_if_valid(input_matrix):
    n = len(input_matrix)
    for i in range(n):
        if not len(set(input_matrix[i])) == n:
            return False
        temp = []
        for y in range(n):
            temp.append(input_matrix[y][i])
        if not  len((set(temp))) == n:
            return False
    return True

if __name__ == "__main__":
    input_matrix = [[1,2,3],[2,3,1],[3,1,2]]
    input_matrix2 = [
        [1, 2, 3, 4, 5],
        [2, 3, 4, 5, 1],
        [3, 4, 5, 1, 2],
        [4, 5, 1, 2, 3],
        [5, 1, 2, 3, 4]
    ]
    print(check_if_valid(input_matrix))
    print(check_if_valid(input_matrix2))
