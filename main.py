
"""
案例：简单的数字加减乘除
目的：对简单的代码进行逐步优化
收获：学会如何优化代码，优化思路。
"""

"""
Python命名规则：
      1.变量名称：一般用小写的英文，如果多个字母，用_隔开
      2.常量：一般用大写的英文名词
      3.方法：一般用小写的英文动词，如果多个，用下划线隔开
      4.类型：一般用英文名词，首字母大写
"""
from abc import ABCMeta, abstractmethod
class Operation(metaclass=ABCMeta):
    str_num1 = ""
    str_num2 = ""
    @abstractmethod
    def get_result(self):
        pass

class OperationAdd(Operation):
    def get_result(self):
        return float(self.str_num1) + float(self.str_num2)

class OperationSub(Operation):
    def get_result(self):
        return float(self.str_num1) - float(self.str_num2)

class OperationMul(Operation):
    def get_result(self):
        return float(self.str_num1) * float(self.str_num2)

class OperationDiv(Operation):
    def get_result(self):
        return float(self.str_num1) / float(self.str_num2)


class Factory:
    def __init__(self,oper):
        self.oper = oper

    def create_obj(self):
        if self.oper == "+":
            return OperationAdd()
        if self.oper == "-":
            return OperationSub()
        if self.oper == "*":
            return OperationMul()
        if self.oper == "/":
            return OperationDiv()


# 以下代码也是对的，不是低耦合高内聚，以上代码是优化代码
# class Operation:
#     def __init__(self,str_num1,str_num2,oper):
#         # 当由一个类变成对象的时候，会自动调用这个方法。
#         # self -> 就是我们创建的对象
#         # 作用：对对象的属性做初始化
#         self.str_num1 = str_num1
#         self.str_num2 = str_num2
#         self.oper = oper
#
#     def get_result(self):
#         if self.oper == "+":
#             return float(self.str_num1) + float(self.str_num2)
#         if self.oper == "-":
#             return float(self.str_num1) - float(self.str_num2)
#         if self.oper == "*":
#             return float(self.str_num1) * float(self.str_num2)
#         if self.oper == "/":
#             return float(self.str_num1) / float(self.str_num2)



if __name__ == "__main__":   # 代码入口

    str_num1 = input("请输入第一个数：")
    oper = input("请输入加减运算符：")
    str_num2 = input("请输入第二个数字：")

    try:  # 异常处理
        Operation.str_num1 = str_num1
        Operation.str_num2 = str_num2
        obj = Factory(oper).create_obj()
        result = obj.get_result()
        print(result)

        # oper1 = Operation(str_num1,str_num2,oper)
        # result = oper1.get_result()
        # print(result)

    except Exception as e:
        print(str(e))





