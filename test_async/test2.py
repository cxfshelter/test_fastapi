aa = 1

cc = 1

class B():

    def __init__(self):
        global cc
        cc = 2

    def c(self):
        print(aa)


b = B()
b.c()
print(cc)