# -*- coding: utf-8 -*-
"""Customer Segmentation in Online Retail.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1nmqPZGcVGac_lPyVR2C--AzHhm_2T43X

# Customer Segmentation in Online Retail
---
"""

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import warnings

from google.colab import drive
warnings.filterwarnings('ignore')

"""## 1. Data Preparation"""

drive.mount('/content/drive/')
df=pd.read_excel('/content/drive/MyDrive/datasets/Online_Retail.xlsx')

"""I load the data. Once done, I also give some basic informations on the content of the dataframe: the type of the various variables, the number of null values and their percentage with respect to the total number of entries:"""

df.head()

df.describe().T

df.isna().sum()

### Checking for Missing values
pd.DataFrame(data={'Data Type':df.dtypes.values,'Null Values':df.isna().sum().values,
        '%age of Null Values':[round(df.isna().sum().values[i]*100/len(df),2) for i in range(len(df.columns))]},index=df.columns).T

"""While looking at the number of null values in the dataframe, it is interesting to note that  ∼ 25% of the entries are not assigned to a particular customer. With the data available, it is impossible to impute values for the user and these entries are thus useless for the current exercise. So I delete them from the dataframe:"""

df[df.Description.isna()==True].sort_values(by='UnitPrice',ascending=False)

"""`We can see that the data point with the values missing are just some faulty entries with zero Unit Price. So we can delete them`"""

df.dropna(subset=['CustomerID'],axis=0,inplace=True)
pd.DataFrame(data={'Data Type':df.dtypes.values,'Null Values':df.isna().sum().values,
        '%age of Null Values':[round(df.isna().sum().values[i]*100/len(df),2) for i in range(len(df.columns))]},index=df.columns).T

### Checking for Duplicates
print('The number of Duplicates are ',df.duplicated().sum())
df[df.duplicated()==True]

df.drop_duplicates(inplace=True)

df.duplicated().sum()

"""## 2. Exploring the Data

### `Country`
"""

df.Country.unique()

df.Country.value_counts()

plt.figure(figsize=(18,8))
sns.countplot(df.Country,order=df.Country.value_counts(ascending=False).index[:10],palette='Accent')
plt.xticks(rotation=45)
plt.title('Top 10 Countries in terms of no of orders')
plt.show()

"""The above graph shows the percentage of orders from the top 10 countries, sorted by the number of orders. This shows that more than 90% of orders are coming from United Kingdom and no other country even makes up 3% of the orders in the data.

Therefore, for the purpose of this analysis, I will be taking data corresponding to orders from the United Kingdom. This subset will be made in one of the next steps and will be mentioned as required.

### `Customers and Products`
"""

#Let us now look at the total number of products, transactions, and customers in the data, 
#which correspond to the total unique stock codes, invoice number, and customer IDs present in the data.

pd.DataFrame([{'Products': len(df['StockCode'].value_counts()),    
               'Transactions': len(df['InvoiceNo'].value_counts()),
               'Customers': 4372,  
              }], index = ['Quantity'])

"""It can be seen that the data concern 4372 users and that they bought 3958 different products. The total number of transactions carried out is of the order of  ∼ 22'000.

will determine the number of products purchased in every transaction:
"""

temp=df.groupby('InvoiceNo',as_index=False).agg(
    {'Description':np.count_nonzero}).sort_values(by='Description',ascending=False)
temp.columns=['InvoiceNo','Total_Orders']
temp

"""The first lines of this list shows several things worthy of interest:

1. the existence of entries with the prefix C for the InvoiceNo variable: this indicates transactions that have been canceled
2. the existence of users who only came once and only purchased one product (e.g. nº12346)
3. the existence of frequent users that buy a large number of items at each order
"""

## Order Distribution per Invoice
plt.figure(figsize=(10,5))
plt.hist(temp.Total_Orders,bins=40)
plt.xlabel('Invoice')
plt.ylabel('Total Orders')
plt.show()

temp['check']=[str(np.where(str.startswith(str(k),'C')==False,'Not Cancelled','Cancelled')) for k in temp.InvoiceNo]

