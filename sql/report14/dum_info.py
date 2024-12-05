import random
import string


class user_info :
    
    def first_name(): # 이름
        name = input("이름 입력해주세요")
        # name = ""
        # for _ in range(8):       
        #     name += random.choice(string.ascii_lowercase
        return name
    
    def last_name(): # 성
        name = input("성(씨)를 입력해주세요")
        # name = ""
        # for _ in range(5):       
        #     name += random.choice(string.ascii_lowercase)

        return name
    
    def email(): #email
        email = input("이메일 입력해주세요")
        # email= ""
        # for _ in range(4):       
        #     email += random.choice(string.ascii_lowercase)
        # for _ in range(5):       
        #     email += str(random.randint(0, 10))
            
        return email
    
    def password(): #password
        password = input("암호를 입력해주세요")
        # password= ""
        # for _ in range(2):       
        #     password += random.choice(string.ascii_lowercase)
        # for _ in range(6):       
        #     password += str(random.randint(0, 10))
            
        return password
    def choice() :
        while True :
            gender = input("성을 입력해주세요 남자 : MALE , 여자 : FEMALE ")
            if gender == "MALE":
                break 
            if gender == "FEMALE":
                break 
            print("입력 잘못하셨습니다. MALE, FEMALE 로 대문자로 입력해주세요")
        return gender
    
# ---------------------------------------------------------------------------------

    def raw_material_id():
        material = int(input("원재료 id를 입력해주세요"))
        return material
    
    def pre_quantity():
        material = int(input("이전 재고 수량을 입력해주세요"))
        return material
    
    def quantity():
        quantity = int(input("변동 재고 수량을 입력해주세요"))
        return quantity
    
    def change_type():
        while True :
            type = input("분류를 입력해주세요  입고 : IN  , 출고 : OUT , 반품 : RETURNED , 폐기 : DISCARDED")
            if type == "IN":
                break 
            if type == "OUT":
                break 
            if type == "RETURNED":
                break 
            if type == "DISCARDED":
                break 
            print("입력 잘못하셨습니다. 입고 : IN  , 출고 : OUT , 반품 : RETURNED , 폐기 : DISCARDED 로 대문자로 입력해주세요")
        return type

    def store_id() :
        store_id = int(input("매장 번호를 입력해주세요"))
        return  store_id
    
# ---------------------------------------------------------------------------------

    def sales_record_id():
        sales_record_id = int(input("판매 번호를 입력해주세요"))
        return  sales_record_id
    def product_id():
        product_id = int(input("제품 번호를 입력해주세요"))
        return  product_id
    def sales_quantity():
        sales_quantity = int(input("판매 수량을 입력해주세요"))
        return  sales_quantity
    
# ---------------------------------------------------------------------------------


    def product_name():
        product_nam = input("상품 이름 입력해주세요")
        return product_nam
    def description():
        descriptio = input("상품 설명을 상세하게 입력해주세요")
        return descriptio
    def product_price():
        product_price = float(input("판매가를 입력해주세요 $로 입력할것"))
        return  round(product_price, 2)
