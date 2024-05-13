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

We have created a new product called Anti-Money Laundering.

Anti-Money Laundering empowers financial institutions to detect and prevent financial crimes by modeling complex relationships between transactions, accounts, and entities as a graph.  Anti-Money Laundering enables financial institutions to monitor and detect suspicious transactions in real time, automate identification of high-risk customers and their activities, and track transaction flows with enhanced due diligence and Know-Your-Customer (KYC) compliance.  Anti-Money Laundering helps TigerGraph customers stay ahead of the curve in the fight against financial crime reducing risk of reputational damage and maintaining trust with their customers.

For this application, create a list of the top personas that would use this application. 
Do not list any personas that deal with application performance or security.
Focus only on personas that would use a chatbot to ask questions
 about the data within the application.
Return the list as a Python list data structure using the list name personas.
Order the list based on the most frequent users of the
application to the least frequent users of the application.
"""

response = query_openai(question)
print("Response from OpenAI:\n\n", response)