print(temp.check.value_counts())

sns.countplot(temp.check)
plt.grid()
plt.plot()

print('\nAround {}% of orders were cancelled'.format(round(temp.check.value_counts()[1]*100/len(temp),2)))

"""We note that the number of cancellations is quite large ( ∼ 16% of the total number of transactions)."""

df.head()[:2]

"""### `Stock Code`"""

temp=pd.DataFrame(data={'StockCode':df.StockCode,'Description':df.Description,'dtype':[str.isidentifier(str(k)) for k in df.StockCode]})
temp[temp.dtype==True][:5]

temp[temp.dtype==True].StockCode.unique()

codes=['POST', 'D', 'C2', 'M', 'PADS', 'DOT', 'CRUK']
temp=temp[temp.StockCode.isin(codes)]
for code in codes:
    print("{:<15} -> {:<30}".format(code,temp[df.StockCode==code].Description.unique()[0]))

"""We see that there are several types of peculiar transactions, connected i.e., port charges, bank fee, discount, free gifts,etc"""

plt.figure(figsize=(10,5))
sns.countplot(temp.StockCode)
plt.xticks(rotation=60)
plt.show()

"""## `Total Amount per Billing`

In order to have a global view of the type of order performed in this dataset, I determine how the purchases are divided according to total Amount
"""

df['Amount']=df.UnitPrice*df.Quantity
df.head()

temp=df[(df.Quantity>0) & (df.StockCode.isin(codes).values==False)].groupby(
    'InvoiceNo',as_index=False).agg(
    {'Quantity':sum,'Amount':sum})
temp.head()

plt.figure(figsize=[18,5])
sns.distplot(temp[temp!=0].Amount,kde=False,)

"""Maximum orders are under $12500"""

bins = [-1,50,100,200,500,1000,5000,np.inf]
names = ['<50','50-100','100-200','200-500','500-1000','1000-5000','5000+']
temp['amount_cat']=pd.cut(temp['Amount'],bins,labels=names)

plt.figure(figsize=(7,7))
plt.pie(temp[temp.Amount>0].amount_cat.value_counts().values,labels=names,autopct = lambda x:'{:1.0f}%'.format(x) if x > 1 else '',
       shadow = True, startangle=0)
plt.show()

"""It can be seen that the vast majority of orders concern purcheses of low value ∼ 78% of purchases give prices in excess of £200."""

temp=df[(df.Quantity>0) & (df.StockCode.isin(codes).values==False)].groupby(
    'Country',as_index=False).agg(
    {'Quantity':sum,'Amount':sum})
temp.head()

plt.figure(figsize=(18,5))
sns.barplot(x='Country',y='Amount',data=temp[temp.Country!='United Kingdom'],)
plt.xticks(rotation=45)
plt.title('Country-wise Sales(UK not included)',size=15)
plt.show()

"""### I thought of implementing nltk to `create product categories` but it can happen that a particular category of product wasn't sold for the whole year. So generalising things to segregate all products in this clusters won't prove to be a good method

## 3. Understanding Cohort Analysis

What is Cohort Analysis?

A cohort is a set of users who share similar characteristics over time. Cohort analysis groups the users into mutually exclusive groups and their behaviour is measured over time.

It can provide information about product and customer lifecycle.

There are three types of cohort analysis:

1. Time cohorts: It groups customers by their purchase behaviour over time.
2. Behaviour cohorts: It groups customers by the product or service they signed up for.
3. Size cohorts: Refers to various sizes of customers who purchase company's products or services. This categorization can be based on the amount of spending in some period of time.

Understanding the needs of various cohorts can help a company design custom-made services or products for particular segments.

In the following analysis, we will create Time cohorts and look at customers who remain active during particular cohorts over a period of time that they transact over.

### `Time Cohorts`

`Checking the date range of our data, we find that it ranges from the start date: 2010–12–01 to the end date: 2011–12–09.`

`Next, a column called CohortMonth was created to indicate the month of the transaction by taking the first date of the month of InvoiceDate for each transaction. Then, information about the first month of the transaction was extracted, grouped by the CustomerID.`
"""

