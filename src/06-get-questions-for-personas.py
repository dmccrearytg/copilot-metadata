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
    'E-Commerce Business Owner',
    'Marketing Manager',
    'Sales Manager',
    'Customer Service Representative',
    'Product Manager',
    'E-Commerce Strategist',
    'Supply Inventory Manager',
    'Business Analyst'
]

question_template = """
We have created a new application we call Merchant Product Recommendations.

Merchant Product Recommendations enhances the checkout experience by enabling financial payment providers with ability to suggest highly relevant products to customers at the point of sale. By analyzing the complex relationships between products, customers, and merchants, businesses can identify patterns and correlations that drive sales and revenue. With TigerGraph's graph database, businesses can analyze vast amounts of transactional data in real-time to uncover hidden patterns and correlations, provide personalized product recommendations that increase average order value and customer satisfaction, and optimize inventory and reduce waste by identifying slow-moving products optimizing product offerings.  Merchant Product Recommendations can help TigerGraph customers unlock new revenue streams, improve customer satisfaction, and establish a competitive edge in the e-commerce landscape.


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