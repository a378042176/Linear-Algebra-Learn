from playLA.Matrix import Matrix
from playLA.Vector import Vector

if __name__ == "__main__":
    matrix = Matrix([[1, 2], [3, 4]])
    print(matrix)

    print("matrix.shape = {}".format(matrix.shape()))
    print("matrix.size = {}".format(matrix.size()))
    print("matrix.len = {}".format(len(matrix)))
    print("matrix[0][0] = {}".format(matrix[0, 0]))
    print("matrix.row_vector(0) = {}".format(matrix.row_vector(0)))
    print("matrix.col_vector(0) = {}".format(matrix.col_vector(0)))

    matrix2 = Matrix([[5, 6], [7, 8]])
    print("add: {}".format(matrix + matrix2))
    print("sub: {}".format(matrix - matrix2))

    print("{} * 2: {}".format(matrix, matrix * 2))
    print("2 * {} : {}".format(matrix, 2 * matrix))

    print("zero_2_3: {}".format(Matrix.zero(2, 3)))

    T = Matrix([[1.5, 0], [0, 2]])
    p = Vector([5, 3])
    print("T.dot(p) = {}".format(T.dot(p)))

    P = Matrix([[0, 4, 5], [0, 0, 3]])
    print("T.dot(P) = {}".format(T.dot(P)))

    print("A.dot(B) = {}".format(matrix.dot(matrix2)))  # 矩阵乘法不遵守交换率
    print("B.dot(A) = {}".format(matrix2.dot(matrix)))

    print("P.T = {}".format(P.T()))
