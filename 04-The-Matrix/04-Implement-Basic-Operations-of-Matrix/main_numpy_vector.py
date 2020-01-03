import numpy as np

if __name__ == "__main__":
    print(np.__version__)
    # np.array 的基础
    lst = [1,2,3]
    # 原生的list,元素可以是不同类型的数据
    lst[0] = "Linear Algebra"
    print(lst)

    vec = np.array([1,2,3])
    print(vec)
    # np.array的元素不能是不同类型的
    # vec[0] = "Linear Algebra"
    # vec[0] = 666
    # print(vec)

    # np.array 的创建
    print(np.zeros(5))
    print(np.ones(5))
    print(np.full(5,666)) #填充同一个数值

    # np.array的基本属性
    print(vec)
    print("size = ",vec.size)
    print("size = ",len(vec))
    print(vec[0])
    print(vec[-1]) # 取出最后一值
    print(vec[0:2])
    print(type(vec[0:2]))

    #np.array的基本运算
    vec2 = np.array([4,5,6])
    print("{} + {} = {}".format(vec,vec2,vec + vec2) )
    print("{} - {} = {}".format(vec,vec2,vec - vec2) )
    print("{} * {} = {}".format(2,vec,2 * vec) )
    print("{} * {} = {}".format(vec,vec2,vec * vec2) )
    print("{}.dot({}) = {}".format(vec,vec2,vec.dot(vec2)))

    #
    print(np.linalg.norm(vec)) # 求模
    print(vec / np.linalg.norm(vec)) # 求标准化向量
    print(np.linalg.norm(vec / np.linalg.norm(vec))) # 求标准化向量的模

    # 除0异常
    zero3 = np.zeros(3)
    try:
        print(zero3 / np.linalg.norm(zero3))
    except ZeroDivisionError:
        print("ZeroDivisionError")