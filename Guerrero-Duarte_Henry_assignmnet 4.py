"""CS309 Python Assignment Template
This template is to be used with all assignments. Failure to use this template
will result in max grade of half credit. To use this template replace lines beginning
with a "#" with the indicated information. Your code will go in the code section.
Save this file with in the form lastname_firstname_assignmnet#.py before submitting to iLearn
For example if I (Sonny Sevin) was submitting assignmnet 1, the file name wouled be: sevin_sonny_assignment1.py."""

#Henry Guerrero-Duarte sfsu_id 918600766
#assignment_4


####################Code#############################

###Henry Guerrero- Duarte
##Instructions: Please complete the following functions that handle matrix operations

def print_matrix(matrix):
    """input: matrix, output: none. This function will print out a matrix in rows
    and columns"""

    #Read the matrix to find the Rows and Columns
    R= len(matrix)
    C= len(matrix[0])

    # For printing the matrix
    for i in matrix(R):
        for j in range(C):
            print(matrix[i][j], end = " ")
        print()

def matrix_addition(matrix1, matrix2):
    """input: two matrices to add together, output: result. This function will
    add the two input matrices together"""

    #determine if matrices are able to be added together (same size R by C)
    R1= len(matrix1)
    C1= len(matrix1[0])
    R2= len(matrix2)
    C2= len(matrix2[0])

    if ((R1 == R2) and (C1 == C2)):
        print("The matrices can be added together")

    #build empty matrix to hold results
        result = []
        result = [ [ 0 for Rows in range( R1 ) ]
             for Columns in range( C1 ) ]

    #add the matrices
    # iterate through rows
        for i in range(R1):
            # iterate through columns
            for j in range(C1):
                result[i][j] = matrix1[i][j] + matrix2[i][j]

            return result
    else:
        return print("The matrices cannot be added together")


def matrix_multiplication(matrix1, matrix2):
    """input: the two matrices to multiple, output: result. This function will
    multiply two matrices together"""

    #first check to see if they are compatible to be multiplied (equal num of cols)
    R1= len(matrix1)
    C1= len(matrix1[0])
    R2= len(matrix2)
    C2= len(matrix2[0])

    if ((C1 == R2)):
        print("The matrices can be multiplied together")

    #build an empty matrix to hold results
        result = []
        result = [ [ 0 for Rows_in_matrix1 in range( R1 ) ]
             for Columns_in_matrix2 in range( C2 ) ]

    #go through rows of matrix1
        for i in range(R1):
    #go through columns of matrix2
            for j in range(C2):
    #go through rows of matrix2 and calculate and store results
                for k in range(R2):
                    result[i][j] += matrix1[i][k] * matrix2[k][j]
        return result
    else:
        return print("The matrices cannot be multiplied together")

###############End Code################################

#############Scoring
#Program ran:
#Correct Output:
#Documentation:
#Requirements Met:
#Total:
