#introducing method for 3 items:
class Classname:
    def InstanceMethod(self):
        print("hello sourav in the world of instancemethod")

    @classmethod
    def ClassMethod(cls):
        print("This is class method")

    @staticmethod
    def staticmethod():
        print("this is sataticmethod")

v1 = Classname()
v1.InstanceMethod()
Classname.staticmethod()
Classname.ClassMethod()


