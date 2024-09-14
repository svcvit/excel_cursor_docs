# Pivot Table

Automatically generate monthly spending for each person based on user order records.

![](/images/Xnip2024-09-13_20-22-10.jpg)

> 💡 Calculate the consumption amount for each person every month, with one row of data per user. The columns should retain the member number and name, followed by columns showing the amount for each month.

## Sample Data
| Transaction Time     | Member Name | Member Gender | Member Status | Member Code      | Info Completeness | Birth Date | Returnable Quantity | Product Name    | Product Code | Payment Amount | Last Purchase Time | Last Purchase Amount | Source Channel                   | Standard Price | Activity Level | Total Purchase Times | Total Purchase Amount | Order Code | Return Quantity | Net Sales Amount | Sales Quantity |
| -------------------- | ----------- | ------------- | ------------- | ---------------- | ----------------- | ---------- | ------------------- | --------------- | ------------ | --------------- | ------------------ | -------------------- | -------------------------------- | -------------- | -------------- | -------------------- | --------------------- | ---------- | --------------- | ----------------- | -------------- |
| 2024-08-20 18:15:03  | Hang Yuanyuan | Unknown     | [50]Regular Member | PP240321689842 | 0               |            | 2                   | Vitamin AD Drops | 12051054    | 91.60          | 2024-08-20         | 91.6                 | Shanghai Gaoji Yutian Pharmacy Co., Ltd | 45.80         | Active A       | 3                    | 3,352                | 22859008   | 0               | 91.60            | 2              |
| 2024-08-20 18:00:26  | Ning Meiru   | Male         | [50]Regular Member | PP181127268580 | 0               |            | 1                   | Bromocriptine Mesylate Tablets | 22041774 | 90.50      | 2024-08-20         | 90.5                 | Gaoji Headquarters              | 90.50         | Active A       | 6                    | 3,730.9              | 22858992   | 0               | 90.50            | 1              |
| 2024-08-20 15:09:14  | Peng Yuxun   | Female       | [50]Regular Member | PP181127269347 | 0               |            | 1                   | Naphazoline Eye Drops | 13186276 | 13.97          | 2024-08-20         | 30.2                 | Yide Taihe Pharmacy              | 13.97         | Active A       | 230                  | 15,987.1             | 22858897   | 0               | 13.97            | 1              |
| 2024-08-20 15:09:14  | Peng Yuxun   | Female       | [50]Regular Member | PP181127269347 | 0               |            | 1                   | Compound Dexamethasone Acetate Cream | 13187858 | 16.23 | 2024-08-20 | 30.2   | Yide Taihe Pharmacy              | 16.23         | Active A       | 230                  | 15,987.1             | 22858897   | 0               | 16.23            | 1              |



## Prompt


```
Calculate the consumption amount for each person every month, with one row of data per user. The columns should retain the member number and name, followed by columns showing the amount for each month.
```

## AI Response
First, based on the requirements, we need to complete the following steps:

1. Convert the `Transaction Time` column to date format and extract the year and month.
2. Group by `Member Code`, `Member Name`, year, and month, and calculate the sum of `Payment Amount` for each user in each month.
3. Convert the result to wide format so that the consumption amount for each month is displayed in different columns.

Here's the pandas code to implement these steps:


```python
import pandas as pd

# 将 '交易时间' 列转换为日期格式
data["CRM Data"]['交易时间'] = pd.to_datetime(data["CRM Data"]['交易时间'])

# 提取年份和月份
data["CRM Data"]['年月'] = data["CRM Data"]['交易时间'].dt.to_period('M')

# 按照会员编码、会员名称和年月分组，并计算支付金额总和
monthly_spending = data["CRM Data"].groupby(['会员编码', '会员名称', '年月'])['支付金额'].sum().reset_index()

# 将数据转换为宽格式
df_output = monthly_spending.pivot_table(index=['会员编码', '会员名称'], columns='年月', values='支付金额', fill_value=0)

# 重置索引
df_output.reset_index(inplace=True)

# 输出结果
df_output
```


## Result
| Member Code      | Member Name | 2023-08 | 2023-09 | 2023-10 | 2023-11 | 2023-12 | 2024-01 | 2024-02 | 2024-03 | 2024-04 | 2024-05 | 2024-06 | 2024-07 | 2024-08 |
| ---------------- | ----------- | ------- | ------- | ------- | ------- | ------- | ------- | ------- | ------- | ------- | ------- | ------- | ------- | ------- |
| PP181127265147   | Song Bolian | 727.4   | 0       | 0       | 0       | 78.9    | 304.5   | 119.4   | 0       | 0       | 0       | 0       | 0       | 0       |
| PP181127265153   | Tang Waiyi  | 0       | 0       | 0       | 0       | 0       | 0       | 0       | 0       | 0       | 130.2   | 0       | 0       | 0       |
| PP181127265173   | Yin Yan     | 0       | 0       | 333.9   | 589.2   | 2502.3  | 168.9   | 183.7   | 136.1   | 105.1   | 333.8   | 33.6    | 629.9   | 5.9     |
| PP181127265187   | Qi Yueshan  | 0       | 34.2    | 0       | 0       | 0       | 0       | 0       | 0       | 0       | 0       | 0       | 0       | 0       |
| PP181127265340   | Wei Kunzhan | 0       | 0       | 0       | 0       | 3615.3  | 0       | 0       | 0       | 0       | 0       | 0       | 0       | 0       |
