-- CREATE

(1) **`customers`** 테이블에 새 고객을 추가하세요.
INSERT INTO customers (name, address, customerID, ...) VALUES ('joo', '1234 madong', 1,...);

(2) **`products`** 테이블에 새 제품을 추가하세요.
INSERT INTO products (name, price, productID, ...) VALUES ('Teasue', 1000, 1, ...);

(3) **`employees`** 테이블에 새 직원을 추가하세요.
INSERT INTO employees (employee_Name, position , ...) VALUES ('Moo', 'PM', ...);

(4) **`offices`** 테이블에 새 사무실을 추가하세요.
INSERT INTO offices (office_name, phone_number, ...) VALUES ('OZcording', '123-456-7890', ...);

(5) **`orders`** 테이블에 새 주문을 추가하세요.
INSERT INTO orders (order_num , order_name, oder_EA, ...) VALUES (01, '콤비네이션피자', 1 ,...);

(6) **`orderdetails`** 테이블에 주문 상세 정보를 추가하세요.
INSERT INTO orderdetails (option1, option2, detail, delivery ,...) VALUES ('피클추가', '핫소스추가','올리브제외', True, ...);

(7) **`payments`** 테이블에 지불 정보를 추가하세요.
INSERT INTO payments (customerID, amount, paymentDate, ...) VALUES ('맛있다', 26700, '2024-12-04', ...);

(8) **`productlines`** 테이블에 제품 라인을 추가하세요.
INSERT INTO productlines (productLine, explain, ...) VALUES ('콤비네이션피자', '각종 재료가 들어간 맛있는 피자', ...);

(9) **`customers`** 테이블에 다른 지역의 고객을 추가하세요.
INSERT INTO customers (name, address, ...) VALUES ('Hyeong', '남서로 4길 55', ...);

(10) **`products`** 테이블에 다른 카테고리의 제품을 추가하세요.
INSERT INTO products (name, price, productLine, ...) VALUES ('Teasue', 1000, 'toilet paper', ...);

--READ
**`customers`** 테이블에서 모든 고객 정보를 조회하세요.
SELECT * FROM customers;

(2) **`products`** 테이블에서 모든 제품 목록을 조회하세요.
SELECT name, price FROM products;

(3) **`employees`** 테이블에서 모든 직원의 이름과 직급을 조회하세요.
SELECT firstName, position FROM employees;

(4) **`offices`** 테이블에서 모든 사무실의 위치를 조회하세요.
SELECT office_name, phone_number FROM offices;

(5) **`orders`** 테이블에서 최근 10개의 주문을 조회하세요.
SELECT * FROM orders ORDER BY order_num LIMIT 10;

(6) **`orderdetails`** 테이블에서 특정 주문의 모든 상세 정보를 조회하세요.
SELECT * FROM orderdetails WhERE oder_num = 1 ;

(7) **`payments`** 테이블에서 특정 고객의 모든 지불 정보를 조회하세요.
SELECT * FROM payments WHERE customerID = 1 ;

(8) **`productlines`** 테이블에서 각 제품 라인의 설명을 조회하세요.
SELECT productLine, explain FROM productlines;

(9) **`customers`** 테이블에서 특정 지역의 고객을 조회하세요.
SELECT * FROM customers WHERE address = '1234 madong';

(10) **`products`** 테이블에서 특정 가격 범위의 제품을 조회하세요.
SELECT * FROM products WHERE price BETWEEN 900 AND 5000; 

--UPDATE
**`customers`** 테이블에서 특정 고객의 주소를 갱신하세요.
UPDATE customers SET address = '1234 majangdong' WHERE customerID = 1;

(2) **`products`** 테이블에서 특정 제품의 가격을 갱신하세요.
UPDATE products SET price = 2000 WHERE productID = 1;

(3) **`employees`** 테이블에서 특정 직원의 직급을 갱신하세요.
UPDATE employees SET position = 'PO' WHERE employeeID = 1;

(4) **`offices`** 테이블에서 특정 사무실의 전화번호를 갱신하세요.
UPDATE offices SET phone = '010-000-0001' WHERE officeID = 1;

(5) **`orders`** 테이블에서 특정 주문의 상태를 갱신하세요.
UPDATE orders SET status = '페퍼로니피자' WHERE orderID = 1;

(6) **`orderdetails`** 테이블에서 특정 주문 상세의 수량을 갱신하세요.
UPDATE orderdetails SET option1 = 3 WHERE orderID = 1;

(7) **`payments`** 테이블에서 특정 지불의 금액을 갱신하세요.
UPDATE payments SET amount = 3000 WHERE customerID = 1 AND paymentDate = '2024-12-04';

(8) **`productlines`** 테이블에서 특정 제품 라인의 설명을 갱신하세요.
UPDATE productlines SET explain ='휴지' WHERE productIDID = 1 

(9) **`customers`** 테이블에서 특정 고객의 이메일을 갱신하세요.
UPDATE customers SET  WHERE custmer_email = 'aaaa@gmail.com' WHERE customerID = 1 

(10) **`products`** 테이블에서 여러 제품의 가격을 한 번에 갱신하세요.
UPDATE products SET price = price * 1.1;

--DELETE
(1) **`customers`** 테이블에서 특정 고객을 삭제하세요.
DELETE FROM customers WHERE customerID = 1;

(2) **`products`** 테이블에서 특정 제품을 삭제하세요.
DELETE FROM products WHERE productID = 1;

(3) **`employees`** 테이블에서 특정 직원을 삭제하세요.
DELETE FROM employees WHERE employeesID = 1;

(4) **`offices`** 테이블에서 특정 사무실을 삭제하세요.
DELETE FROM offices WHERE officeID = 1;

(5) **`orders`** 테이블에서 특정 주문을 삭제하세요.
DELETE FROM orders WHERE orderID = 1;

(6) **`orderdetails`** 테이블에서 특정 주문 상세를 삭제하세요.
DELETE FROM orderdetails WHERE orderID = 1;

(7) **`payments`** 테이블에서 특정 지불 내역을 삭제하세요.
DELETE FROM payments WHERE customerID = 1;

(8) **`productlines`** 테이블에서 특정 제품 라인을 삭제하세요.
DELETE FROM productlines WHERE productLine = '콤비네이션피자';

(9) **`customers`** 테이블에서 특정 지역의 모든 고객을 삭제하세요.
DELETE FROM customers WHERE city = '1234 madong';

(10) **`products`** 테이블에서 특정 카테고리의 모든 제품을 삭제하세요.
DELETE FROM products WHERE productLine = '콤비네이션피자';