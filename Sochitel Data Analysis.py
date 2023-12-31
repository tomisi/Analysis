#!/usr/bin/env python
# coding: utf-8

# In[6]:


import IPython
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
from country_converter import CountryConverter
from IPython.display import display


# In[7]:


cc = CountryConverter()


# In[8]:


file_path = r"C:\Users\Hp\Downloads\dataset.xlsx"
df = pd.read_excel(file_path)


# In[9]:


df.head()


# In[119]:


duplicates = df.duplicated()


# In[121]:


duplicated_rows = df[duplicates]
print("Duplicated Rows:")
print(duplicated_rows)


# In[10]:


revenue_by_client = df.groupby('Beneficial User')['Buy Margin (£)'].sum()


# In[11]:


highest_revenue_client = revenue_by_client.idxmax()
highest_revenue_amount = revenue_by_client.max()


# In[12]:


print("Client with the highest revenue:", highest_revenue_client)
print("Revenue generated by the client:", highest_revenue_amount)


# In[13]:


revenue_by_operator = df.groupby('Operator')['Buy Margin (£)'].sum()


# In[14]:


highest_revenue_operator = revenue_by_operator.idxmax()
highest_revenue_amount = revenue_by_operator.max()


# In[15]:


print("Operator with the highest revenue:", highest_revenue_operator)
print("Revenue generated by the operator:", highest_revenue_amount)


# In[16]:


revenue_by_client = df.groupby('Beneficial User')['Buy Margin (£)'].sum()


# In[17]:


top_client = revenue_by_client.idxmax()
top_client_revenue = revenue_by_client.max()


# In[18]:


print("Top client in terms of revenue:", top_client)
print("Revenue generated by the top client:", top_client_revenue)


# In[19]:


total_revenue = df['Buy Margin (£)'].sum()


# In[20]:


percentage_contribution = (top_client_revenue / total_revenue) * 100


# In[21]:


print("Percentage of revenue contributed by the top client: {:.2f}%".format(percentage_contribution))


# In[22]:


revenue_by_client = df.groupby('Beneficial User')['Buy Margin (£)'].sum()


# In[23]:


top_10_clients = revenue_by_client.sort_values(ascending=False).head(10)


# In[24]:


print("Top 10 clients:")
print(top_10_clients)


# In[25]:


if not pd.api.types.is_datetime64_any_dtype(df['Date']):
    df['Date'] = pd.to_datetime(df['Date'])


# In[26]:


revenue_by_date = df.groupby('Date')['Buy Margin (£)'].sum()


# In[27]:


date_with_highest_revenue = revenue_by_date.idxmax()


# In[28]:


total_revenue = df['Buy Margin (£)'].sum()
percentage_contribution = (revenue_by_date[date_with_highest_revenue] / total_revenue) * 100


# In[30]:


print("Date with the highest revenue:", date_with_highest_revenue)
print("Percentage contribution of the day's revenue: {:.2f}%".format(percentage_contribution))


# In[35]:


plt.figure(figsize=(12, 6))
revenue_by_date.plot(kind='bar', color='Orange', edgecolor='black', linewidth=0.7)
plt.axvline(x=date_with_highest_revenue, color='firebrick', linestyle='--', label='Day with Highest Revenue')
plt.title('Daily Revenue Analysis', fontsize=16, fontweight='bold')
plt.xlabel('Date', fontsize=12)
plt.ylabel('Revenue (£)', fontsize=12)
plt.xticks(fontsize=10, rotation=45, ha='right')
plt.yticks(fontsize=10)
plt.legend(fontsize=10)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()


# In[45]:


revenue_by_operator = df.groupby('Operator')['Buy Margin (£)'].sum()


# In[46]:


operator_with_max_revenue = revenue_by_operator.idxmax()


# In[47]:


operator_with_max_revenue = revenue_by_operator.idxmax()


# In[48]:


print("Operator with the highest revenue:", operator_with_max_revenue)


# In[49]:


sorted_revenue = revenue_by_operator.sort_values(ascending=False)


# In[50]:


top_10_operators = sorted_revenue.head(10)


# In[53]:


plt.figure(figsize=(12, 6))
top_10_operators.plot(kind='bar', color='orange', edgecolor='black')
plt.title('Top 10 Operators with Highest Revenue')
plt.xlabel('Operator')
plt.ylabel('Revenue (£)')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()


