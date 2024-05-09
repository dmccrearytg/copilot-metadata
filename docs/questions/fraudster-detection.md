# Fraudster Detection

## Application Description

Identify individuals or entities engaging in fraudulent activities within the financial domain, such as unauthorized transactions, money laundering, or identity theft. For example, it may identify unusual spending patterns, multiple accounts linked to the same individual, or transactions involving high-risk entities or locations. Once potential fraudsters are identified, the solution may trigger alerts for manual review by fraud investigators or automatically block suspicious transactions in real-time. Graph algorithms such as community detection can identify clusters of interconnected entities that may represent fraud rings or syndicates. Link analysis algorithms can trace connections between suspicious entities and uncover commonalities or shared characteristics that may suggest collusion or coordination in fraudulent activities. Centrality measures can identify influential nodes within the network, such as individuals with many connections or accounts with high transaction volumes, which may be key players in fraudulent schemes.

## Persona Prompt

```linenums="0"
We have created a new application we call the "Fraudster Detection" application.  
The Fraudster Detection application identifies individuals or entities engaging in 
fraudulent activities within the financial domain, such as unauthorized transactions, 
money laundering, or identity theft.   For example, it may identify unusual spending 
patterns, multiple accounts linked to the same individual, or transactions involving 
high-risk entities or locations. Once potential fraudsters are identified, 
the solution may trigger alerts for manual review by fraud investigators or 
automatically block suspicious transactions in real-time. Graph algorithms 
such as community detection can identify clusters of interconnected entities 
that may represent fraud rings or syndicates. Link analysis algorithms can 
trace connections between suspicious entities and uncover commonalities or 
shared characteristics that may suggest collusion or coordination in fraudulent 
activities. Centrality measures can identify influential nodes within the network, 
such as individuals with many connections or accounts with high transaction volumes, 
which may be key players in fraudulent schemes.

For this application, create a list of the top personas that would use this application. 
Do not list any personas that deal with application performance or security.
Focus only on personas that would use a chatbot to ask questions
 about the data within the application.
Return the list as a Python list data structure.
Order the list based on the most frequent users of the
application to the least frequent users of the application.
```

## Persona Response

```Python
personas = [
    'Fraud Investigator',
    'Financial Crime Analyst',
    'Compliance Officer',
    'Risk Management Specialist',
    'Forensic Accountant',
    'Bank Manager',
    'Internal Auditor',
    'Law Enforcement Officer',
    'Regulatory Agency Representative'
]
```

The above roles represent people who would interact with the application in a professional capacity and use a chatbot to understand the data. They are ordered based on the assumption that individuals working directly with fraud detection and financial crime prevention (fraud investigator, financial crime analyst, etc.) would use it more frequently than those in more general or oversight roles (bank manager, law enforcement officer, etc.).