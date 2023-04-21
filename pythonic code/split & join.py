
### Split & join ###

import pprint

lst =["a",  "b", "c"]
lst2= ["d","e","f"]

pprint.pprint([i+j for i in lst for j in lst2 if not(i==j)])
#pprint : print를 예쁘게 출력해주는 기능

loop_lst= [i+j for i in lst for j in lst2 if not(i==j)]
print("1번째 loop: %l ", loop_lst) 
# ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']


loop_lst2 = [i+j if not (i ==j) else i for i in lst for j in lst2]
# if 조건문 else 조건문 for 문
print("2번째 loop: %l ",loop_lst2)



words = " The quick brown fox jumps over the lazy dog".split()
print([[i.upper(), i.lower(),len(i)]for i in words]) 
# [['THE', 'the', 3], ['QUICK', 'quick', 5], ['BROWN', 'brown', 5], ['FOX', 'fox', 3], ['JUMPS', 'jumps', 5], ['OVER', 'over', 4], ['THE', 'the', 3], ['LAZY', 'lazy', 4], ['DOG', 'dog', 3]]

loop_lst3 =[[i+j for i in lst]for j in lst2]
print("3번째 loop : ", loop_lst3) 
# [['ad', 'bd', 'cd'], ['ae', 'be', 'ce'], ['af', 'bf', 'cf']]
# 2D로 실행됨.  for j in lst2부터 돌아감. 


loop_lst4 =[[j+i for i in lst if i != "a"]for j in lst2]
print("4번째 loop : ", loop_lst4) 
# [['db', 'dc'], ['eb', 'ec'], ['fb', 'fc']]
# 2D로 실행됨.  for j in lst2부터 돌아감. 

#reference 
# https://www.boostcourse.org/ai100/lecture/739170?isDesc=false