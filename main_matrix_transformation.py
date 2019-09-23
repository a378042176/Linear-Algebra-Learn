import math

import matplotlib.pyplot as plt

from playLA.Matrix import Matrix

if __name__ == "__main__":
    points = [[0, 0], [0, 5], [3, 5], [3, 4], [1, 4],
              [1, 3], [2, 3], [2, 2], [1, 2], [1, 0]]

    x = [point[0] for point in points]
    y = [point[1] for point in points]

    plt.figure(figsize=(5, 5))
    plt.xlim(-10, 10)
    plt.ylim(-10, 10)

    plt.plot(x, y)
    # plt.show()

    P = Matrix(points)
    # P 10*2
    # T 2*2 变换矩阵，可称为函数
    # T = Matrix([[2, 0], [0, 1.5]]) # 放大
    # T = Matrix([[1, 0], [0, -1]])  # x轴翻转
    # T = Matrix([[-1, 0], [0, 1]])  # y轴翻转
    # T = Matrix([[-1, 0], [0, -1]])  # 完全翻转
    # T = Matrix([[1, 0.5], [0, 1]])  # x轴错切
    # T = Matrix([[1, 0], [0.5, 1]])  # y轴错切
    # theta = math.pi / 3  # 1/3度
    # T = Matrix([[math.cos(theta), math.sin(theta)], [-math.sin(theta), math.cos(theta)]]) # 旋转theta度

    T = Matrix([[0, -1], [1, 0]])


    P2 = T.dot(P.T())  # 因为要用T作为函数乘以P，需满足T的列为2，P的行为2，但P是10*2，T是2*2，所以要将P转置成2*10再相乘
    plt.plot([P2.col_vector(i)[0] for i in range(P2.col_num())],
             [P2.col_vector(i)[1] for i in range(P2.col_num())])

    plt.show()
