# Financial Customer 360

## Description

Customer 360 allows financial institutions to gain a comprehensive view of each customer's interactions, preferences, and needs across all touchpoints. Tigergraph can connect data silos across an institution such as banking transactions, online interactions, customer service inquiries, and social media engagements. The Customer 360 platform provides valuable insights for targeted product offerings. Additionally, it fosters stronger customer relationships, improves retention rates, and ultimately drives profitability through increased customer satisfaction and loyalty.

## Personas

In the given context, here is the breakdown: 

- `Customer Service Representative`: They would use the chatbot to quickly access a customer's transaction history, preferences, and any recent inquiries to provide immediate assistance.
- `Banking Consultant`: For providing personalized consultation and suggestions, these professionals would require access to comprehensive customer data.
- `Marketing Analyst`: To understand customer behavior, preferences, and buying patterns for making strategic marketing decisions, a marketing analyst would require access to diverse customer data.
- `Sales Manager`: They need access to customer data to understand their needs and offer tailored products, boosting sales.
- `Customer Relationship Manager`: CRM managers can use this application to understand the customer journey across multiple touchpoints and improve customer service.
- `Social Media Manager`: This role may use the platform to understand the customer experiences and views expressed over social media platforms.
- `Product Manager`: Accessing customer data can help Product Managers understand which products are popular with customers and why, thus helping to design better products.
- `Data Analyst`: They would use chatbot to fetch specific customer datasets for analysis purposes.
- `Retail Banker`: They might use the application to get a holistic view of customers' interactions and offer them personalized banking solutions.

```python
personas = [
    'Customer Service Representative',
    'Banking Consultant',
    'Marketing Analyst',
    'Sales Manager',
    'Customer Relationship Manager',
    'Social Media Manager',
    'Product Manager',
    'Data Analyst',
    'Retails Banker'
]
``` 

## Persona Questions

### Persona: Customer Service Representative 

1. What is the last banking transaction of [customer name]?
2. Can you show me the online interactions of [customer name] over the [time period]?
3. How many customer service inquiries did [customer name] make in the last [time period]?
4. What are the most common issues raised by [customer name] in their service inquiries?
5. Can you pull up the social media engagements of [customer name] over the past [time period]?
6. What are the product preferences of [customer name]?
7. What is the customer satisfaction score of [customer name]?
8. Has [customer name] shown any signs of disloyalty or dissatisfaction in the past [time period]?
9. Can you show me a comprehensive view of [customer name]'s interactions and preferences across all touchpoints?
10. What targeted product offerings should we consider for [customer name] based on our collected data? 
11. Can you provide me some insights on how to improve the retention rate of [customer name]?
12. How can we enhance the customer satisfaction of [customer name] in order to boost profitability?

### Persona: Banking Consultant 

