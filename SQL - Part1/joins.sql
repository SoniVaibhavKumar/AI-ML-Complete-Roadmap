CREATE TABLE customers (
customer_id INT PRIMARY KEY,
name VARCHAR(50),
city VARCHAR(50)
);

INSERT INTO customers VALUES
(1, 'Alice', 'Mumbai'), 
(2, 'Bob', 'Delhi'), 
(3, 'Charlie', 'Bangalore'), 
(4, 'David', 'Mumbai');

CREATE TABLE orders (
order_id INT PRIMARY KEY,
customer_id INT,
amount INT
);

INSERT INTO orders VALUES
(101, 1, 500),
(102, 1, 900),
(103, 2, 300),
(104, 5, 700);

SELECT * FROM customers;
SELECT * FROM orders;

-- inner join

SELECT * FROM customers c INNER JOIN orders o ON c.customer_id = o.customer_id;

SELECT c.customer_id, o.order_id, c.name FROM customers c INNER JOIN orders o ON c.customer_id = o.customer_id;

SELECT * FROM customers c LEFT JOIN orders o ON c.customer_id = o.customer_id;

SELECT * FROM customers c RIGHT JOIN orders o ON c.customer_id = o.customer_id;

-- outer join

SELECT * FROM customers c LEFT JOIN orders o ON c.customer_id = o.customer_id
UNION
SELECT * FROM customers c RIGHT JOIN orders o ON c.customer_id = o.customer_id;

-- cross join

SELECT * FROM customers CROSS JOIN orders;

-- self join

SELECT * FROM customers as A JOIN customers as B ON A.customer_id = B.customer_id;

-- sub-queries

SELECT * FROM orders WHERE amount > ( SELECT AVG(amount) FROM orders );

SELECT name, ( SELECT COUNT(*) FROM orders o WHERE o.customer_id = c.customer_id ) as order_count FROM customers c;

DELIMITER $$
CREATE PROCEDURE check_balance(IN acc_id INT)
BEGIN
	SELECT balance
    FROM accounts
    WHERE account_id = acc_id;
END $$

DELIMITER ;

CALL check_balance(1);
CALL check_balance(2);




