# Getting Started

## Conda Setup

```
conda create -n "copilot-metadata" python=3
conda activate copilot-metadata
pip install requests openai


You will need an OpenAI API Key

Store the key in your ~/.zshrc file
```
OPENAI_API_KEY=sk...
export OPENAI_API_KEY
```

Test:

```
echo $OPENAI_API_KEY
```

Run the following program

```sh
python src/01-openai-test.py
```
