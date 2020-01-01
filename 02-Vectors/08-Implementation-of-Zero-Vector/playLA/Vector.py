# 定义一个py类
class Vector:
    def __init__(self,lst):
        """
        lst是一个列表
        下划线 _ 开头的变量, 定义为私有变量
        """
        self._values = lst

    @classmethod
    def zero(cls,dim):
        """返回一个dim维的零向量"""
        return cls([0] * dim)

    def __add__(self, another):
        """
        向量加法,返回结果向量
        :param another:
        :return:
        """
        assert len(self) == len(another),\
        "Error in adding. Length of vectors must be same."
        #return Vector([a+b for a,b in zip(self._values,another._values)])
        return Vector([a + b for a, b in zip(self, another)])

    def __sub__(self, another):
        """向量减法,返回结果向量"""
        assert len(self) == len(another),\
        "Error in subtracting. Length of vectors must be same."

        return Vector([a - b for a, b in zip(self, another)])

    def __mul__(self, k):
        """返回数量乘法的结果向量: self * k"""
        return Vector([k * e for e in self])

    def __rmul__(self, k):
        """返回数量乘法的结果向量: k * self """
        return self * k  # 调用__mul__

    def __pos__(self):
        """返回向量取正的结果向量"""
        return 1 * self # 调用__rmul__

    def __neg__(self):
        """返回向量取负的结果向量"""
        return -1 * self # 调用__rmul__

    def __iter__(self):
        """返回向量的迭代器"""
        return self._values.__iter__()

    def __getitem__(self, index):
        """
        取向量的第index个元素,
        例如: vector[1],vector[2]
        """
        return  self._values[index]

    def __len__(self):
        """返回向量长度(有多少个元素)"""
        return len(self._values)

    def __repr__(self):
        """
        在 Python 交互式命令行下直接输出对象默认使用的是__repr__
        :return:
        """
        return "Vector({})" .format(self._values)

    def __str__(self):
        """
        输出向量的字符串表达形式
        例如: (1, 2, 3)
        :return:
        """
        return "({})".format(", ".join(str(e) for e in self._values))