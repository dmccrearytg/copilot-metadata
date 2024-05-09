# Mule Account Detection

## Description

Mule account detection in financial crime is a critical endeavor aimed at identifying bank accounts that are used to receive and disperse money from illicit activities. These mule accounts, which may be involved either knowingly or unknowingly in these operations, present a significant challenge for financial institutions. The rapid movement of funds through an extensive and seemingly unconnected network of accounts, spread across numerous financial institutions, complicates the tracking and halting of such illicit transactions. Financial institutions are therefore tasked with detecting this activity promptly to prevent further fund transfers and ensure the return of assets to their rightful owners. TigerGraph's solutions address this challenge through a suite of sophisticated graph algorithms that enable real-time monitoring, feature engineering for machine learning, and anomaly detection to trace illegal funds effectively. Community Detection is employed to unveil clusters within the transaction network, highlighting groups of accounts that work in concert to move illicit funds. The Centrality (PageRank) algorithm identifies key accounts that act as central nodes in the distribution network, crucial for disrupting the flow of illicit money. Closeness (Shortest Path) analysis reveals the most direct routes for money laundering, aiding in the trace back to the source. Lastly, Deep Link Analysis uncovers hidden connections between accounts, providing a comprehensive understanding of the network's structure and operation. Together, these algorithms form the backbone of TigerGraph's approach to dismantling the complex networks of mule accounts, safeguarding the financial system against the movement of illicit funds.

## Prompt

## Personas

```python 
[
    "Financial Fraud Investigator", 
    "Anti-Money Laundering Compliance Officer", 
    "Forensic Accountant", 
    "Bank Auditor", 
    "Legal Counsel specializing in financial crimes", 
    "Risk Manager", 
    "Regulatory Compliance Officer", 
    "Law Enforcement Officer specializing in financial crimes"
]
```

## Questions

## Persona: Financial Fraud Investigator 

1. What is the total volume of funds transferred through [suspected mule account number] in the [time period]?
2. Have there been any unusual patterns or suspicious activities detected in [suspected mule account number] within the [time period]?
3. Can you display a transaction network graph highlighting clusters related to [suspected mule account number]?
4. Among the transactions in the [time period], can you identify the most direct routes for fund transfers linked to [suspected mule account number]?
5. Who are the central accounts or nodes in the distribution network involving [suspected mule account number] in the [time period]?
6. Run a Deep Link Analysis on the recent transactions related to [suspected mule account number] within the [time period].
7. Can you identify any hidden connections related to [suspected mule account number] within the [time period]?
8. Run a Centrality (PageRank) algorithm on the data for [suspected mule account number] to identify key accounts in the [time period].
9. Can you provide a summary of all the activities associated with [suspected mule account number] in the [time period]?
10. Based on the Closeness (Shortest Path) analysis, what is the most likely source of funds for [suspected mule account number] in the [time period]?
11. Can you provide me the list of accounts that most interacted with [suspected mule account number] during the [time period]?
12. Have there been any reported illicit activities associated with any accounts connected to [suspected mule account number] in the [time period]?
13. Can you provide a visualization of the transaction network related to [suspected mule account number] during the [time period]?
14. Can you run the Community Detection algorithm on the data for [suspected mule account number] to identify clusters in the [time period]? 
15. Can you forecast potential unusual activities for [suspected mule account number] in the upcoming [future time period] based on past data?



## Persona: Anti-Money Laundering Compliance Officer 

1. What are the new [red flag] indicators detected by Mule Account Detection Application?
2. Can you display the [risk rating] of this [account number] in Mule Account Detection Application?
3. How many [accounts] have been associated with money laundering activities in the past [time period]?
4. Which [accounts] have shown high-velocity fund transfers in the last [time period]?
5. Can you provide a summary of [suspicious activities] reported by the Mule Account Detection Application over the last [time period]?
6. How many [accounts] have been flagged as high-risk mule accounts in the past [time period]?
7. Can you provide a list of the top 10 [accounts] which have received the most money from illicit activities?
8. Can you provide a network map showing the transactions of account number [account number]?
9. What are the common patterns detected in recent [suspicious financial transactions]?
10. Which [financial institutions] have been involved in the largest number of mule account transactions in the last [time period]?
11. Can you filter the flagged mule accounts based on [geographic location]? 
12. Can you provide a detailed transaction history of the flagged account number [account number]?
13. Can you highlight the links between high-risk [accounts] and their associated [transaction network]?
14. How has the network of mule accounts evolved over the last [time period]?
15. Can you display the shortest transaction routes linked to mule accounts for the last [time period]?



## Persona: Forensic Accountant 

1. What is the total amount of funds that have been transferred through [specific mule account] over [time period]?
2. Can I get a list of all transactions involving [specific mule account] during [time period]?
3. What was the most frequently used mule account in [geographic location] during [time period]?
4. Could you identify the [top 5] accounts connected to [specific mule account]?
5. How does the [specific mule account] rank in terms of centrality (PageRank) in our network?
6. How many steps or transactions does it typically take for funds to travel from [source mule account] to [target mule account]?
7. Who is the primary owner of [specific mule account]?
8. Can you find any common links or patterns amongst the mule accounts detected in [geographic location] during [time period]?
9. Can you show a graph representation of the transaction network involved with [specific mule account] over [time period]?
10. What is the average transaction size for [specific mule account] over [time period]?
11. Can you find connections between [specific mule account] and known illicit organizations or entities?
12. Has there been an increase in transactions through mule accounts in [geographic location] over [time period]?
13. What group or cluster does the [specific mule account] belong to in our network?



