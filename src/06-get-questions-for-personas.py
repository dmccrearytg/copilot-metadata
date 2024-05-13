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
    "Network Administrator", 
    "IT Manager", 
    "Data Analyst", 
    "IT Consultant", 
    "Threat Analyst", 
    "IT Auditor", 
    "Chief Information Officer", 
    "Research and Development Engineer",
    "Network Architect"
]

question_template = """
We have created a new web application product Network Digital Twin Knowledge Graph.

Cybersecurity is a crucial aspect of big organizations. Enterprises have their own data centers and their own network infrastructure involving a lot of devices. A well-planned attack can lead to serious issues, like data breach, corrupted files, and loss of data. Billions of dollars are lost each year due to cyberattacks.

TigerGraph allows you to connect data from different sources. Data at a scale of terabytes can be loaded into TigerGraph to give a comprehensive view of the network infrastructure of your organization. With visualizations in TigerGraph, users can gain a better visibility of the platform by seeing different components in their Network Infrastructure and tracing different paths leading from a suspicious device or IP address. Different graph algorithms can be run at scale and allows us to detect various kinds of cybersecurity attacks close to real-time. With TigerGraph, users can also extract graph features to Machine Learning models which has the potential to improve the accuracy of those models for tasks like anomaly detection.

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