# Generating CoPilot Personas

We need an accurate description of a Solution Kit application to generate a list
of personas that would use the application.  We can then use the following prompt structure:



## Prompt

```linenums="0" 
We have created a new Application called {APPLICATION_NAME}.

{APPLICATION DESCRIPTION}

For this application, create a list of the top personas that
would use a chatbot for this application. 
Do not list any personas that deal with application performance or security.
Focus only on personas that would use a chatbot to ask questions
about the data within the application.
If appropriate, include a persona.

Return a list of the persona names in a Python list called "personas".
Include a newline after each comma in the list.
Order the list based on the most frequent users of the
application to the least frequent users of the application.
```

## Sample Response

1. **Fraud Analyst: This professional is responsible for analyzing transactions to detect any fraudulent activities. They would use the application to track, monitor, and analyze data related to financial transactions and detect patterns indicative of fraudulent behavior.

2. Compliance Officer: They ensure the organization conducts business in full compliance with all national and international laws and regulations that pertain to its particular industry. This persona would use the application to ensure the organization is compliant with local, state, and federal rules about fraud detection and prevention.

3. Risk Manager: They're tasked with identifying and assessing potential risks in all areas of a financial organization. They would use the application to analyze transactions, pinpoint any risks, and implement measures to minimize potential loss.

4. IT Security Officer: This role involves protecting both data and systems from unauthorised access, use, disclosure, disruption, modification, or destruction. An IT security officer would be interested in the security aspects of the application to ensure the data and analysis are secure from any potential threats or breaches.

5. Legal Team: They guide the organization to work within the constraints of the law. They would also use the application for investigations and evidence in case of any legal proceedings.

6. Auditor: Uses the application to verify the accuracy of financial transactions and ensure no fraudulent activity has occurred. 

7. Financial Institutions/Banks: These entities would use the application to monitor the transactions of their clients and preemptively identify any suspicious or fraudulent activities.

8. End User/Customer: While they may not directly interact with the application, they are a key persona as they are the subject of the transactions being monitored for potential fraud. A significant aspect of a financial fraud transaction application's function is focused on maintaining the financial security of these individuals.



## Python Program

```python

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

We have created a new web application product called {APP_NAME}

{APPLICATION DESCRIPTION}

For this application, create a list of the top personas that would use this application. 
Do not list any personas that deal with application performance or security.
Focus only on personas that would use a chatbot to ask questions
 about the data within the application.

Return the list as a Python list data structure using the list name personas.  
Use one line for each persona and make sure to put a newline after each comma.
Order the list based on the most frequent users of the
application to the least frequent users of the application.
"""

response = query_openai(question)
print("Response from OpenAI:\n\n", response)
```
