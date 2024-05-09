# Test of using Python formatted strings.

countries = ["USA", "France", "Spain"]
question_template = """
What is the capital of {}?
"""

for country in countries:
    question = question_template.format(country)
    # response = query_openai(question)
    print("Question:", question)