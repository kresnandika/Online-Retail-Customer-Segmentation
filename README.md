<!-- PROJECT LOGO -->
![image](https://user-images.githubusercontent.com/86877457/132400947-436793f0-dc39-4564-8758-ec70e54de0a0.jpg)
<br />
<p align="center">

  <h3 align="center">Customer Segmentation in Online Retail</h3>

  <p align="center">
    In this project, I'll try performing Customer Segmentation in Online Retail dataset using python, focussing on cohort analysis, understanding market base, sales and customer purchase patterns using RFM analysis and clustering.
    <br />
  </p>
</p>




<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
    </li>
    <li>
      <a href="#problem-statement">Problem Statement</a>
      <ul>
        <li><a href="#understanding-customer-segmentation">Understanding Customer Segmentation</a></li>
        <li><a href="#ways-to-segment-your-customers">Ways to Segment your Customers</a></li>
      </ul>
    </li>
    <li>
	<a href="#data-overview">Data Overview</a>
	<ul>
          <li><a href="#data-attributes">Data Attributes</a></li>
          <li><a href="#data-snapshot">Data Snapshot</a></li>
        </ul>
    </li>
    <li><a href="#implementaion">Implementaion</a>
	<ul>
          <li><a href="#exploring-the-data">Exploring the Data</a></li>
          <li><a href="#cohort-analysis">Cohort Analysis</a></li>
	  <li><a href="#rfm-segmentation">RFM Segmentation</a></li>
	  <li><a href="#clustering">Clustering</a></li>
        </ul>
    </li>
    <li><a href="#final-thoughts">Final Thoughts</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

Customer segmentation has a lot of potential benefits. It helps a company to develop an effective strategy for targeting its customers. This has a direct impact on the entire product development cycle, the budget management practices, and the plan for delivering targeted promotional content to customers. Customer segmentation can also help a company to understand how its customers are alike, what is important to them, and what is not. Often such information can be used to develop personalized relevant content for different customer bases. 

**As per the Pareto Principle, 80% of outcomes result from 20% of all the causes of any given event.**

In business terms, we can say that 20% of customers contribute 80% share of the total revenue of a company. That’s why finding this set of people is important. I will explain the importance of customer segmentation in a detailed manner later in this article itself.


<!-- PROBLEM STATEMENT -->
## Problem Statement

The overall aim of this process is to identify high-value customer base i.e. customers that have the highest growth potential or are the most profitable.

Insights from customer segmentation are used to develop tailor-made marketing campaigns and for designing overall marketing strategy and planning.

### Understanding Customer Segmentation

Customer segmentation is the process of separating customers into groups on the basis of their shared behavior or other attributes.

The type of segmentation criterion followed would create a big difference in the way the business operates and formulates its strategy. This is elucidated below.


1. Zero segments: This means that the company is treating all of its customers in a similar manner. In other words, there is no differentiated strategy and all of the customer base is being reached out by a single mass marketing campaign.
  
2. One segment: This means that the company is targeting a particular group or niche of customers in a tightly defined target market.
  
3. Two or more segments: This means that the company is targeting 2 or more groups within its customer base and is making specific marketing strategies for each segment.
  
4. Thousands of segments: This means that the company is treating each customer as unique and is making a customized offer for each one of them.

**Factors for segmentation for a business to consumer marketing company:**

1. **Demographic:** Age, Gender, Education, Ethnicity, Income, Employment, hobbies, etc.
2. **Recency, Frequency, and Monetary:** Time period of the last transaction, the frequency with which the customer transacts, and the total monetary value of trade.
3. **Behavioral:** Previous purchasing behavior, brand preferences, life events, etc.
4. **Psychographic:** Beliefs, personality, lifestyle, personal interest, motivation, priorities, etc.
5. **Geographical:** Country, zip code, climatic conditions, urban/rural areal differentiation, accessibility to markets, etc.

### Ways to Segment your Customers?

To start with customer segmentation, a company needs to have a clear vision and a goal in mind. 

The following steps can be undertaken to find segments in the customer base:

1. Analyze the existing customer pool
2. Develop an understanding of each customer
3. Define segment opportunities
4. Research the segment
5. Experiment with new strategies


<!-- DATA OVERVIEW -->
## Data Overview

Source: [The UCI Machine Learning Repository](https://bit.ly/3BPWgr4)

Data: This is a transnational data set which contains all the transactions occurring between 01/12/2010 and 09/12/2011 for a UK-based and registered non-store online retail. The company mainly sells unique all-occasion gifts. Many customers of the company are wholesalers.

Downloaded the xlxs file from Kaggle.

### Data Attributes

**1. InvoiceNo:** Invoice number. Nominal, a 6-digit integral number uniquely assigned to each transaction. If this code starts with letter ‘c’, it indicates a cancellation.

**2. StockCode:** Product (item) code. Nominal, a 5-digit integral number uniquely assigned to each distinct product.

**3. Description:** Product (item) name. Nominal.

**4. Quantity:** The quantities of each product (item) per transaction. Numeric.

**5. InvoiceDate:** Invoice Date and time. Numeric, the day and time when each transaction was generated.

**6. UnitPrice:** Unit price. Numeric, Product price per unit in sterling.

**7. CustomerID:** Customer number. Nominal, a 5-digit integral number uniquely assigned to each customer.

**8. Country:** Country name. Nominal, the name of the country where each customer resides.

### Data Snapshot

![image](https://miro.medium.com/max/2000/1*LiXE_SJlbXXTXoiLFasu7A.png)

<!-- IMPLEMANTATION -->
## Implementaion

**Real-world/Business objectives and constraints**

- Interpretability is important.
- Errors can be costly.
- Segmantation should suit the retail business

### Exploring the Data

Data was processed and cleaned. Here the duplicates were removed and the missing values were handled.

**Country**

Since the data, taken from the UCI Machine Learning repository describes the data to based on transactions for a UK-based and registered non-store online retail, let us check the percentage of orders from each country in the data.

![image](https://user-images.githubusercontent.com/86877457/132364248-5074e4c0-b17d-4b0e-ad34-83de485f3e93.png)

The above graph shows the percentage of orders from the top 10 countries, sorted by the number of orders. This shows that more than 90% of orders are coming from United Kingdom and no other country even makes up 3% of the orders in the data.

**Customers and Products**

The total number of products, transactions, and customers in the data, which correspond to the total unique stock codes was found out

![image](https://user-images.githubusercontent.com/86877457/132364618-7b91ea6c-72d5-4b38-aaac-da5d8a87978e.png)

It can be seen that the data concern 4372 users and that they bought 3958 different products. The total number of transactions carried out is of the order of ∼ 24000.

Many Order were cancelled and across the countries. As per the data, if the invoice number code starts with the letter ‘c’, it indicates a canceled order.

![image](https://user-images.githubusercontent.com/86877457/132365236-c3734aba-7a6f-4f66-8e57-b404449fbfd5.png)

We note that the number of cancellations is quite large ( ∼ 16% of the total number of transactions).
As we can see from the above figure, these cases are the ones where CustomerID values are NaNs and the decription mentioned check, lost, missing, smashed got these itmems. These cases were also removed from the data.

**Stock Code**

several types of peculiar transactions, connected i.e., port charges, bank fee, discount, free gifts, Carry bags, Samples, Amazon Fee,transaction fees which needed to be analysed.

![image](https://user-images.githubusercontent.com/86877457/132366457-8f51877b-885b-47c5-a684-de5e3fd30a3a.png)

**Net Amount/Invoice**

![image](https://user-images.githubusercontent.com/86877457/132366788-11d3cdef-3a24-43ff-a031-ed2648e03867.png)

*Amount shown are in UK Dollars

It can be seen that the vast majority of orders concern purcheses of low value ∼ 78% of purchases give prices in excess of £200.

![image](https://user-images.githubusercontent.com/86877457/132367301-c110a9f9-9566-41eb-ac66-628f4221fd69.png)

*UK not included. UK as expected topped the list int this category.

### Cohort Analysis
**What is Cohort Analysis**

A cohort is a set of users who share similar characteristics over time. Cohort analysis groups the users into mutually exclusive groups and their behaviour is measured over time.

There are three types of cohort analysis:

- **Time cohorts:** It groups customers by their purchase behaviour over time.
- **Behaviour cohorts:** It groups customers by the product or service they signed up for.
- **Size cohorts:** Refers to various sizes of customers who purchase company's products or services. This categorization can be based on the amount of spending in some period of time.

In the following analysis, I created 'Time Cohorts'

Checking the date range of our data, we find that it ranges from the start date: 2010–12–01 to the end date: 2011–12–09.

Next, a column called 'CohortMonth' was created to indicate the month of the transaction by taking the first date of the month of InvoiceDate for each transaction. Then, information about the first month of the transaction was extracted, grouped by the CustomerID.

![image](https://user-images.githubusercontent.com/86877457/132368576-33372fc3-6fc8-4e97-814f-f68394a06a2e.png)

Then I found the difference between the InvoiceMonth and the CohortMonth column in terms of the number of months to get the CohartIndex. Choartindex will tell us about the month of repurchase after their initial purchase.

![image](https://user-images.githubusercontent.com/86877457/132369142-a9ecc310-96aa-4347-b51e-8130e7103e3e.png)

After obtaining the above information, I obtained the cohort analysis matrix by grouping the data by CohortMonth and CohortIndex and aggregating on the CustomerID column.

![image](https://user-images.githubusercontent.com/86877457/132369533-f2581a25-31c9-458b-bb22-3a8f51ab6b96.png)

**What does the above table tell us?**

Consider CohortMonth 2010–12–01: For CohortIndex 0, this tells us that 948 unique customers made transactions during CohortMonth 2010–12–01. For CohortIndex 1, this tells that there are 341 customers out of 948 who made their first transaction during CohortMonth 2010–12–01 and they also made transactions during the next month. That is, they remained active.

Now I calculated the Retention Rate. It is defined as the percentage of active customers out of total customers.

![image](https://user-images.githubusercontent.com/86877457/132369804-450dd1c8-c907-45e4-b8c4-ef3646ca1efc.png)

From the above retention rate heatmap, we can see that there is an average retention of ~35% for the CohortMonth 2010–12–01, with the highest retention rate occurring after 11 months (49.3%). For all the other CohortMonths, the average retention rates are around 18–25%

### RFM Segmentation
RFM stands for **Recency, Frequency, and Monetary.**

RFM analysis is a commonly used technique to generate and assign a score to each customer based on how recent their last transaction was (Recency), how many transactions they have made in the last year (Frequency), and what the monetary value of their transaction was (Monetary).

RFM analysis helps to answer the following questions: Who was our most recent customer? How many times has he purchased items from our shop? And what is the total value of his trade? All this information can be critical to understanding how good or bad a customer is to the company.

After getting the RFM values, a common practice is to create ‘quartiles’ on each of the metrics and assigning the required order.

I used the net Amount to get the monetary value of each transaction i.e., per CustomerID
For RFM analysis, we need to define a ‘snapshot date’, which is the day on which we are conducting this analysis. Here, I have taken the snapshot date as the highest date in the (last date on data + 1). This is equal to the date 2011–12–10.(YYYY-MM-DD)

![image](https://user-images.githubusercontent.com/86877457/132370764-8099ed38-835c-4557-a320-4b543eb8e17b.png)

![image](https://user-images.githubusercontent.com/86877457/132370812-5db15f56-9c46-4a52-878e-f35818749513.png)

Then, I created 4 quartiles segment on this data with split at [25%ile,50%ile,75%ile] and collate these scores into an RFM_Segment column by assigning a score(1,2,3,4) value [R,F,M] respectively to the attributes.

- For the recency metric, the highest value, 4, will be assigned to the customers with the least recency value (since they are the most recent customers).
- For the frequency and monetary metric, the highest value, 4, will be assigned to the customers with the Top 25% frequency and monetary values, respectively.

After dividing the metrics into quartiles, The RFM_Score is calculated by summing up the RFM quartile metrics and RFM_Segment is calulated by collating them as a string of characters. 

![image](https://user-images.githubusercontent.com/86877457/132371242-2643a720-7499-4923-ad50-75385903f6e8.png)

Now the data can be grouped on the basis of RFM Score and mean attributes value can be compared for varoius RFM scores.

![image](https://user-images.githubusercontent.com/86877457/132385657-6d8acfb4-46b8-4b0f-855b-9a5c3608aead.png)

**MY ANALYSIS FROM RFM SEGMENTATION**

As expected, customers with the lowest RFM scores have the highest recency value and the lowest frequency and monetary value, and the vice-versa is true as well.

This data was clustred in three groups on the basis of RFM Score(3-12):
- **'Low':** RFM Score < 5
- **'Middle':** 5 <= RFM Score < 9
- **'Top':** RFM Score >= 9

![image](https://user-images.githubusercontent.com/86877457/132386098-ef6a5e7d-389e-4802-9dd0-92c6a1cd0248.png)

In many scenarios, this would have been okay. But, if we want to properly find out segments on our RFM values, we can use a clustering algorithm like K-means.

### Clustering
I chose K-Means clustering because the attribute were explicitly labelled. 

**Preprocessing data for Clustering**

Firstly, I prepared the data for Kmeans clustering on RFM Score data so that it can meet the key assumptions of Kmeans algorithm, which are:

1. The varaiables should be distributed symmetrically
2. Variables should have similar average values
3. Variables should have similar standard deviation values

![image](https://user-images.githubusercontent.com/86877457/132389115-97fc0124-9c2d-40c1-8f48-b03d49f2b164.png)

As you can see from the above plots, all the variables do not have a symmetrical distribution. All of them are skewed to the right. To remove the skewness, we can try the following transformations:

- Log transformations
- Box-Cox transformations
- Cube root transformations

The log transformation cannot be used for negative values. However, this data do not have any negative values since it is a customer transactions dataset.

After performming log transform and standardising the date, **Skewness has been removed**

![image](https://user-images.githubusercontent.com/86877457/132389568-138f5fbf-54f0-4bf5-ac73-4fa88c395ff8.png)



**Clustering with K-means Algorithm**

I performed K-means Clsutering on the data and follwed the 'Elbow Method' to get the optimal number of clusters. One can also use silhouette analysis to find the optimal number of clusters. For the purpose of this analysis, I have only used the elbow plot method.

![image](https://user-images.githubusercontent.com/86877457/132389865-11f63b62-b931-4ca4-9813-481ca34abf02.png)

From the above plot, the optimal number can be taken as 3 or 4 or 5.

So, after grouping the data in their clusters, for each value among 3, 4 and 5
For interpreting this segment, I drew Snake Plot fro all three values.

![image](https://user-images.githubusercontent.com/86877457/132392045-e1613880-251c-4532-b431-062e36571fad.png)

From the above snake plot, we can see the distribution of recency, frequency, and monetary metric values across the clusters. The clusters seem to be separate from each other, which indicates a good heterogeneous mix of clusters. Best happens for k=3. But k=4 happens to be more practical.

As the final step in this analysis,I extracted this information now for each customer and grouped them in the clusters formed that can be used to map the customer with their relative importance by the company:

This can be approched by finding the relative importance of each attributes for each clusters so that the company can focus more on the attribute of max importance for a particular cluster of customers. Ths was calculated by dividing the Mean value of attributes of each cluster and dividing it by the overall population average. A heatmap was plotted for the result:

![image](https://user-images.githubusercontent.com/86877457/132393027-28b9f33b-8836-4d2c-ae75-74e7174a2531.png)

<!-- FINAL THOUGHTS -->
## Final Thoughts

From the above analysis, we can see that there should be 4 clusters in our data. To understand what these 4 clusters mean in a business scenario, we should look back the table comparing the clustering performance of RFM Segmentation Model and 4 clusters for the mean values of recency, frequency, and monetary metric. On this basis, let us label the clusters as **‘New customers’, ‘Lost customers’, ‘Loyal customers’, and ‘At Risk customers’.**

**MY INTERPRETATION**

![image](https://user-images.githubusercontent.com/86877457/132398189-8d90880b-6966-480b-944d-a9ffba803595.png)

**FURTHER IMPROVEMENT**
- Product Category could be incorporated into the segmentation. Further product description can be used to derive the product categories with the help of NLP.
- Conducting deeper segmentation on customers based on their geographical location, and demographic and psychographic factors.
- Taking other factors such as geographical location, demographic, psychographic factors and purchase history into consideration we can build a predictive model to predict thier next purchase for them and for the customers with similar attributes.