# In[57]:


df['Continent'] = df['Operator Country'].apply(lambda country: cc.convert(names=country, to='continent'))


# In[63]:


df['Profit'] = df['User Amount (£)'] - df['Calculated Cost (£)']


# In[65]:


revenue_breakdown = df.groupby(['Operator', 'Operator Country', 'Continent', 'Operator Currency'])['Profit'].sum().reset_index()


# In[68]:


revenue_breakdown = revenue_breakdown.sort_values(by='Profit', ascending=False)


# In[69]:


pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)


# In[70]:


#print(revenue_breakdown)
display(revenue_breakdown)


# In[107]:


product_revenue = df.groupby('Product Type')['Buy Margin (£)'].sum().reset_index()


# In[108]:


least_performing_products = product_revenue.sort_values(by='Buy Margin (£)', ascending=True)


# In[109]:


top_10_least_performing_products = least_performing_products.head(10)


# In[110]:


print("Top 10 Least Performing Products:")
print(least_performing_products)


# In[112]:


plt.figure(figsize=(12, 6))
plt.bar(top_10_least_performing_products['Product Type'], top_10_least_performing_products['Buy Margin (£)'], color='Orange')
plt.title('Top 10 Least Performing Products')
plt.xlabel('Product Name')
plt.ylabel('Buy Margin (£)')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()


# In[91]:


operator_supplier_count = df.groupby('Operator')['Suppier Name'].nunique().reset_index()


# In[92]:


print(operator_supplier_count)


# In[93]:


total_revenue_generated = df['Buy Margin (£)'].sum()

print("Total Revenue Generated: £{:.2f}".format(total_revenue_generated))


# In[94]:


client_revenue = df.groupby('Beneficial User')['Buy Margin (£)'].sum().reset_index()


# In[95]:


sorted_client_revenue = client_revenue.sort_values(by='Buy Margin (£)', ascending=False)


# In[96]:


top_7_clients = sorted_client_revenue.head(7)

print(top_7_clients)


# In[102]:


df['Profit'] = df['Buy Margin (£)']


# In[103]:


revenue_breakdown = df.groupby([ 'Continent' ])['Profit'].sum().reset_index()


# In[104]:


revenue_breakdown = revenue_breakdown.sort_values(by='Profit', ascending=False)


# In[105]:


print(revenue_breakdown)


# In[106]:


product_revenue = df.groupby('Product Type')['Buy Margin (£)'].sum().reset_index()


# In[113]:



print(product_revenue)


# In[114]:


average_buy_margin = product_revenue['Buy Margin (£)'].mean()


# In[115]:


most_profitable_products = product_revenue[product_revenue['Buy Margin (£)'] >= average_buy_margin]


# In[116]:


improvement_needed_products = product_revenue[product_revenue['Buy Margin (£)'] < average_buy_margin]


# In[117]:


print("Most Profitable Products:")
print(most_profitable_products)


# In[118]:


print("\nProducts Needing Improvement:")
print(improvement_needed_products)


# In[124]:


revenue_by_currency = df.groupby('Operator Currency')['Buy Margin (£)'].sum().reset_index()
print(revenue_by_currency)


# In[127]:


revenue_by_currency = df.groupby('Operator Currency')['Buy Margin (£)'].sum().reset_index()
top_10_currencies = revenue_by_currency.sort_values('Buy Margin (£)', ascending=False).head(10)


# In[133]:


plt.figure(figsize=(10, 6))
bars = plt.bar(top_10_currencies['Operator Currency'], top_10_currencies['Buy Margin (£)'], color='orange')
plt.xlabel('Operator Currency')
plt.ylabel('Revenue (£)')
plt.title('Top 10 Currencies by Revenue')
plt.xticks(rotation=45, ha='right', fontsize=10)
plt.yticks(fontsize=10)
for bar in bars:
    height = bar.get_height()
    plt.annotate(f'{height:.2f}', xy=(bar.get_x() + bar.get_width() / 2, height),
                 xytext=(0, 3), textcoords="offset points", ha='center', va='bottom', fontsize=9)

plt.tight_layout()
plt.show()


# In[ ]:




