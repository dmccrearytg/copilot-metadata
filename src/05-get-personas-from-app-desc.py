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
"""

response = query_openai(question)
print("Response from OpenAI:\n\n", response)