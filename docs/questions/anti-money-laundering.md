# Anti-Money Laundering

## Description

Anti-Money Laundering empowers financial institutions to detect and prevent financial crimes by modeling complex relationships between transactions, accounts, and entities as a graph.  Anti-Money Laundering enables financial institutions to monitor and detect suspicious transactions in real time, automate identification of high-risk customers and their activities, and track transaction flows with enhanced due diligence and Know-Your-Customer (KYC) compliance.  Anti-Money Laundering helps TigerGraph customers stay ahead of the curve in the fight against financial crime reducing risk of reputational damage and maintaining trust with their customers.

## Personas

```python
personas = [
    "Financial Crime Investigation Analyst",
    "Compliance Officer",
    "Risk Management Officer",
    "AML (Anti-Money Laundering) Analyst",
    "Bank Manager",
    "Financial Adviser",
    "Customer Service Representative",
    "Board Members",
]
```

## Persona Questions

### Persona: Financial Crime Investigation Analyst 

1. Can you provide a list of transactions made by [customer name] over the [time period]?
2. Is there any suspicious activity or transactions on the account of [customer name] in the past [time period]?
3. What are the top 10 high-risk customers based on their transactions in the last [time period]?
4. Can you provide transaction details of [transaction ID]?
5. Can you show the transaction flow of [customer name] for the [time period]?
6. Does the account of [customer name] comply with the KYC procedures? 
7. How many suspicious transactions have been detected in the last [time period]?
8. Can you show a graph view of the transactions made by [customer name] in the [time period]?
9. Who are the frequent transaction partners of [customer name] in the past [time period]?
10. Has there been any significant change in the transaction behavior of [customer name] in the last [time period]? 
11. Can you provide an overview of the financial activities in [geographic location] over the past [time period]?
12. What is the total value of transactions made by [customer name] over the past [time period]?
13. Are there any customers who have exceeded their transaction limit in the past [time period]?
14. Show the list of all transactions flagged as high risk in the last [time period].
15. Can you produce a report of all transactions conducted by [customer name] with [another customer name] within the [time period]?

### Persona: Compliance Officer 

1. What is the volume of suspicious transactions detected in the last [time period]?
2. Can you show the transaction behaviour of [customer name] over the past [time period]?
3. Who are the high-risk customers identified in the last [time period]?
4. What are the most common types of suspicious transactions identified in the last [time period]?
5. Show me the transactional links between [customer name] and other entities over the past [time period].
6. Can you provide a report of all flagged transactions for [customer name]?
7. What is the total amount involved in the suspicious transactions detected over the [time period]?
8. Can you generate a risk score for [potential customer name] based on their potential transaction behaviors?
9. How up-to-date is our Know-Your-Customer (KYC) compliance for all customers?
10. Who are the top [number] customers with the most transactions over the [time period]?
11. Provide a summary of transactional links between our customers and high-risk geographical locations in [geographic location].
12. What is our current due diligence status for [customer name]?
13. Are there any updates to anti-money laundering regulations that we need to be aware of?
14. What are the trend patterns of suspicious transactions identified over the [time period]?
15. How many customers have we lost due to suspicion of financial fraud in the past [time period]?

### Persona: Risk Management Officer 

1. What are the high-risk customers identified during [time period]?
2. How many suspicious transactions were detected today?
3. Can you update the status of the investigation on account number [account number]?
4. Could you list all transactions from [geographic location] that are identified as suspicious in the past [time-period]?
5. Is there any pattern identified in the financial transactions of customer [customer name/id]?
6. Which entities have the highest number of suspicious transactions in [geographic location] during [time period]?
7. How is our compliance with KYC norms in the [geographic location] for the [time period]?
8. What percentage of total transactions were identified as high-risk during [time-period]?
9. Is there a trend in the financial crimes detected over the past [time period]?
10. Could you detail the transaction flows of high-risk customers with enhanced due diligence?
11. What is the total value of suspicious transactions during [time period]?
12. Have there been any breaches in compliance regulations in the [time period]?
13. Who are the customers with the most repeated suspicious transactions in the past [time period]?
14. Show me a graph model of relations between accounts and transactions flagged as suspicious in the last [time period].
15. How often is the Anti-Money Laundering system updated with new detection rules and norms?

### Persona: AML (Anti-Money Laundering) Analyst 

1. What is the total volume of transactions for [specific customer] over the [time period]?
2. Can you provide a list of high-risk customers detected in the [time period]?
3. What is the transaction pattern of [specific customer] over the [time period]?
4. How many suspicious transactions have been detected in [specific geographic location] over the [time period]?
5. Can you provide a list of the most common suspicious activities detected in the [time period]?
6. Can you provide a breakdown of the types of suspicious transactions detected in [specific geographic location] over the [time period]?
7. What is the risk rating of [specific customer]?
8. Can you provide a transaction summary for [specific customer] over the [time period]?
9. Which customers had the highest transaction volumes over the [time period]?
10. Which customers had the most frequent transactions over the [time period]?
11. Have there been any changes in the transaction behavior of [specific customer] over [time period]?
12. What entities are most commonly involved in suspicious transactions over the [time period]?
13. Can you provide a report on the current AML compliance status for the [time period]?
14. Can you update me on any new regulatory changes affecting AML over the [time period]?
15. Who are the top [number] customers with the highest number of suspicious transactions in the [time period]?
16. Can you generate a risk profile for [specific customer]?
17. Can you provide a list of all transactions linked to [specific customer] over the [time period]?
18. Has [specific customer] been associated with any flagged entities over the [time period]?
19. Which customer transactions exceeded the normal threshold over the [time period]?
20. Can you identify any unusual patterns in transactions by [specific customer] over the [time period]?

