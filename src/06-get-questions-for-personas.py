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
    "Financial Crime Investigation Analyst",
    "Compliance Officer",
    "Risk Management Officer",
    "AML (Anti-Money Laundering) Analyst",
    "Bank Manager",
    "Financial Adviser",
    "Customer Service Representative",
    "Board Members",
]

question_template = """
We have created a new product we call Anti-Money Laundering.

Anti-Money Laundering empowers financial institutions to detect and prevent financial crimes by modeling complex relationships between transactions, accounts, and entities as a graph.  Anti-Money Laundering enables financial institutions to monitor and detect suspicious transactions in real time, automate identification of high-risk customers and their activities, and track transaction flows with enhanced due diligence and Know-Your-Customer (KYC) compliance.  Anti-Money Laundering helps TigerGraph customers stay ahead of the curve in the fight against financial crime reducing risk of reputational damage and maintaining trust with their customers.

For the persona {}, what are the most common questions that this role
would ask a chatbot?

For each question, include the parameters to the question in square brackets: "[" and "]".
For example, use [geographic location] or [time period] if the question has location and time paraemters.
Return the results in Markdown numbered list format.
"""

for persona in personas:
    question = question_template.format(persona)
    response = query_openai(question)
    print("\n### Persona:", persona, "\n")
    print(response)

print("\nDone\n")