# 定义一个py类
class Vector:
    def __init__(self,lst):
        """
        lst是一个列表
        下划线 _ 开头的变量, 定义为私有变量
        """
        self._values = lst

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