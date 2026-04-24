CREATE DATABASE sales_db;
USE sales_db;

SELECT * FROM sales_data
limit 3;


### MONTHLY REVENUE
SELECT Month ,SUM(Revenue)
from sales_data
GROUP BY Month
ORDER BY Month;


###Top Products (Quantity)
SELECT Description, SUM(Quantity)
from sales_data
Group BY Description
ORDER BY SUM(Quantity) desc
LIMIT 10;


### Top Customers
SELECT CustomerID, SUM(Revenue)
from sales_data
Group BY CustomerID
ORDER BY SUM(Revenue) desc
LIMIT 10;


### Country-wise Revenue
SELECT Country, SUM(Revenue)
from sales_data
Group BY Country
ORDER BY SUM(Revenue) desc
LIMIT 10;


### Total Revenue
SELECT SUM(Revenue)
from sales_data;
SELECT SUM(Quantity*UnitPrice)
FROM sales_data;


SELECT COUNT(distinct InvoiceNo)
FROM sales_data ;

### Average Order Value
SELECT AVG(temp)
FROM (SELECT InvoiceNO,SUM(Revenue) as temp
from sales_data
group by InvoiceNO) as temp2;


### Repeat vs New Customers
SELECT 
    CustomerID,
    CASE 
        WHEN COUNT(DISTINCT InvoiceNo) > 1 THEN 'Repeat'
        ELSE 'New'
    END AS customer_type
FROM sales_data
GROUP BY CustomerID;

### Top 5 highest spend customer
select CustomerID , sum(Revenue)
from sales_data
group by CustomerID
order by sum(Revenue) desc
limit 5;

