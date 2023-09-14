#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
 # create a new matrix with the same size
    new_matrix = [[0 for col in row] for row in matrix]
    
    # iterate through the matrix
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            new_matrix[row][col] = matrix[row][col] ** 2
            
    return new_matrix
