# Data Collation

Extract a basic user information table from the order purchase record table.

![](/images/Xnip2024-09-13_20-03-14.jpg)

> 💡 By using AI to understand which fields belong to user records, automatically infer the columns that need to be retained, and deduplicate based on member codes, the goal can be achieved.

## Sample Data
| Transaction Time     | Member Name | Member Gender | Member Status | Member Code      | Info Completeness | Birth Date | Returnable Quantity | Product Name    | Product Code | Payment Amount | Last Purchase Time | Last Purchase Amount | Source Channel                   | Standard Price | Activity Level | Total Purchase Times | Total Purchase Amount | Order Code | Return Quantity | Net Sales Amount | Sales Quantity |
| -------------------- | ----------- | ------------- | ------------- | ---------------- | ----------------- | ---------- | ------------------- | --------------- | ------------ | --------------- | ------------------ | -------------------- | -------------------------------- | -------------- | -------------- | -------------------- | --------------------- | ---------- | --------------- | ----------------- | -------------- |
| 2024-08-20 18:15:03  | Hang Yuanyuan | Unknown     | [50]Regular Member | PP240321689842 | 0               |            | 2                   | Vitamin AD Drops | 12051054    | 91.60          | 2024-08-20         | 91.6                 | Shanghai Gaoji Yutian Pharmacy Co., Ltd | 45.80         | Active A       | 3                    | 3,352                | 22859008   | 0               | 91.60            | 2              |
| 2024-08-20 18:00:26  | Ning Meiru   | Male         | [50]Regular Member | PP181127268580 | 0               |            | 1                   | Bromocriptine Mesylate Tablets | 22041774 | 90.50      | 2024-08-20         | 90.5                 | Gaoji Headquarters              | 90.50         | Active A       | 6                    | 3,730.9              | 22858992   | 0               | 90.50            | 1              |
| 2024-08-20 15:09:14  | Peng Yuxun   | Female       | [50]Regular Member | PP181127269347 | 0               |            | 1                   | Naphazoline Eye Drops | 13186276 | 13.97          | 2024-08-20         | 30.2                 | Yide Taihe Pharmacy              | 13.97         | Active A       | 230                  | 15,987.1             | 22858897   | 0               | 13.97            | 1              |
| 2024-08-20 15:09:14  | Peng Yuxun   | Female       | [50]Regular Member | PP181127269347 | 0               |            | 1                   | Compound Dexamethasone Acetate Cream | 13187858 | 16.23 | 2024-08-20 | 30.2   | Yide Taihe Pharmacy              | 16.23         | Active A       | 230                  | 15,987.1             | 22858897   | 0               | 16.23            | 1              |



## Prompt


```
This is a user order data. Please identify which fields are related to basic user information based on the header, help me organize them, and finally generate a user table. Note to deduplicate based on the member code.
```


## AI Response
First, based on the user's basic information, we can identify the following user-related fields:

- Member Name
- Member Gender
- Member Status
- Member Code
- Birth Date
- Info Completeness

Next, we'll generate a user table using these fields and deduplicate based on the member code. Here are the processing steps:

1. Extract fields related to basic user information from the original data.
2. Deduplicate based on member code, keeping unique user records.

Here's the pandas code to implement these steps:


```python
import pandas as pd
user_columns = ['Member Name', 'Member Gender', 'Member Status', 'Member Code', 'Birth Date', 'Info Completeness']
df_users = data["CRM Data"][user_columns].drop_duplicates(subset='Member Code')
df_output = df_users.reset_index(drop=True)
```


## Result
| Member Name | Member Gender | Member Status | Member Code      | Birth Date | Info Completeness |
| ----------- | ------------- | ------------- | ---------------- | ---------- | ----------------- |
| Hang Yuanyuan | Unknown     | [50]Regular Member | PP240321689842 |            | 0                 |
| Ning Meiru   | Male         | [50]Regular Member | PP181127268580 |            | 0                 |
| Peng Yuxun   | Female       | [50]Regular Member | PP181127269347 |            | 0                 |
| Su Fengkuan  | Female       | [50]Regular Member | PP181127269016 |            | 0                 |
| He Rongning  | Male         | [50]Regular Member | PP181127265499 |            | 0                 |
