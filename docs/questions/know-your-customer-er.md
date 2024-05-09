# Know Your Customer Entity Resolution

## Description

The "Know Your Customer" application (KYC) verifies the identity of customers and assesses the potential risk of financial crime.  The Solution Kit collects and analyzes customer data, including personal information, transaction history, and other relevant data points, to ensure compliance with regulatory requirements and mitigate financial risks. The TigerGraph database models and analyzes complex relationships and connections between customers, accounts, transactions, and other entities. TigerGraph enables comprehensive link analysis, anomaly detection, and network visualization, allowing financial institutions to identify suspicious patterns and behaviors more effectively. Coupled with real-time processing and scalability, TigerGraph's KYC solution can analyze large volumes of data efficiently and adapt to evolving regulatory requirements and fraud threats, ultimately enhancing the accuracy and effectiveness of customer due diligence processes.

## Sample Prompt To Get Personas for KYC

```linenums="0"
We have created a Know Your Customer (KYC) application. 
This application verifies the identity of customers and 
assess potemtial risk of financial crime. Solution collects 
and analyzes customer data, including personal information, 
transaction history, and other relevant data points, 
to ensure compliance with regulatory requirements and mitigate 
financial risks. Graph databases models and analyzes complex 
relationships and connections between customers, accounts, 
transactions, and other entities. TigerGraph enables comprehensive 
link analysis, anomaly detection, and network visualization, 
allowing financial institutions to identify suspicious patterns 
and behaviors more effectively. Coupled with real-time processing 
and scalability, TigerGraph's KYC solution can analyze large volumes 
of data efficiently and adapt to evolving regulatory requirements and fraud threats, 
ultimately enhancing the accuracy and effectiveness of customer due diligence processes.

For this application, create a list of the top personas that would use this application. 
Do not list any personas that deal with application performance or security.
Focus only on personas that would use a chatbot to ask questions about the data within the application.
Return the list as a Python list data structure.
Order the list based on the most frequent users of the
application to the least frequent users of the application.
```

## Response

Note that these results are sorted from the most frequent users of the application to the least frequent users of the application.

1. **Customer Service Representative**: A Customer Service Representative would use the chatbot to help answer customer queries or to guide customers through the data within the application.

4. **Branch Bank Manager**: A Branch Bank Manager would use the KYC application to oversee the financial activities of the bank. They could use the application to ensure compliance with banking laws and regulations and to assess the risk portfolios of their customers.

2. **Fraud Investigator**: A Fraud Investigator would use the application to detect any suspicious patterns or behaviors among customers' data, enabling them to take necessary actions to mitigate financial risk.

3. **Financial Analyst**: A Financial Analyst conducts detailed financial analyses, reviewing economic performance of companies, and making investment recommendations. They would use this application to study the transaction history and other relevant data points of various customers.

4. **Compliance Officer**: A Compliance Officer is responsible for ensuring a company is being run legally and ethically, maintaining its compliance with various regulatory requirements. They would use the KYC application to verify the identity of customers and assess potential risks of financial crime.


Copy this code into the question generator Python program:

```py
personas = [
'Customer Service Representative'
'Branch Bank Manager',
'Fraud Investigator',
'Compliance Officer',
 'Risk Analyst']
 ```

 Persona: Customer Service Representative 

1. What is the current KYC status of [customer name or customer ID]?
2. Are there any pending KYC documents for [customer name or customer ID]?
3. Can you show me the transaction history of [customer name or customer ID] for [specific time period]?
4. Were there any identified suspicious activities for [customer name or customer ID] in the last [specific time period]?
5. Can the system identify any potential financial risks linked to [customer name or customer ID]?
6. Can I see a visual representation of the network connections for [customer name or customer ID]?
7. Can you provide me with the personal information of [customer name or customer ID] for compliance checks?
8. Are there any regulatory requirements that haven’t been met by [customer name or customer ID]?
9. Has [customer name or customer ID] been involved in any recent transactions with [another customer name or customer ID]?
10. Does [customer name or customer ID] have any connections with [other entity name or ID]?
11. Are there any anomalies or unusual patterns in the transactions of [customer name or customer ID]?
12. Is there an update required in the KYC of [customer name or customer ID] to adapt to new regulatory requirements?
13. What are the recent transactions of [customer name or customer ID] in the last [specific time period]?
14. Can you show the transaction history of [customer name or customer ID] between [date1] and [date2]?
15. Are there any red flags in the KYC details of [customer name or customer ID]?