import datetime as dt

# Start and end dates:
print('Start date: {}'.format(df.InvoiceDate.min()))
print('End date: {}'.format(df.InvoiceDate.max()))

cohort_data = df[['InvoiceNo','StockCode','Description','Quantity','InvoiceDate','UnitPrice','Amount','CustomerID','Country']]

cohort_data.isna().sum()

cohort_data.InvoiceDate=pd.to_datetime(cohort_data.InvoiceDate).apply(lambda x:dt.datetime(x.year,x.month,x.day))

cohort_data.head()[:2]

grouping=cohort_data.groupby('CustomerID',as_index=False)['InvoiceDate'].min()
grouping.columns=['CustomerID','CohortMonth']
grouping['CohortMonth']=grouping['CohortMonth'].apply(lambda x:dt.datetime(x.year,x.month,1))
grouping.columns=['CustomerID','CohortMonth']
cohort_data=cohort_data.merge(grouping,on='CustomerID',how='left')
cohort_data.head()

cohort_data['CohortIndex']=pd.Series((cohort_data.InvoiceDate-cohort_data.CohortMonth)/30).dt.days.astype('int')

cohort_data.tail()

grouping=cohort_data.groupby(['CohortMonth','CohortIndex'],as_index=False).agg({'CustomerID':'nunique'})
cohort_counts=grouping.pivot_table(columns='CohortIndex',index='CohortMonth')
cohort_counts

"""What does the above table tell us?

Consider CohortMonth 2010–12–01: For CohortIndex 0, this tells us that 815 unique customers made transactions during CohortMonth 2010–12–01. For CohortIndex 1, this tells that there are 289 customers out of 815 who made their first transaction during CohortMonth 2010–12–01 and they also made transactions during the next month. That is, they remained active.

For CohortIndex 2, this tells that there are 263 customers out of 815 who made their first transaction during CohortMonth 2010–12–01 and they also made transactions during the second-next month. And so on for higher CohortIndices.

Let us now calculate the Retention Rate. It is defined as the percentage of active customers out of total customers. Since the number of active customers in each cohort corresponds to the CohortIndex 0 values, we take the first column of the data as the cohort sizes.
"""

cohort_sizes = cohort_counts.iloc[:,0]

# Divide all values in the cohort_counts table by cohort_sizes
retention=cohort_counts.divide(cohort_sizes, axis=0)

# Review the retention table
retention=retention.round(3)*100
retention

plt.figure(figsize=(10, 8))
sns.heatmap(retention,annot=True,fmt = '0.1f',cmap ='BuGn')
plt.title('Retention rates')
plt.show()

"""# 4. RFM Segmentation

RFM stands for Recency, Frequency, and Monetary.

`RFM analysis is a commonly used technique to generate and assign a score to each customer based on how recent their last transaction was (Recency), how many transactions they have made in the last year (Frequency), and what the monetary value of their transaction was (Monetary).`

`RFM analysis helps to answer the following questions: Who was our most recent customer? How many times has he purchased items from our shop? And what is the total value of his trade? All this information can be critical to understanding how good or bad a customer is to the company.`

`After getting the RFM values, a common practice is to create ‘quartiles’ on each of the metrics and assigning the required order.`

We will be using Amount column to get the monetary value of each transaction. Calling the .describe() method on this column, we get:
"""

cohort_data.head()[:3]

"""The defination of recency takes into consideration a complete one year data. So, we'll crop out one year from the end of data"""

print("The Date Range we'll select will be\n")
start_date=cohort_data.InvoiceDate.max()-dt.timedelta(days=364)
print('Start Date: ',start_date)
print('End Date: ',cohort_data.InvoiceDate.max())

data_rfm=cohort_data[(cohort_data.InvoiceDate>=start_date) & (cohort_data.Amount>0)]
data_rfm.reset_index(drop=True,inplace=True)
data_rfm.head()

