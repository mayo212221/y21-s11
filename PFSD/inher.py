class parent:
    def fn1(self):
        print("this is parent calss")
class child(parent):
    def fn2(self):
        print("this is child class")
ob=child()
ob.fn1()
ob.fn2()
