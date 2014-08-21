import urllib

from test import *

def set_password2(password):

    if str( type(password))[8:11] == 'int':
        print(id(password) ) 
    else :
        print(password +"          " + str( id(password) )) 
    # id(password)           ㄱ. 이게 객체의 주소라고?? (Hint: it's the object's memory address.)
    del(password)#           ㄴ. 지웠는데 또 똑같은 주소에 할당된다고 ? 그냥 해시값 아냐?... 다양한 해시의 개념. 
                               # 결론: 리터럴 객체는 존재하고.. 변수는 해당 리터럴 객체를 가리키는 주소를 갖는다.  
pasFunc=set_password2


pasFunc("하하하하하") 
pasFunc("하하하하")
pasFunc("하하하")
pasFunc("하하")
pasFunc("하")
pasFunc(512)
pasFunc(555)
pasFunc(515)

"""
하하하하하
25848192
하하하하
25936912
하하하
26176448
하하
26231776
하
26236272
"""

pasFunc("하하하하하")
pasFunc("하하하하하")
pasFunc("하하하하하")
pasFunc("하하하하하")
pasFunc("하하하하하")
pasFunc(515)
pasFunc(515)
pasFunc(515)
pasFunc(515)




def getSumNProduct(x, y):
           return x + y, x * y

# 함수 호출
sum, product = getSumNProduct(10, 10)

print(sum)
print(product)

tempList = getSumNProduct(10, 10)
print(tempList[0])
print(tempList[1])
