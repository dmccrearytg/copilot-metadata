# Get Questions For Each Persona
# Assume the OpenAI API Key is stored in the OPENAI_API_KEY environment variable

import requests
import os  # Required to access environment variables

def query_openai(question, temperature=0.0):
    # Retrieve your OpenAI API key from an environment variable
    api_key = os.getenv('OPENAI_API_KEY')
    
    if not api_key:
        return "API key is not set in environment variables."
    
    # Define the URL for the OpenAI API (this example uses the ChatGPT model)
    url = 'https://api.openai.com/v1/chat/completions'
    
    # Set up the headers with your API key
    headers = {
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json',
    }
    
    # Define the data payload for the POST request
    data = {
        "model": "gpt-4",
        "messages": [{"role": "user", "content": question}],
    }
    
    # Make the POST request to the OpenAI API
    response = requests.post(url, headers=headers, json=data)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Get the response content
        return response.json()['choices'][0]['message']['content']
    else:
        # If there was an error, return the error message
        return f"Error: {response.status_code} - {response.text}"

# Step 1: Get a list of the personals

personas = [
    "Financial Fraud Investigator", 
    "Anti-Money Laundering Compliance Officer", 
    "Forensic Accountant", 
    "Bank Auditor", 
    "Legal Counsel specializing in financial crimes", 
    "Risk Manager", 
    "Regulatory Compliance Officer", 
    "Law Enforcement Officer specializing in financial crimes"
]

question_template = """
We have created a new application we call Mule account detection Application.  
Within financial crime is a critical endeavor aimed at identifying bank accounts that are used to receive and disperse money from illicit activities. These mule accounts, which may be involved either knowingly or unknowingly in these operations, present a significant challenge for financial institutions. The rapid movement of funds through an extensive and seemingly unconnected network of accounts, spread across numerous financial institutions, complicates the tracking and halting of such illicit transactions. Financial institutions are therefore tasked with detecting this activity promptly to prevent further fund transfers and ensure the return of assets to their rightful owners. TigerGraph's solutions address this challenge through a suite of sophisticated graph algorithms that enable real-time monitoring, feature engineering for machine learning, and anomaly detection to trace illegal funds effectively. Community Detection is employed to unveil clusters within the transaction network, highlighting groups of accounts that work in concert to move illicit funds. The Centrality (PageRank) algorithm identifies key accounts that act as central nodes in the distribution network, crucial for disrupting the flow of illicit money. Closeness (Shortest Path) analysis reveals the most direct routes for money laundering, aiding in the trace back to the source. Lastly, Deep Link Analysis uncovers hidden connections between accounts, providing a comprehensive understanding of the network's structure and operation. Together, these algorithms form the backbone of TigerGraph's approach to dismantling the complex networks of mule accounts, safeguarding the financial system against the movement of illicit funds.

For the persona {}, what are the most common questions that this role
would ask a chatbot?

For each question, include the parameters to the question in square brackets: "[" and "]".
For example, use [geographic location] or [time period] if the question has location and time paraemters.
Return the results in Markdown numbered list format.
"""

for persona in personas:
    question = question_template.format(persona)
    response = query_openai(question)
    print("\n\n")
    print("## Persona:", persona, "\n")
    print(response)

print("\nDone\n")