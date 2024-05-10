# Getting Started

There are several steps.

1. Get your Python virtual environment setup and add the necessary Python libraries.  We use Conda in this example.
2. Get your OpenAI API Key and put it in your .zshrc file so it is setup when you start a shell
3. Test your API Key
4. For a new application, generate the personas
5. For each Persona, generate the questions

## Conda Setup

We recommend you setup a named virtual environment with Conda or a Python VENV.

Here are the steps with Conda

```sh
conda create -n "copilot-metadata" python=3
conda activate copilot-metadata
pip install requests openai mkdocs mkdocs-material
```

You will need an OpenAI API Key

Store the key in your ~/.zshrc file
```sh
OPENAI_API_KEY=sk...
export OPENAI_API_KEY
```

## Test Your Environment Variable

```
echo $OPENAI_API_KEY
```

Run the following program Python program in the src directory that tests your OpenAI API Key works.

```sh
python src/01-openai-test.py
```

## Generate Personas from the Application Description

Edit the ```src/05-get-personas-from-app-desc.py``` Python program to add a description.  Use the following Python program:

```sh
python 05-get-personas-from-app-desc.py
```

That will generate a list of personas. You will use this list for the next section.
Make sure you review the list and remove any personas that are not appropriate
such as security and performance roles.

## Generate Questions for Each Persona

Take the description and list of personas and copy them into
the appropriate areas of the ```06-get-questions-for-personas.py``` program.

```sh
python 06-get-questions-for-personas.py
```

## TODO

1. Add a feature to take the application description as an input parameter in a file or
the section within a markdown documents after the ## Application Description section header.
2. Take the output of the first Python program and use it as the input to the second.