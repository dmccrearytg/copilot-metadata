# OpenAPI Connection Test
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

# Example usage

question = """
Mule account detection in financial crime is a critical endeavor aimed at 
identifying bank accounts that are used to receive and disperse money from 
illicit activities. These mule accounts, which may be involved either knowingly 
or unknowingly in these operations, present a significant challenge for 
financial institutions. The rapid movement of funds through an extensive and 
seemingly unconnected network of accounts, spread across numerous financial 
institutions, complicates the tracking and halting of such illicit transactions. 
Financial institutions are therefore tasked with detecting this activity 
promptly to prevent further fund transfers and ensure the return of assets 
to their rightful owners. TigerGraph's solutions address this challenge 
through a suite of sophisticated graph algorithms that enable real-time 
monitoring, feature engineering for machine learning, and anomaly detection 
to trace illegal funds effectively. Community Detection is employed to unveil
 clusters within the transaction network, highlighting groups of accounts 
 that work in concert to move illicit funds. The Centrality (PageRank) 
 algorithm identifies key accounts that act as central nodes in the distribution network, 
 crucial for disrupting the flow of illicit money. Closeness (Shortest Path) analysis 
 reveals the most direct routes for money laundering, aiding in the trace back to the 
 source. Lastly, Deep Link Analysis uncovers hidden connections between accounts, 
 providing a comprehensive understanding of the network's structure and operation. 
 Together, these algorithms form the backbone of TigerGraph's approach to dismantling 
the complex networks of mule accounts, safeguarding the financial system 
against the movement of illicit funds.

For this application, create a list of the top personas that would use this application. 
Do not list any personas that deal with application performance or security.
Focus only on personas that would use a chatbot to ask questions
 about the data within the application.
Return the list as a Python list data structure.
Order the list based on the most frequent users of the
application to the least frequent users of the application.
"""

response = query_openai(question)
print("Response from OpenAI:\n\n", response)