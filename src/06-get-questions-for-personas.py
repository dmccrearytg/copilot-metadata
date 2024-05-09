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
"Customer Service Representative",
"Branch Bank Manager",
"Fraud Investigator",
"Compliance Officer",
"Risk Analyst"]

question_template = """
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