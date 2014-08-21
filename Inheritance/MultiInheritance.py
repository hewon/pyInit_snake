'''
Created on 2014. 8. 21.

@author: csc1725
'''
#다이아몬드 상속 


class A:
    def __init__(self):
        print("AAAAAAAAA")
        super().__init__()



class B(A):
    def __init__(self):
        print("BBBBBBBB")
        super().__init__()



class C(A):
    def __init__(self):
        print("CCCCCCC")
        super().__init__()



class D(B,C):
    def __init__(self):
        print("DDDDDDD")
        super().__init__()
        
        
Object = D()
print( D.__mro__ )
 
