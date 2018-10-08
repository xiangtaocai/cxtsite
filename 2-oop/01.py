'''
定义一个类
'''
#定义一个空的类
class Student():
    pass#空类必须有pass

mingyue = Student()


#听python的学生,注意层级
class PythonStudent():
    name = None
    age = 180
    course = 'python'
    #默认出来一个self
    def doHomework(self):
        print("I am doing homewok")


        #推荐在末尾使用return
        return None

yueyue = PythonStudent()
print(yueyue.name)
print(yueyue.age)
# 注意成员函数调用没有传入参数
yueyue.doHomework()
