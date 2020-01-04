import  matplotlib.pyplot as plt
from playLA.Matrix import  Matrix
from playLA.Vector import  Vector
import math
if __name__ == "__main__":
    points = [[0, 0], [0, 5], [3, 5], [3, 4], [1, 4],
              [1, 3], [2, 3], [2, 2], [1, 2], [1, 0]]

    #串联
    x = [point[0] for point in points]
    y = [point[1] for point in points]

    plt.figure(figsize=(5,5))
    plt.xlim(-10,10)
    plt.ylim(-10,10)
    plt.plot(x,y)
    #plt.show()

    P = Matrix(points)

    T = Matrix([[2, 0],[0, 1.5]]) # x轴放大2倍,y轴放大1.5倍
    T = Matrix([[1, 0], [0, -1]]) # 垂直镜像
    T = Matrix([[-1, 0], [0, 1]])  # 水平镜像
    T = Matrix([[-1, 0], [0, -1]])  # 垂直翻转镜像
    T = Matrix([[1, 0.5], [0, 1]])  # x轴错切
    T = Matrix([[1, 0], [0.5, 1]])  # y轴错切

    # 顺时旋转 60度角
    theta = math.pi / 3
    T = Matrix([[math.cos(theta),math.sin(theta)],
                [-math.sin(theta),math.cos(theta)]])
    P2 = T.dot(P.T())  # 两个矩阵点乘
    # x,y点相连
    plt.plot([P2.col_vector(i)[0] for i in range(P2.col_num())],
             [P2.col_vector(i)[1] for i in range(P2.col_num())])
    print("请看图片...")
    plt.show()