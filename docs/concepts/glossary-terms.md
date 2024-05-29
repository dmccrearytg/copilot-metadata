# Glossary Terms

For CoPilot to work effectively, it is important to have clear definitions of business terms.
These terms are used in conversations people are having with their applications using TigerGraph CoPilot.
We use ISO/IEC 11197 Metadata Registry standards to generate precise definitions for these terms.
Here are the key characteristics of the business glossary defintions we use:

1. Precise
1. Concise
1. Distinct
1. Noncircular
1. Unencumbered with rules

There is a full blog entry [LLM Friendly Defitions](https://www.tigergraph.com/blog/llm-friendly-definitions-for-tigergraph-copilot/).  We can use an LLM, a Python program and a GitHub
action to generate a list of key terms from any Solution Kit description.

## Using a JSON File to Store Solution Kit Concepts

Glossary Terms can be stored in our concepts.json file.  The concepts file has a format like the following:

```json
[
    {
        "$schema": "concept-registry.jschema",
        "ConceptID": "suspicious-activity-report",
        "ConceptPrefLabel": "Suspicious Activity Report",
        "ConceptAltLabels": ["SAR"],
        "ConceptDefinition": "A document filed by financial institutions to report potential instances of money laundering, fraud, or other suspicious activities to regulatory authorities. It is used to alert authorities of transactions that may involve criminal activity, requiring detailed descriptions of the suspect behavior and any relevant account information.",
        "ConceptURI": ["http://tigergraph.com/metadata-registry/financial-fraud/suspicious-activity-report"],
        "ConceptExample": "A example of a SAR is a report that shows the same IP address was used to apply for many credit cards.",
        "ConceptComposability": "AND",
        "ConceptSource": "TigerGraph Solution Kit",
        "ConceptSourceMethod": "Manual review with ChatGPT",
        "ConceptApprovedDate": "2024-05-01",
        "ConceptApprovedBy": {
            "PersonFullName": "Sue Johnson",
            "Email": "sue.johnson@example.com"
        }
    }
]
```

The structure of this file can be validated by the ```concept-registry.jschema``` JSON Schema.
This file has the file extension .jschema.  The Concept schema is []()

## Generating an Initial List of Business Terms for an Application

Given a Solution Kit Description, here is a sample prompt you can use to create a list of ISO definitions:

```linenums="0"
Create a list of the 25 most common key business terms used in the application described by the following text:

{APPLICATION_DESCRIPTION}

Return a list of these terms in a JSON file.  Return the results in the following format.  For example:
[
   {"ConceptPrefLabel": "Suspicious Activity Report"},
   {"ConceptPrefLabel": "Non-Obiouse Relationship"}
]
```
