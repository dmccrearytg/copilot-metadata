# Metadata Loaders

When a Solution Kit is deployed, there are many tasks that must be run
to load subsets of the solution-kit-metadata.json file that must
be loaded into TigerGraph so that other tools can use this data.

Here are some tasks that we will need:

1. **Questions Loaded into Vector Store** - each question should be run through
a process that creates an embedding and this embedding is loaded into
a vector store.

2. **Persona Startup Questions** - when a chatbot starts up, it will display
a short list of sample questions that are used frequently or that demonstrate
a specific capability.  A list of all questions that have personal-based startup
flagged will need to be loaded into TigerGraph as a Question vertex and a GSQL
query such as ```getStartupQuestionForPersona(PERSONA)``` will be callable by a front end.  This
will return a JSON array with the question string and the script to call.