"""`Now, for RFM analysis, we need to define a ‘snapshot date’, which is the day on which we are conducting this analysis. Here, I have taken the snapshot date as the highest date in the data + 1 (The next day after the date till which the data was updated). This is equal to the date 2011–12–10. (YYYY-MM-DD)`"""

snapshot_date=data_rfm.InvoiceDate.max()+dt.timedelta(days=1) #The date at which the RFM Analysis should be taking place
print('Snapshot Date: ',snapshot_date)

# Aggregate data on a customer level

data=data_rfm.groupby('CustomerID',as_index=False).agg({'InvoiceDate':lambda x:(snapshot_date-x.max()).days,
                                        'InvoiceNo':'count',
                                        'Amount':'sum'}).rename(columns = {'InvoiceDate': 'Recency',
                                                                                   'InvoiceNo': 'Frequency',
                                                                                   'Amount': 'MonetaryValue'})
data.head()

"""`For the recency metric, the highest value, 4, will be assigned to the customers with the least recency value (since they are the most recent customers). `

`For the frequency and monetary metric, the highest value, 4, will be assigned to the customers with the Top 25% frequency and monetary values, respectively.` 

`After dividing the metrics into quartiles, we can collate the metrics into a single column (like a string of characters {like ‘213’}) to create classes of RFM values for our customers. We can divide the RFM metrics into lesser or more cuts depending on our requirements.`
"""

r_quartiles=pd.qcut(data.Recency,4,labels=[4,3,2,1])
f_quartiles=pd.qcut(data.Frequency,4,labels=[1,2,3,4])
m_quartiles=pd.qcut(data.MonetaryValue,4,labels=[1,2,3,4])

data['R']=r_quartiles
data['F']=f_quartiles
data['M']=m_quartiles

data.head()

data['RFM_Segment']=[str(data.R[i])+str(data.F[i])+str(data.M[i]) for i in range(len(data))]
data['RFM_Score']=data.R.astype('int')+data.F.astype('int')+data.M.astype('int')

data.head()

"""Let us now analyse RFM Score distribution and their groups."""

data.groupby('RFM_Score').agg({'Recency': 'mean',
                                'Frequency': 'mean',
                                'MonetaryValue': ['mean', 'count'] }).round(1)

"""As expected, customers with the lowest RFM scores have the highest recency value and the lowest frequency and monetary value, and the vice-versa is true as well.

#### `Finally, we can create segments within this score range of RFM_Score 3–12, by manually creating categories in our data:`
1. Customers with an RFM_Score greater than or equal to 9 can be put in the ‘Top’ category. 
2. Similarly, customers with an RFM_Score between 5 to 9 can be put in the ‘Middle’ category, and 
3. the rest can be put in the ‘Low’ category. 

Let us call our categories the ‘General_Segment’. Analyzing the mean values of recency, frequency, and monetary, we get:
"""

bins=[0,5,9,np.inf]
label=['Low','Middle','Top']
data['General_Segment']=pd.cut(data.RFM_Score,bins=bins,labels=label)

data.groupby('General_Segment').agg({'Recency':'mean',
                                    'Frequency':'mean',
                                    'MonetaryValue':['mean','count']}).round(1)

"""### In many scenarios, this would be okay. But, if we want to properly find out segments on our RFM values, we can use a clustering algorithm like K-means.

## Preprocessing data for Clustering

`In the next section, we are going to prepare the data for Kmeans clustering on RFM Score data. To do this, we need to preprocess the data so that it can meet the key assumptions of Kmeans algorithm, which are:`

`1. The varaiables should be distributed symmetrically
2. Variables should have similar average values
3. Variables should have similar standard deviation values`
"""

# Checking the distribution of Recency, Frequency and MonetaryValue variables.
plt.figure(figsize=(18,10))

# Plot distribution of var1
plt.subplot(3, 1, 1); sns.distplot(data['Recency'],bins=50)

# Plot distribution of var2
plt.subplot(3, 1, 2); sns.distplot(data['Frequency'],bins=100)

