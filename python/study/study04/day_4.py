stock = {
    "팥붕어빵" : 10,
    "슈붕어빵" : 8,
    "초코붕어빵" : 5
}

stock["팥붕어빵"] = 15
print(stock["팥붕어빵"])
fish_brade = input("맛을 입력해주세요")
count = int(input("개수를 입력해주세요"))


if fish_brade == "팥붕어빵" :
    stock["팥붕어빵"] += count
    print(f'{fish_brade}맛을 {count}개 채워 현재 재고는 {stock["팥붕어빵"]}개 입니다.')
elif fish_brade == "슈붕어빵" :
    stock["슈붕어빵"] += count
    print(f'{fish_brade}맛을 {count}개 채워 현재 재고는 {stock["슈붕어빵"]}개 입니다.')
elif fish_brade == "초코붕어빵" :
    stock["초코붕어빵"] += count
    print(f'{fish_brade}맛을 {count}개 채워 현재 재고는 {stock["초코붕어빵"]}개 입니다.')
