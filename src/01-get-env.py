# OpenAPI Environment Variable Test
# Assume the OpenAI API Key is stored in the OPENAI_API_KEY environment variable
# Make sure you export the variable to downstream processes with the export OPENAI_API_KEY
import requests
import os  # Required to access environment variables

api_key = os.getenv('OPENAI_API_KEY')

print(api_key)
