USE atliq_hardware;
SHOW TABLES;
-- Check row counts
SELECT 'Products' as Table_Name, COUNT(*) as Total_Rows FROM dim_product
UNION ALL
SELECT 'Customers', COUNT(*) FROM dim_customer
UNION ALL
SELECT 'Dates', COUNT(*) FROM dim_date
UNION ALL
SELECT 'Sales', COUNT(*) FROM fact_sales_monthly
UNION ALL
SELECT 'Targets', COUNT(*) FROM fact_targets;
