'''
### 프로젝트 : 간단한 ATM 관리 시스템

[문제 1: 잔액 확인]

현재 잔액은 1000원입니다. 현재 잔액을 출력하세요 . 변수명 예시( 잔액 - balance)
'''


balance = 1000
print(f'현재 잔액은 {balance}원 입니다.')
recipts = []
while True : 
    num = input("사용하실 기능을 선택해주세요 (1:입금, 2:출금, 3번:영수증 보기 4번: 종료")
    if num == "1" :
        # 입금 기능    
        deposit_amount = int(input("입금할 금액을 입력해주세요 : "))
        balance += deposit_amount
        recipts.append(("입금",deposit_amount,balance))
        print(f'입금하신 금액은 {deposit_amount}원 입니다. 현재 잔액은 {balance}원 입니다.')
    elif num == "2" :
        # 출금기능
        withdraw_amount = int(input("출금할 금액을 입력해주세요 : "))

        withdraw_amount= min(balance , withdraw_amount) # 출금 가능금액 
        balance -= withdraw_amount
        recipts.append(("출금",withdraw_amount,balance))
        print(f'출금하신 금액은 {withdraw_amount}원 입니다. 현재 잔액은 {balance}원 입니다.')

    elif num == "3" :
        #영수증 내역 출력
        print(recipts)
    
    elif num == "4" :
        print('ATM 서비스를 종료합니다.') 
        break