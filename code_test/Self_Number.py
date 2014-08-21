'''
Created on 2014. 8. 14.

@author: csc1725
'''
#===========================================
# 알고리즘 연습했구나 ㅋㅋㅋ
#null인 넘버 빼도 되고 아님.. set에 넣고 for문 돌려도 되고
#===========================================

#초기화 방법 옹!!
list = [0] * 5000

#for문 사용 방법  
for i in range(1,5000):#5000까지 안해도 될거 같다 하지만 계속
    val = 0
    
    #index는 0부터 
    for j in range(0,len(str(i))):
        #print(str(i)+ "=" + str(j))
        val += int(str(i)[j])  
    
    #마지막에 하나더 더 해줘야 하니까
    
    try: 
        list[val+i] = 1 # set에다가 넣을까??? 퍼포먼스를 생각하지는 말자.
        # 결론은 1이 아닌 것을 뽑아내면 되는 거겠네  
        print(str(i) +"===="+ str(val+i))
    except:
        print("endendendend")
    
    

"""
for i in range( len(list) ):
    if list[i] != 1 :
        print(i)
        
"""
#얘는 어케 알지??? for문이 끝났다는 것을 