import random

import pymysql
import dum_info
from pymysql.cursors import DictCursor

# Faker 객체 생성
fake = dum_info.user_info

# 데이터베이스 연결 설정
connection = pymysql.connect(
    host='localhost',
    user='root',
    passwd= '1234',
    db='db_test',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor #DictCursor dict 형태로 데이터를 받아옴
)

try:
    with connection.cursor() as cursor:
        # user 10명 입력
        
        for i in range(10):
            print("\n회원정보를 입력해주세요\n")
            first_name = fake.first_name() # 이름
            last_name = fake.last_name() # 성
            email = fake.email() #email 
            password = fake.password() #password
            gender = fake.choice()
            sql = "INSERT INTO users (first_name, last_name, email, password, gender) VALUES (%s, %s, %s, %s, %s)"
            values = (first_name, last_name, email, password, gender)
            cursor.execute(sql,values)
        
        # 재고 변동 이력 10개 만들기 
        for _ in range(10):
            raw_material_id = fake.raw_material_id() 
            pre_quantity = fake.pre_quantity()
            quantity = fake.uantity()
            change_type = fake.change_type()
            store_id = fake.store_id() 
            sql= "INSERT INTO stocks (raw_material_id, pre_quantity, quantity, change_type, store_id) VALUES (%s, %s, %s, %s, %s)"
            values = (raw_material_id, pre_quantity, quantity, change_type, store_id)    
            cursor.execute(sql,values)

        # sales_items 테이블에 데이터 추가하기
            sales_record_id = fake.sales_record_id()
            product_id = fake.product_id()
            quantity = fake.sales_quantity()

            sql= "INSERT INTO sales_items (sales_record_id, product_id, quantity) VALUES (%s, %s, %s)"
            values = (sales_record_id, product_id, quantity)    
            cursor.execute(sql,values)

        # 상품 추가하기
            name = fake.product_name()
            description =  fake.description()
            price = fake.product_price()

            sql= "INSERT INTO products (name, description, price) VALUES (%s, %s, %s)"
            values = (name, description, price)    
            cursor.execute(sql,values)
    

        # 직원 소속 변경하기 

            #기존 등록된 사람 변경 하는 구문 
            sql= "UPDATE employees SET store_id = 5, type = 'STAFF' , is_active ='TRUE' WHERE user_id = (SELECT id FROM users WHERE first_name='user1')" #user1 이름을 가진 사람의 id를 가져옴
            cursor.execute(sql)
            sql= "UPDATE employees SET store_id = 7, type = 'MANEGER' , is_active ='TRUE' WHERE user_id = (SELECT id FROM users WHERE first_name='user2')"
            cursor.execute(sql)


            #신규 채용시 
            sql = "UPDATE users SET is_staff = 'TRUE' WHERE first_name= 'user1')"
            cursor.execute(sql)
            sql = "INSERT INTO employees (code, type, store_id) VALUES( 133, 'STAFF', 5)"
            cursor.execute(sql)

            sql = "UPDATE users SET is_staff = 'TRUE' WHERE first_name= 'user2')"
            cursor.execute(sql)
            sql = "INSERT INTO employees (code, type, store_id) VALUES( 134, 'MANEGER', 7)"
            cursor.execute(sql)


        print("all done")
        # # 변경 사항 커밋
        connection.commit()
finally:
    connection.close()


