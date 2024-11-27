#함수 만드는 방법
'''
def 함수명() :
    print() or list.append() or 딕셔너리에 값 바꾸기 

def 함수명(매개변수1, 매개변수2, 매개변수3):

'''

hello = "안녕하세요"

def oz_len(hello):
    count = 0
    for i in range(hello):
        count += 1
    return count   

print(oz_len(hello))