# Plot distribution of var3
plt.subplot(3, 1, 3); sns.distplot(data['MonetaryValue'],bins=100)

plt.show()

"""As we can see from the above plots, all the variables do not have a symmetrical distribution. All of them are skewed to the right. To remove the skewness, we can try the following transformations:

1. log transformations
2. Box-Cox transformations
3. Cube root transformations

The log transformation cannot be used for negative values. One common practice one can use here is to add a constant value to get a positive value and this is generally taken as the absolute of the least negative value of the variable to each observation. However, in our data, we do not have any negative values since we are dealing with customer transactions dataset.
"""

data[['Recency', 'Frequency', 'MonetaryValue']].describe().T

"""Min Value of every column > 0

Also, We also see that we do not get constant mean and standard deviation values.
"""

data.sample(5)

rfm_data = data[['Recency','Frequency','MonetaryValue']]

from sklearn.preprocessing import StandardScaler

# Unskew the data
data_log = np.log(rfm_data)

# Initialize a standard scaler and fit it
scaler = StandardScaler()
scaler.fit(data_log)

# Scale and center the data
data_normalized = scaler.transform(data_log)

# Create a pandas DataFrame
data_norm = pd.DataFrame(data=data_normalized, index=rfm_data.index, columns=rfm_data.columns)

data_norm.describe().round(2).T

"""Will check for skewness in Data now again"""

plt.figure(figsize=(18,10))

# Plot recency distribution
plt.subplot(3, 1, 1); sns.distplot(data_norm['Recency'])

# Plot frequency distribution
plt.subplot(3, 1, 2); sns.distplot(data_norm['Frequency'])

# Plot monetary value distribution
plt.subplot(3, 1, 3); sns.distplot(data_norm['MonetaryValue'])

# Show the plot
plt.show()

"""### `Skewness has been removed`

## Clustering with K-means Algorithm

We will build multiple clusters upon our RFM data and will try to find out the optimal number of clusters in our data using the `elbow method`.
"""

from sklearn.cluster import KMeans

sse=[]

#Fit KMeans and calculate sse for every k
for i in range(1,25,1):
    model=KMeans(n_clusters=i,random_state=40)
    model.fit(data_norm)
    sse.append(model.inertia_)

plt.figure(figsize=(10,4))

plt.title('The Elbow Method')
plt.xlabel('n_clusters'); 
plt.ylabel('Sum of squared errors')
plt.plot(range(1,25,1),sse,marker='o',markerfacecolor='r')
plt.xticks(ticks=range(0,25,1))
plt.grid()
plt.show()

"""From the above plot, we can see that the optimal number of cluster is 3 or 4 or 5.

Let us take k = 3 first.
"""

kmeans = KMeans(n_clusters=3, random_state=1)
kmeans.fit(data_norm)
cluster_labels = kmeans.labels_

data_norm_k3 = data_norm.assign(Cluster = cluster_labels) #Normalized RFM DATA
data_k3 = rfm_data.assign(Cluster = cluster_labels)#Orignal RFM Data

# Calculate average RFM values and size for each cluster like we did before
summary_k3 = data_k3.groupby(['Cluster']).agg({'Recency': 'mean',
                                                    'Frequency': 'mean',
                                                    'MonetaryValue': ['mean', 'count'],}).round(0)

summary_k3

"""Let us now take k = 4."""

kmeans = KMeans(n_clusters=4, random_state=1)
kmeans.fit(data_norm)
cluster_labels = kmeans.labels_

data_norm_k4 = data_norm.assign(Cluster = cluster_labels) #Normalized RFM DATA
data_k4 = rfm_data.assign(Cluster = cluster_labels)#Orignal RFM Data

# Calculate average RFM values and size for each cluster like we did before
summary_k4 = data_k4.groupby(['Cluster']).agg({'Recency': 'mean',
                                                    'Frequency': 'mean',
                                                    'MonetaryValue': ['mean', 'count'],}).round(0)

summary_k4

"""K=5"""

