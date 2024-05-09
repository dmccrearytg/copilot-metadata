# Test of using Python formatted strings.

countries = ["USA", "France", "Spain"]

for country in countries:
    question = f"""
What is the capital of {country}?
"""
    # response = query_openai(question)
    print(f"Response from OpenAI for {country}:", question)