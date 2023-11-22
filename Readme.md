# Coffee Shop Analysis

## Overview
This project involves the analysis of a coffee shop dataset obtained from Kaggle. The dataset comprises nine separate CSV files, with the main file containing nearly 50,000 rows and 14 columns representing transaction details. Each row corresponds to a line item of a transaction.

## Data Acquisition
The dataset was obtained from Kaggle and consists of nine CSV files. The main file contains transaction details, including transaction date, time, sales outlet, staff, customer, order details, line item details, product details, quantity, line item amount, unit price, and promotional item information.

## Data Preparation
### Original Data (Before Prep)
The original data was loaded using the `wrangle` module's `get_data` function. It consists of columns such as transaction_id, transaction_date, transaction_time, sales_outlet_id, staff_id, customer_id, instore_yn, order, line_item_id, product_id, quantity, line_item_amount, unit_price, and promo_item_yn.

### Cleaned Data
The data was cleaned using the `wrangle` module. Duplicate transaction_id entries were reset, and the data was ordered by date and time. Unnecessary or ambiguous columns such as order, line_item_id, instore_yn, and promo_item_yn were dropped. Data types were adjusted, and a cleaned CSV file ('clean_sales.csv') was created for further analysis.

### Data Dictionary 

| Column             | Data Type | Description                                           |
|--------------------|-----------|-------------------------------------------------------|
| transaction_id     | Integer   | Unique identifier for each transaction.                |
| transaction_date   | Date      | Date of the transaction.                               |
| transaction_time   | Time      | Time of the transaction.                               |
| sales_outlet_id    | Integer   | Identifier for the sales outlet where the transaction occurred. |
| staff_id           | Integer   | Identifier for the staff member involved in the transaction. |
| customer_id        | Integer   | Identifier for the customer involved in the transaction. |
| is_instore         | Binary    | Indicator of whether the transaction occurred in-store (1) or not (0). |
| product_id         | Integer   | Identifier for the product involved in the transaction. |
| quantity           | Integer   | The quantity of the product in the transaction.         |
| line_item_amount   | Float     | The total amount for the line item in the transaction.  |
| unit_price         | Float     | The unit price of the product in the transaction.       |
| is_promo           | Binary    | Indicator of whether the product is a promotional item (1) or not (0). |

This table provides a concise summary of the data types and descriptions for each relevant column in the dataset.

## Train-Test Split
The dataset underwent a division into training and testing sets, with the initial three weeks assigned to the training set and the final week designated for testing purposes.

## Data Exploration
The following key questions were explored:
- What is the best-selling store?
- What are the daily sales for the entire company?
- What are the daily sales by store?
- What is the best-selling product?
- Which product group performs the best in sales?
- Which items are purchased most often?

The exploration revealed insights such as Store 8 having the highest sales revenue in the first three weeks, Store 5 having the lowest sales revenue, and the majority of revenue coming from the beverages product group.

## Modeling
A time series analysis was attempted by splitting off the last week of the data. Due to the limited data, the modeling results were not shown, as the model's performance was expected to be suboptimal.

## Conclusion
### Summary
- Store 8 has the highest sales revenue in the first three weeks.
- Store 5 has the lowest sales revenue in the first three weeks.
- Revenue does not necessarily correlate with the popularity of items.
- The majority of revenue comes from the beverages product group.

### Recommendations
- Collect more data for better analysis.
- Address transaction number system to prevent duplicates.

## Next Steps
- Create a more comprehensive visualization dashboard using Tableau.
- https://public.tableau.com/app/profile/josh.burch/viz/CoffeShop_17005852363230/Dashboard1?publish=yes
