# Generating Persona Questions

To generate a list of questions for each persona will need three items.

1. The Application Name
2. The Application Description
3. The Persona Name

## Sample Prompt

```linenums="0"
We have created a new web application product called {APPLICATION_NAME}.

{APPLICATION_DESCRIPTION}

For the persona {PERSONA}, what are the most common questions that this role
would ask a chatbot?

For each question, include the parameters to the question in square brackets: "[" and "]".
For example, use [geographic location] or [time period] if the question has location and time paraemters.
Return the results in Markdown numbered list format.
```

## Sample Program
