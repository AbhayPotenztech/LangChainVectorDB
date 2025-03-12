import os

# Check if the OPENAI_API_KEY environment variable is set
api_key = os.environ.get('OPENAI_API_KEY')

if api_key:
    print(f"API Key is set: {api_key}")
else:
    print("API Key is NOT set!")