import numpy as np


###############################


# the vector

vector = np.array([[1, 2, 3]])
print("original vector: \n", vector)


########################


# transposing the vector

trvector = np.transpose(vector)
print("transposed vector: \n", trvector)


#########################################


# dotting the vectors

print("dot of vectors: \n",
      np.dot(vector, trvector), "\n")


#######################################


# create a matrix

matrix = np.array([[1, 2, 3],
                   [1, 2, 3],
                   [1, 2, 3]])
print("the original matrix: \n", matrix)


#########################################

# transpose the matrix

trmatrix = np.transpose(matrix)
print("the transposed matrix: \n", trmatrix)


#############################################


# dot the matrix with its transpose

print("dot of matrices: \n",
      np.dot(matrix, trmatrix), "\n")


##########################################


# # outer product matrix multiplication
# print("the outer product of the matrix with the transposed matrix: \n", np.outer(matrix, trmatrix), "\n")
#
# # kron product matrix multiplication
# print("the kronecker product of the matrix with the transposed matrix: \n", np.kron(matrix, trmatrix), "\n")
#
# # dot product of 2 matrices
# # a 2-D matrix, or set of sets
# matrix = np.array([[1, 2, 3],
#                    [1, 1, 3],
#                    [-3, 2, 19]])
# print("original matrix: \n", matrix)
# trmatrix = np.transpose(matrix)
# print("transposed matrix: \n", trmatrix, "\n")
# print("dot product of 2 matrices: \n", np.dot(matrix, trmatrix), "\n")
# print("equivalent to (v1 * w1) + (v2 * w2*) + (v3 * w3)")



