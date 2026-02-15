-- Use the database
USE atliq_hardware;

-- Set local_infile to ON
SET GLOBAL local_infile = 1;

-- Import Products
LOAD DATA LOCAL INFILE '/Users/asthapankaj/Desktop/atliq_project/dim_product.csv'
INTO TABLE dim_product
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

-- Import Customers
LOAD DATA LOCAL INFILE '/Users/asthapankaj/Desktop/atliq_project/dim_customer.csv'
INTO TABLE dim_customer
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

-- Import Dates
LOAD DATA LOCAL INFILE '/Users/asthapankaj/Desktop/atliq_project/dim_date.csv'
INTO TABLE dim_date
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

-- Import Sales
LOAD DATA LOCAL INFILE '/Users/asthapankaj-- Use the database
USE atliq_hardware;

-- Set local_infile to ON
SET GLOBAL local_infile = 1;

-- Import Products
LOAD DATA LOCAL INFILE '/Users/asthapankaj/Desktop/atliq_project/dim_product.csv'
INTO TABLE dim_product
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

-- Import Customers
LOAD DATA LOCAL INFILE '/Users/asthapankaj/Desktop/atliq_project/dim_customer.csv'
INTO TABLE dim_customer
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

-- Import Dates
LOAD DATA LOCAL INFILE '/Users/asthapankaj/Desktop/atliq_project/dim_date.csv'
INTO TABLE dim_date
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

-- Import Sales
LOAD DATA LOCAL INFILE '/Users/asthapankaj/Desktop/atliq_project/fact_sales_monthly.csv'
INTO TABLE fact_sales_monthly
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

-- Import Targets
LOAD DATA LOCAL INFILE '/Users/asthapankaj/Desktop/atliq_project/fact_targets.csv'
INTO TABLE fact_targets
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(fiscal_year, month, month_name, department, target_revenue);/Desktop/atliq_project/fact_sales_monthly.csv'
INTO TABLE fact_sales_monthly
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

-- Import Targets
LOAD DATA LOCAL INFILE '/Users/asthapankaj/Desktop/atliq_project/fact_targets.csv'
INTO TABLE fact_targets
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(fiscal_year, month, month_name, department, target_revenue);