kmeans = KMeans(n_clusters=5, random_state=1)
kmeans.fit(data_norm)
cluster_labels = kmeans.labels_

data_norm_k5= data_norm.assign(Cluster = cluster_labels) #Normalized RFM DATA
data_k5= rfm_data.assign(Cluster = cluster_labels)#Orignal RFM Data

# Calculate average RFM values and size for each cluster like we did before
summary_k5 = data_k5.groupby(['Cluster']).agg({'Recency': 'mean',
                                                    'Frequency': 'mean',
                                                    'MonetaryValue': ['mean', 'count'],}).round(0)

summary_k5

"""## Profiling and Interpreting segments"""

display(summary_k3)
display(summary_k4)
display(summary_k5)

"""We can also build snakeplots to understand and compare the segments. Let us build a snakeplot for our data with all clusters value.

Before building snakeplots, let us assign back customerID values to the row indices.
"""

data_norm_k3.index = data['CustomerID'].astype(int)
data_norm_k4.index = data['CustomerID'].astype(int)
data_norm_k5.index = data['CustomerID'].astype(int)

data_norm_k4.head()

# Melt the data into along format so RFM values and metric names are stored in 1 column each like Feature and its value
data_melt_k3=pd.melt(data_norm_k3.reset_index(),id_vars=['CustomerID','Cluster'],
                  value_vars=['Recency','Frequency','MonetaryValue'],
                  var_name='Features',
                  value_name='Value')

data_melt_k4=pd.melt(data_norm_k4.reset_index(),id_vars=['CustomerID','Cluster'],
                  value_vars=['Recency','Frequency','MonetaryValue'],
                  var_name='Features',
                  value_name='Value')

data_melt_k5=pd.melt(data_norm_k5.reset_index(),id_vars=['CustomerID','Cluster'],
                  value_vars=['Recency','Frequency','MonetaryValue'],
                  var_name='Features',
                  value_name='Value')

data_melt_k4.head()

plt.figure(figsize=[18,4])
plt.title('Snake plot of standardized variables')
plt.subplot(1,3,1);sns.lineplot(x="Features", y="Value", hue='Cluster', data=data_melt_k3);plt.title('K=3')
plt.subplot(1,3,2);sns.lineplot(x="Features", y="Value", hue='Cluster', data=data_melt_k4);plt.title('K=4')
plt.subplot(1,3,3);sns.lineplot(x="Features", y="Value", hue='Cluster', data=data_melt_k5);plt.title('K=5')
plt.show()

"""From the above snake plot, we can see the distribution of recency, frequency, and monetary metric values across the clusters. The clusters seem to be separate from each other, which indicates a good heterogeneous mix of clusters. Best happens for k=3

#### `Assigning CustomerID index to data_k4 dataframe and rfm_data dataframe:`
"""

data_k4.index = data['CustomerID'].astype(int)
data_k4.head()

rfm_data.index = data['CustomerID'].astype(int)
rfm_data.head()

cluster_avg = data_k4.groupby(['Cluster']).mean()
population_avg = rfm_data.head().mean()

display(cluster_avg)
display(population_avg)

relative_imp = cluster_avg.divide(population_avg,axis=1)
relative_imp.round(2)

# Plot heatmap
plt.figure(figsize=(8, 4))
plt.title('Relative importance of Attributes')
sns.heatmap(data=relative_imp, annot=True, fmt='.2f', cmap='RdYlGn')
plt.show()

"""# Final Thoughts

From the above analysis, we can see that there should be 4 clusters in our data. To understand what these 4 clusters mean in a business scenario, we should look back the table comparing the clustering performance of 3 and 4 clusters for the mean values of recency, frequency, and monetary metric. On this basis, let us label the clusters as ‘New customers’, ‘Lost customers’, ‘Best customers’, and ‘At risk customers’.

Below is the table giving the RFM interpretation of each segment and the points that a company is recommended to keep in mind while designing the marketing strategy for that segment of customers.

![image](https://user-images.githubusercontent.com/86877457/132398189-8d90880b-6966-480b-944d-a9ffba803595.png)
"""