## Persona: Bank Auditor 

1. What is the total number of suspicious transactions in [specific time period]?
2. Could you provide a list of flagged accounts involved in illegal activities during [specific time period]?
3. How many high-risk mule accounts have been identified within [geographic location]?
4. Can you trace the transaction history of [specific account number]?
5. What are the most active mule accounts in [geographic location] during [specific time period]?
6. Are there any common links or connections between [Account A] and [Account B]?
7. How many transactions were detected by the Centrality algorithm as potentially fraudulent within [specific time period]?
8. What is the level of risk associated with [specific account number] based on its past transactions?
9. Which accounts have been identified as central nodes in the illegal funds distribution network within [geographic location]?
10. Can you provide details about the group or cluster associated with [specific account number]?
11. Using the Closeness analysis, can you trace back the most direct routes for money laundering involving [specific account number]?
12. What are the hidden connections unveiled by the Deep Link Analysis connected to [specific account number]?
13. Can you show me the graph representation of transactions between mule accounts during [specific time period]?
14. What are the top detected anomalies in transactions during [specific time period] based on the features engineered for machine learning?
15. How effective is the real-time monitoring in detecting suspicious activities for [specific account number]?



## Persona: Legal Counsel specializing in financial crimes 

1. What is the current total amount of illicit funds detected by the Mule Account Detection Application in [specific time period]?
2. How many mule accounts have been identified by the application within the [specific time period]?
3. What are the top 5 bank accounts that the Centrality (PageRank) algorithm identified as key nodes in the [specific time-period]?
4. Can you provide a count of how many mule accounts have been detected within [geographic location]?
5. What are the trending patterns of illicit fund movement detected by the Deep Link Analysis over the past [specific time-period]?
6. How effective has the application been in disrupting the flow of illicit funds in [specific time period]?
7. What are the most common direct routes for money laundering identified by Closeness (Shortest Path) analysis in [specific time period]?
8. How many clusters of mule accounts have been detected by Community Detection in [specific time period]?
9. Could you provide a snapshot of the structure and operation of the identified mule account networks in [geographic location] within [specific time period]?
10. Which financial institutions had the most identified mule accounts by the application in [specific time period]?
11. What is the total value of assets returned to their rightful owners due to the detection and disruption of mule accounts within [specific time period]?
12. How many accounts were involved unknowingly in money laundering activities as detected by the application in [specific time period]?



## Persona: Risk Manager 

1. What is the total amount of illicit funds detected in the [time period]?
2. How many mule accounts were identified within the [time period]?
3. What was the average amount of money that passed through the mule accounts in the [time period]?
4. Can you show the transaction associated with [specific mule account number]?
5. Which geographic locations have the highest activities of mule accounts during the [time period]? 
6. How many mule accounts have been associated with [specific financial institution] in the [time period]?
7. Please show me the transactions conducted by [specific account] in [specific time period]. Are there any anomalies detected?
8. Which account(s) have shown sudden increase in transactions in the [time period]?
9. What direct routes for money laundering have been identified in the [time period]?
10. Which clusters within the transaction network were most active in [specific time period]?
11. What are the top 5 accounts that act as central nodes in the distribution network in the [time period]?
12. Can I get details of deep link analysis for account [specific account number]? 
13. Who are the rightful owners for the assets in account [specific mule account number]?
14. Can you show me the most complex networks of mule accounts detected in the [time period]?
15. How many accounts were involved knowingly and unknowingly in the mule activities during the [time period]?



## Persona: Regulatory Compliance Officer 

1. What are the [names/IDs] of the accounts flagged as potential mule accounts in the [last week/month/year]?
2. Can you show me a graph representation of the suspicious transactions between mule accounts in the [past week/month/year]?
3. How does the Centrality (PageRank) algorithm determine the key accounts in potential money laundering operations?
4. How many [bank accounts] have been found to be indirectly linked to the identified mule accounts?
5. Can you give a detailed analysis of the mule account network structure that was discovered in the [specified period]?
6. How many flagged transactions involved amounts exceeding [specific amount] in the [last month/year]?
7. How can we trace back to the source of these potentially illicit funds?
8. Can you provide the detailed transaction history of [account id/name], flagged as a mule account?
9. What is the shortest path analysis result for the account [account id/name] suspected of money laundering?
10. Explain the Community Detection feature in identifying groups of accounts involved in potential illicit fund flow.
11. How many [suspicious transactions] were detected by the system in [specific geographical location] during the [specific time period]?
12. Give me the statistical data on the assets returned to their rightful owners after detection of illicit transactions in [last month/quarter/year].



## Persona: Law Enforcement Officer specializing in financial crimes 

1. How many mule accounts have been detected in the [transaction period]?
2. Can you provide the details of the mule accounts detected within the [geographic location]?
3. What is the sum of funds transferred through mule accounts in the [time period]?
4. Can you identify the central nodes in the distribution network for the [time period]?
5. What community clusters have been uncovered in the transaction network for the [time period]?
6. What are the most direct routes for money laundering detected in the [time period]?
7. Can you show the hidden connections between accounts detected within the [time period]?
8. What actions have been taken to disrupt the flow of illicit money in the [time period]?
9. What are the top mule accounts involved in financial crimes within the [time period]?
10. How effective have the actions taken to dismantle the complex networks of mule accounts been in the [time period]?