1. What is the total number of banking transactions for customer [customer's name]?
2. How many online interactions has customer [customer's name] had in the past [time period]?
3. What are the preferences of customer [customer's name] in regards to our financial products?
4. Which are the preferred contact methods of customer [customer's name]? 
5. Has there been any recent customer service inquiry from [customer's name] in the last [time period]?
6. Can you show me the social media engagement data of customer [customer's name] over the past [time period]?
7. What kind of insights can be derived from the Customer 360 platform of [customer's name] for product targeting?
8. What can we do to improve our existing relationship with the customer [customer's name]?
9. What is the retention rate of our customers in the [specific product or service] for the last [time period]?
10. How can we increase customer satisfaction of [customer's name] to drive our profitability? 
11. What are the primary needs of customer [customer's name] that we haven't addressed yet? 
12. What areas can we address to improve customer [customer's name]'s loyalty?

### Persona: Marketing Analyst 

1. How many [customers] did we acquire in the previous [time period]?
2. What are the [product preferences] of customers in the [age group] demographic?
3. Is there a pattern in the [banking transactions] over the last [time period]?
4. How have online [interactions] trended in the last [time period]?
5. How many [customer service inquiries] were raised in the previous [time period]?
6. Show me the most common [social media engagements] during the last [time period]?
7. What are the top [product offerings] for [customers] based on their interactions and preferences?
8. What is the customer [retention rate] for the last [time period]?
9. How did the customer [satisfaction] score trend over the [time period]?
10. What is the [profitability] for the last [time period] linked to customer satisfaction and loyalty?
11. Show me a complete [customer 360 view] for the customer with [ID].
12. What are the churn prediction rates based on [customer interactions] data from the last [time period]?
13. What are the most effective channels for [customer engagement] during the last [time period]?
14. What were the main reasons for [customer complaints] during the last [time period]?
15. What are the common traits for our most [loyal customers] during the last [time period]?

### Persona: Sales Manager 

1. What are our total sales in the [time period]?
2. How many new customers have we acquired in the [geographic location] in the [time period]?
3. What were the sales trends for a particular [product] in the [time period]?
4. What are the most popular products in the [geographic location]?
5. What is the customer retention rate in the [time period]?
6. How effective have our targeted product offerings been in the [geographic location] in the [time period]?
7. Which banking transactions are the most frequent in the [time period]?
8. What are some common customer service inquiries in the [time period]?
9. What favored products or services emerge based on online interactions in the [time period]?
10. What is our profitability index for the [time period]?
11. What is the rate of customer satisfaction in the [geographic location] in the [time period]?
12. What are the popular trends on social media engagements concerning our products during the [time period]?
13. What is the significant predictors of customer loyalty in the [time period]?

### Persona: Customer Relationship Manager 

1. What is the current customer retention rate for the [time period]?
2. Can you provide an overview of [customer's name] recent transactions?
3. What are the preferred channels of communication for our customer, [customer name]?
4. Which banking products/services are most popular among our customers in the [geographic location]?
5. Can you list the recent customer service inquiries from [customer name]?
6. Have there been any significant changes in the spending behavior of [customer name] in the recent [time period]?
7. What were the most common reasons for customer complaints in the [time period]?
8. What are the key interests/preferences of [customer name] based on their online interactions and transactions?
9. What are the customer's main areas of concern based on their social media engagements in the [time period]?
10. What potential product offerings could we recommend to [customer's name] based on their interests and past transactions?
11. Can you provide a summary of the overall customer satisfaction rating for the [time period]?
12. What is the profitability trend from [customer name]'s account in the last [time period]?
13. Can you track the frequency of [customer name]'s banking transactions in the past [time period]?
14. Based on customer service inquiries, what are the main issues faced by [customer's name]?
15. Can you show how our targeted product offerings have been received by our customers in the [geographic location] during the [time period]?

### Persona: Social Media Manager 

1. What's the total number of [customer name] interactions across all our social media platforms in the last [time period]?
2. How many [customer name] inquiries were registered through social media platforms in the last [time period]?
3. Can you give me a breakdown of [customer name]'s online interaction across our various social media platforms for the last [time period]?
4. What type of content does [customer name] usually interact with on our social platforms?
5. Which platform does [customer name] use the most for interactions and inquiries?
6. What has been the sentiment of [customer name]'s social media interactions over the last [time period]?
7. Are there any trends or patterns observed in the [customer name]'s interaction with our social media over the [time period]?
8. What is the level of engagement for our recent promotional post on [social media platform] within a [time frame]?
9. What were the top performing posts on [social media platform] over the past [time period]? 
10. How has the social media engagement for [product/service] changed over [time period]? 
11. How many new followers have we gained on [social media platform] over the last [time period]?
12. Which demographic is most engaged with our [specific campaign or product] on [social media platform] during the [time period]?

### Persona: Product Manager 

1. What are the key features of the Financial Customer 360 application?
2. How does Financial Customer 360 improve customer interactions across all touchpoints?
3. Can you explain how Tigergraph can connect data silos [across an institution]?
4. In what ways does Financial Customer 360 foster stronger customer relationships?
5. How can this platform improve our retention rates [over a specific time period]?
6. How can the Financial Customer 360 help drive profitability [across different geographical locations]?
7. What insights can the Customer 360 platform provide for targeted product offerings?
8. Can this application monitor social media engagements [of specific customer segments]?
9. Can you provide examples of how Financial Customer 360 has improved customer satisfaction and loyalty [in similar businesses]?
10. How does Financial Customer 360 handle customer service inquiries [across various channels]?
11. Are there any security features in place to protect the confidential data [of our customers] in Financial Customer 360? 
12. What level of customizability does Financial Customer 360 provide [in terms of user interface and functionality]?
13. Can you clarify how to integrate Financial Customer 360 with our existing systems?

### Persona: Data Analyst 

1. Can you show me the customer's transactions for the [time period]?
2. What is the total value of transactions made by [customer name] in the last [time period]?
3. What are the most common banking transactions made across all the customers during [time period]?
4. Can you provide a summary of [customer name]'s online interaction in [time period]?
5. How many customer service inquiries were received in the [time period]?
6. Can you show me the trend of social media engagements for the [time period]?
7. Which customers have the highest frequency of interactions across all touchpoints in the [time period]?
8. What are the most liked product offerings in our portfolio across customers?
9. Can you analyse the customer retention rate for the [time period]?
10. How has customer satisfaction influenced our profitability in the [time period]?
11. What are the common preferences of the customers who showed high loyalty in the [time period]?
12. Can I get the detailed profile and interaction history of [customer name]?
13. Show me the comparison of customer engagement on different channels for [time period].
14. What are the trending customer needs in the [time period]?
15. Can you identify the products or services that have led to increased customer satisfaction in the [time period]? 
16. What are the key factors influencing our retention rates during the [time period]?
17. How has the profitability trend been over the [time period]? 
18. What is the correlation between customer interactions and their banking transactions in the [time period]? 
19. Are there any outlier customers in terms of interactions or banking transactions in the [time period]?
20. Can you provide the average frequency of customer interactions across all touchpoints for the [time period]?



### Persona: Retails Banker 

1. What is the transaction history of customer [customer name] for the [time period]?
2. Which products does customer [customer name] currently have?
3. When was the last customer service inquiry made by customer [customer name]?
4. How many [type of transaction] has customer [customer name] conducted in the last [time period]?
5. What is customer [customer name]'s preferred channel of interaction (online, phone, in-person)?
6. What is the overall customer satisfaction score for customer [customer name]?
7. What are the most recent social media engagements of customer [customer name]?
8. What is the average transaction value of customer [customer name] in the last [time period]?
9. Has customer [customer name] shown any interest in [banking product name] recently?
10. What is the retention rate of our customers in the [geographic location] over the last [time period]?
11. Has there been any abnormal activity or behavior detected in customer [customer name]'s account recently?
12. How many active loans does customer [customer name] have at the moment?
13. Can you provide a breakdown of customer [customer name]’s transactions by [transaction category] for the last [time period]?
14. Has customer [customer name] set up any regular financial commitments or standing orders?
15. How has customer [customer name]'s credit score changed over the [time period]?