### Persona: Bank Manager 

1. What is the current risk level of my [bank]?
2. Can you show me a list of the high-risk customers in the [time period]?
3. What were the suspicious transactions that took place in the last [time period]?
4. Can I get a detailed report on transaction flow for [customer name]?
5. Show me the financial relationship graph for [customer name]?
6. What is the status of KYC compliance for [customer name]?
7. How many alerted transactions have we had in the last [time period]?
8. Can you list out the top transactions by value in the last [time period]?
9. Who are the customers with the highest transaction volume in the last [time period]?
10. Can you provide a summary of due diligence reports for the last [time period]?
11. How many new high-risk customers have been identified in the last [time period]?
12. What is the total value of suspicious transactions in the last [time period]?
13. Who are the top five clients with suspicious activities in the last [time period]?
14. What are the types of transactions causing the most alerts in the last [time period]?
15. Can you provide a detailed report on the activities of [customer name] in the last [time period]?

### Persona: Financial Adviser 

1. What are the most recent suspicious transactions [time period]?
2. Can you provide a summary report of high-risk customers [time period]?
3. How does the Anti-Money laundering tool detect problem accounts?
4. Could you explain the process of flagging suspicious transactions in real-time [time period]?
5. What actions will the Anti-Money Laundering tool automatically take when it detects suspicious activities [time period]?
6. Can the tool highlight the complex relationships between various accounts, transactions and entities [time period]?
7. Does the Anti-Money Laundering tool automate the process of ‘Know Your Customer’ (KYC) compliance?
8. How does the system monitor transactions and detect potential laundering activities [time period]?
9. How does the Anti-Money laundering tool comply with the most recent AML regulations [geographic location]?
10. Can you generate a summary of suspicious transaction activities [time period]?
11. How can Anti-Money laundering tool help me to maintain the trust of my customers?
12. Can you warn me when transactions flow exceed the normal range [time period]?
13. Can you explain how the Anti-Money Laundering tool reduces the risk of reputational damage?
14. How does the Anti-Money Laundering tool stay up-to-date with the latest financial crime trends [time period]?
15. How can I set the Anti-Money laundering tool to notify me of any unusual customer activities [time period]?

### Persona: Customer Service Representative 

1. What does the Anti-Money Laundering solution do?
2. How can Anti-Money Laundering help us with [specific financial crime risks]?
3. Can Anti-Money Laundering help us track transactions in [real time/ delayed time]?
4. How can Anti-Money Laundering aid in identifying high-risk customers?
5. Can we use Anti-Money Laundering solution to increase our due diligence with regard to [specific type of transaction]?
6. Can Anti-Money Laundering help us meet our Know-Your-Customer (KYC) compliance requirements?
7. How does Anti-Money Laundering assist in tracking transaction flows?
8. Can we integrate Anti-Money Laundering with our existing systems?
9. How can Anti-Money Laundering reduce the risk of reputational damage? 
10. How does the Anti-Money Laundering solution work to maintain customer trust? 
11. What support does TigerGraph offer to address any issues or questions about the Anti-Money Laundering solution? 
12. How does Anti-Money Laundering handle sensitive customer data?

### Persona: Board Members 

1. What are the main features of the Anti-Money Laundering product?
2. How does Anti-Money Laundering system detect [specific type of financial crime]?
3. Can you explain how the real-time monitoring of suspicious transactions works with Anti-Money Laundering?
4. How automated is the identification of high-risk customers in the Anti-Money Laundering system?
5. In what way does Anti-Money Laundering help with our Know-Your-Customer (KYC) compliance?
6. What measures are in place to ensure the privacy and security of customer data with the Anti-Money Laundering product?
7. How does the Anti-Money Laundering platform deal with false positives in suspicious transaction detection?
8. Can the Anti-Money Laundering system be tailored to our organization's specific needs[specific needs or requirements]?
9. How does Anti-Money Laundering track transaction flows and for what [time period] can it do so?
10. Can the Anti-Money Laundering system integrate with our existing infrastructure or systems [existing systems]? 
11. How can Anti-Money Laundering help reduce the risk of reputational damage?
12. What are the costs associated with implementing the Anti-Money Laundering product?
13. How quickly can we expect to see results once the Anti-Money Laundering product is implemented?
14. How can Anti-Money Laundering help maintain trust with [customer segment]?
15. How does the Anti-Money Laundering tool allow us to stay ahead of new forms of financial crime?
