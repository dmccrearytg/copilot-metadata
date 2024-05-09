# Get Questions For Each Persona
# Assume the OpenAI API Key is stored in the OPENAI_API_KEY environment variable

import requests
import os  # Required to access environment variables

def query_openai(question):
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
    "Fraud Analyst",
    "Customer Service Representative",
    "Compliance Officer",
    "Risk Manager",
    "Auditor",
    "Data Scientist",
    "Operations Manager"
]

question_template = """
We have a application that does credit card transaction fraud detection.
It identifies and prevents unauthorized or deceptive transactions in real-time. 
It analyzes transaction data, including cardholder information,
transaction details, and historical patterns, to detect anomalies
and suspicious activity indicative of fraud. TigerGraph models
complex relationships and patterns among entities such as cardholders,
merchants, transactions, and geographic locations.
This enable detection of fraudulent networks and patterns
that may be difficult to uncover using traditional relational databases.
Using graph algorithms enable organizations to detect and respond to
fraudulent transactions quickly and efficiently, ultimately reducing
financial losses and protecting consumers from fraudulent activity.
We are building a chatbot that responds to questions for common personas.

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
    print(response)