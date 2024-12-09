import pymysql
from pymysql.cursors import DictCursor

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
        # 사용자 데이터 삽입
        first_name = "8ki"  # 이름
        last_name = "joa" # 성
        email = "OZ_08@gmail.com"
        password = "a1234" #password
        gender = "MALE"
        sql = "INSERT INTO users (first_name, last_name, email, password, gender) VALUES (%s, %s, %s, %s, %s)"
        values = (first_name, last_name, email, password, gender)
        cursor.execute(sql,values)
        
        
        # "새로운 사용자 8kj joa"의 주소를 변경해주세요 
        
        sql= "UPDATE users SET address = 'py ro 11-05' WHERE first_name= '8ki'"
        cursor.execute(sql,values)
        
        # 1번 store 에서 사용자 "8kj joa"의 주문을 생성해주세요

        # 상품 추가
        name = "팥 붕어빵"
        description = "팥이 들어가 맛있는 붕어빵"
        price = "1"
        sql= "INSERT INTO products (name, description, price) VALUES (%s, %s, %s)"
        values = (name, description, price)    
        cursor.execute(sql,values)

        name = "크림 붕어빵"
        description = "크림이 들어가 맛있는 붕어빵"
        price = "1.5"
        sql= "INSERT INTO products (name, description, price) VALUES (%s, %s, %s)"
        values = (name, description, price)    
        cursor.execute(sql,values)

        name = "피자 붕어빵"
        description = "피자 맛이나 맛있는 붕어빵"
        price = "2"
        sql= "INSERT INTO products (name, description, price) VALUES (%s, %s, %s)"
        values = (name, description, price)    
        cursor.execute(sql,values)

        # sales_records 추가
        store_id = 1 
        sql= "SELECT users FROM id WHERE first_name='8ki'"
        cursor.execute(sql)
        user_cursor = cursor.fetchone()
        user_id  = user_cursor["id"] # 특정유저의 id 가져오기
        sql= "INSERT INTO sales_records(user_id, store_id) VALUES(%s,%s)"
        values = (user_id,store_id)
        cursor.execute(sql,values)

        # salse_item 추가 
        sales_record_id = cursor.lastrowid
        sql= "SELECT products FROM id WHERE name = '팥 붕어빵'"
        cursor.execute(sql)
        product_cursor = cursor.fetchone()
        product_id  = product_cursor["id"]
        quantity = 3
        sql = "INSERT INTO sales_items (sales_record_id, product_id, quantity)VALUES (%s, %s, %s)"
        values = (sales_record_id, product_id, quantity)
        cursor.execute(sql,values)

        # sales_records 추가
        store_id = 1 
        sql= "INSERT INTO sales_records(user_id, store_id) VALUES(%s,%s)"
        values = (user_id,store_id)
        cursor.execute(sql,values)

        # salse_item 추가 
        sql= "SELECT products FROM id WHERE name = '크림 붕어빵'"
        cursor.execute(sql)
        product_cursor = cursor.fetchone()
        product_id  = product_cursor["id"]
        quantity = 2
        sql = "INSERT INTO sales_items (sales_record_id, product_id, quantity)VALUES (%s, %s, %s)"
        values = (sales_record_id, product_id, quantity)
        cursor.execute(sql,values)

        # sales_records 추가
        store_id = 1 
        sql= "INSERT INTO sales_records(user_id, store_id) VALUES(%s,%s)"
        values = (user_id,store_id)
        cursor.execute(sql,values)

        # salse_item 추가 
        sql= "SELECT products FROM id WHERE name = '피자 붕어빵'"
        cursor.execute(sql)
        product_cursor = cursor.fetchone()
        product_id  = product_cursor["id"]
        quantity = 5
        sql = "INSERT INTO sales_items (sales_record_id, product_id, quantity)VALUES (%s, %s, %s)"
        values = (sales_record_id, product_id, quantity)
        cursor.execute(sql,values)
    

        # order_records 테이블에 발주이력을 3건 생성해주세요. (재료는 자유롭게 정해주세요)
        # 원재료 추가 
        name = "반죽"
        price = 3
        sql= "INSERT INTO raw_materials (name, price) VALUES (%s, %s)"
        values = (name , price)    
        cursor.execute(sql,values)

        name = "앙금"
        price = 5
        sql= "INSERT INTO raw_materials (name, price) VALUES (%s, %s)"
        values = (name , price)    
        cursor.execute(sql,values)

        name = "크림"
        price = 7
        sql= "INSERT INTO raw_materials (name, price) VALUES (%s, %s)"
        values = (name , price)    
        cursor.execute(sql,values)

        # order_records 추가 
        sql= "SELECT aw_material FROM id WHERE name = '반죽'"
        cursor.execute(sql)
        material_cursor = cursor.fetchone()
        raw_material_id = material_cursor["id"]
        quantity = 5
        sql= "INSERT INTO order_records (employee_id, supplier_id, raw_material_id, quantity) VALUES (employees.id, suppliers.id, %s, %s)"
        values = (raw_material_id , quantity)    
        cursor.execute(sql,values)

        sql= "SELECT aw_material FROM id WHERE name = '앙금'"
        cursor.execute(sql)
        material_cursor = cursor.fetchone()
        raw_material_id = material_cursor["id"]
        quantity = 3
        sql= "INSERT INTO order_records (employee_id, supplier_id, raw_material_id, quantity) VALUES (employees.id, suppliers.id, %s, %s)"
        values = (raw_material_id , quantity)    
        cursor.execute(sql,values)

        sql= "SELECT aw_material FROM id WHERE name = '크림'"
        cursor.execute(sql)
        material_cursor = cursor.fetchone()
        raw_material_id = material_cursor["id"] 
        quantity = 4
        sql= "INSERT INTO order_records (employee_id, supplier_id, raw_material_id, quantity) VALUES (employees.id, suppliers.id, %s, %s)"
        values = (raw_material_id , quantity)    
        cursor.execute(sql,values)

        
        # stocks 테이블에 원재료 사용이력을 3건 추가하고, 최근 사용이력 3건을 조회해주세요.
        sql= "SELECT aw_material FROM id WHERE name = '반죽'"
        cursor.execute(sql)
        material_cursor = cursor.fetchone()
        raw_material_id = material_cursor["id"] 
        quantity = 5
        change_type = 'IN'

        sql= "INSERT INTO order_records (raw_material_id, quantity, change_type,store_id) VALUES (%s, %s, %s, stores.id)"
        values = (raw_material_id , quantity, change_type)    
        cursor.execute(sql,values)

        sql= "SELECT aw_material FROM id WHERE name = '앙금'"
        cursor.execute(sql)
        material_cursor = cursor.fetchone()
        raw_material_id = material_cursor["id"] 
        quantity = 3
        change_type = 'IN'

        sql= """
        INSERT INTO order_records (raw_material_id, quantity, change_type,store_id) 
        VALUES (%s, %s, %s, stores.id)"
        """
        values = (raw_material_id , quantity, change_type)    
        cursor.execute(sql,values)

        sql= "SELECT aw_material FROM id WHERE name = '크림'"
        cursor.execute(sql)
        material_cursor = cursor.fetchone()
        raw_material_id = material_cursor["id"] 
        quantity = 4
        change_type = 'IN'

        sql= """
        INSERT INTO order_records (raw_material_id, quantity, change_type,store_id) 
        VALUES (%s, %s, %s, stores.id)"
        """
        values = (raw_material_id , quantity, change_type)    
        cursor.execute(sql,values)

        sql = "SELECT * FROM stocks ORDER BY last_used_date DESC LIMIT 3"
        cursor.execute(sql)
        stocks_record = cursor.fetchall()
        print(stocks_record)

        #유저 “8ki joa”가 주문한 내역을 조회해주세요. (단, 비싼 금액의 상품순으로 나열해주세요)
        # 특정 사용자의 ID 가져오기
        sql = """
            SELECT id 
            FROM users 
            WHERE first_name = '8ki' AND last_name = 'joa'
        """
        cursor.execute(sql)
        user_cursor = cursor.fetchone()
        if not user_cursor:
            raise ValueError("사용자 '8ki joa'를 찾을 수 없습니다.")
        user_id = user_cursor['id']

        # 사용자 주문 내역 조회 (별칭 없이 작성된 SQL)
        sql = """
            SELECT products.name AS product_name,   
                sales_items.quantity AS quantity,   
                products.price AS price,            
                (sales_items.quantity * products.price) AS total_price 
            FROM 
                sales_items
            JOIN 
                products ON sales_items.product_id = products.id
            JOIN 
                sales_records ON sales_items.sales_record_id = sales_records.id
            WHERE 
                sales_records.user_id = %s
            ORDER BY 
                total_price DESC
        """
        values = (user_id)
        cursor.execute(sql, values)
        order_history = cursor.fetchall()

        # 결과 출력
        print("주문 내역:")
        for order in order_history:
            print(f"상품명: {order['product_name']}, 수량: {order['quantity']}, 단가: {order['price']}, 총 금액: {order['total_price']}")

        
        connection.commit()
finally:
    connection.close()


