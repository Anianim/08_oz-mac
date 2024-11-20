'''
식별자와 변수명

식별자는 프로그래밍 언어에서 변수, 함수, 클래스, 모듈 등의 이름을 지정하는 모든 명칭을 뜻합니다.
변수명은 변수의 이름을 뜻한다. (값을 저장할 메모리 공간을 참조하기 위해 사용 되는이름)
변수는 데이터를 저장하는 컨테이너이고 변수명은 컨테이너를 가르키는 이름이다.

'''

# import keyword
# print(keyword.kwlist)

# * 내장함수 공부하기 *

# 지정 불가 변수명 확인 가능.

# print("{}{} {}".format(8,"기","백엔드"))

# num = 8
# str_a = "기"
# str_b = "백엔드"
# print(f"{num}{str_a} {str_b}")

# 장단점 list 타입의 경우 리스트의 내용을 *을 통해 format 은 자동으로 입력이 가능하지만 
# f string 경우 각각 형태에 맞게 변수를 지정해줘야 한다. {리스트변수[index]]}

# print(type(777))
# print(type(777.7))

#len() 미리 만들어 놓은 기능 = 내장함수

#변수[시작위치:끝나는위치] : 시작위치부터 출력되고 끝나는 위치 -1까지만 출력된다.

# isupper() /islower() 대소문자를 구별해는데 어떻게? 결과는 True or False 로 반환 

# url = "https://search.naver.com/search.naver?ssc=tab.blog.all&sm=tab_jum&query="
# keyword = input("검색하고 싶은 키워드를 입력해줘 :") #입력을 받을 수 있도록 미리 만들어준 기능입니다. 내장함수

# print(url+keyword)

# if 조건문 
# str = "초격차밴드다"
# if len(str) > 5 :
#     print("참이구나")