Persona: Branch Bank Manager 

1. What is the current progress of [customer name]'s KYC verification?
2. Can you tell me the risk assessment result for [customer name]?
3. What types of anomalies were detected in the transaction history of [customer name]?
4. Could you provide a brief summary of the recent transactions of [customer name]?
5. Are there any customers who are non-compliant with regulatory requirements?
6. How many customers are yet to complete their KYC verification?
7. What is the total number of customers who have completed their KYC verification [this week/month/year]?
8. Can you identify any suspicious patterns in the transactions of [customer name]?
9. How does TigerGraph help improve the effectiveness of customer due diligence processes?
10. Are there any high-risk customers identified in the [geographic location] branch?
11. How many unverified customers do we have in the [geographic location] branch?
12. Is there any unusual transaction activity recorded in the recent [time period]? 
13. Can we conduct a comprehensive link analysis for [customer name]?
14. Could you show me a network visualization for our customers in the [geographic location] branch?
15. How can we further improve our adaptability towards evolving regulatory requirements and fraud threats?



Persona: Fraud Investigator 

1. What is the latest transaction history for [customer name]?
2. How many suspicious transactions have been detected in the last [time period]?
3. Can you show a link analysis for [customer name]?
4. What is the recent account activity level for [customer name]?
5. Are there any anomalies detected in the transactions of [customer name]?
6. Can you highlight the suspicious patterns associated with the account of [customer name]?
7. Show me the transaction history of [customer name] from [specific time period].
8. Provide me the detailed customer data for [customer name].
9. Has the KYC process identified any risks associated with [customer name]?
10. Have there been any transactions in [geographic location] for [customer name] in the past [time period]?
11. What is the overall risk level associated with the [customer name]?
12. Can you show the network visualization between [Customer A] and [Customer B]?
13. What are the latest regulatory requirements and fraud threats updates?
14. Have there been any jurisdiction issues for the transactions of [customer name] in [geographic location]?
15. Can you provide a comprehensive report on all the transactions made by [customer name] within the [time period]?



Persona: Compliance Officer 

1. What is the current financial risk of [Customer Name]?
2. Could you provide the transaction history for [Customer Name] during [Time Period]?
3. Are there any anomalies detected in transactions of [Customer Name]?
4. Can you show the details of [Transaction ID]?
5. What is the network visualization of transactions for [Customer Name]?
6. In [time period], how many suspicious activities were detected?
7. Are there any connections between [Customer Name] and the recent fraudulent activities?
8. Has [Customer Name] met all the compliance requirements for the [compliance check]?
9. Are all the documents updated for [Customer Name] in our KYC records?
10. What is the status of the KYC verification process for [Customer Name]?
11. Is there any recent change in the regulatory requirements that I should be aware of?
12. Can you provide a summary of all suspicious activities in [time period]?
13. How many new customers have been added in the [time period]?
14. What is the status of tax compliance for [Customer Name]?
15. How many customers are on the financial risk warning list currently?
16. Has the [Transaction ID] by [Customer Name] complied with all internal regulations and financial standards?
17. Can you generate a risk profile for [Customer Name] based on their most recent activities?
18. How is the overall compliance score calculated for [Customer Name]?
19. Are there any politically exposed persons (PEPs) connected to [Customer Name]?
20. Who are the top 5 customers with the highest number of flagged transactions in [time period]?



Persona: Risk Analyst 

1. What is the total number of high-risk customers in [specific time period]?
2. Can you show me the transaction history of customer [customer ID / name]?
3. How many suspicious transactions have we identified in [specific geographical location] within [specific time period]?
4. What is the detailed personal information linked to account ID [account ID]?
5. Can you list all the transactions for [customer ID / name] that occurred in [specific time period]?
6. Are there any anomalies detected in customer [customer ID / name] data?
7. Can you show the network visualization for customer [customer ID / name]?
8. Please detail the complex relationships and connections associated with [customer ID / name].
9. How have our customer due diligence processes improved over [specific time period]?
10. What are the new regulatory requirements implemented in [specific time period]?
11. How many high-risk customers are from [specific geographical location]?
12. Show me the account details and transaction history for accounts flagged in [specific time period].
13. Can you provide the statistical report of suspicious activities for [specific time period]?
14. Are there any customers having unusual increase in transactions during [specific time period]?
15. Can we identify any clear patterns in fraudulent activities in [specific geographical location] during [specific time period]?
