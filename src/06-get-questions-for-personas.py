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
    'Supply Chain Manager', 
    'Operations Manager', 
    'Logistics Coordinator', 
    'Inventory Manager', 
    'Warehouse Manager', 
    'Purchasing Manager', 
    'Production Manager', 
    'Quality Assurance Manager', 
    'Top Management Executives']

question_template = """
We have created a new web application product called Supply chain management.

Supply chain management is full of dependencies: a product is the result of hundreds of upstream components and processes fulfilling their requirements.  Unfortunately, manufacturers (and other businesses that have multiple levels of inputs contributing to the final outputs) often cannot get basic reports on the bill of materials, timeliness and efficiency, because their information is spread across too many systems, or the systems are poor at working with dependencies.  A graph-based operational digital twin of a supply chain can solve these problems. The graph excels at modeling dependencies. Not only does it show you the current state of your supply chain (observability), but it can simulate operations, to help you respond agilely to shocks and to make preemptive changes to improve supply chain resiliency.
Observability and monitoring: 
Tracing impact and root causes: When a particular component/supply/region is disrupted and can't be fixed immediately, the business needs to be able to trace downstream to see what will be affected. A graph-based digital twin can show and report on downstream effects using a Directed Breadth-First Search.  Similarly, the digital twin can trace upstream to see what are the possible root causes of a defect.
Identifying alternatives: 
Assessing risks and improving resiliency: Supply change shocks and disruptions WILL occur, but well-prepared businesses work to minimize both the likelihood and impact of disruptions. Algorithms such as degree centrality and betweenness centrality can identify the riskiest stages of a supply chain.

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