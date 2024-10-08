# CoPilot Metadata Glossary of Terms

This document contains a list of terms we use in the CoPilot project.  We draw on
many sources for CoPilot including the fields of semantics, knowledge representation, large-language models, machine learning and natural-language processing (NLP).

#### Alternate Label

Secondary or alternative terms are used to refer to a concept or entity in a graph. These labels include synonyms, abbreviations, or other variations that are recognized but less preferred than the primary label.

#### Broader Concept Relationship

A type of directed edge in a graph where one concept vertex (the broader) encompasses or is more general than another concept vertex (the narrower). This relationship is used to build hierarchical structures within the graph.

#### Chat History (User)

A collection of all prior questions and answers for a given session created by a user.

Our goal is to allow each user to view their prior chat histories on a session-by-session basis.

For example, a fraud investigator might have 10 tabs open for each investigation they are doing.  Each tab would include
the question and answer pairs for that investigation, but the question-answer pairs are never intermixed between sessions for a given user.

#### Chat Log (System)

A detailed record of a chat question and answers for all sessions for all users of the system.  Chat logs capture the sequence of messages exchanged between participants. Chat logs are essential for auditing, troubleshooting, and understanding the context of a conversation.

Note that Chat Logs are records of question-answer pairs with timestamps that are visible to all analyses for all users.
They are different from a [Chat History](#chat-history-user) which is a report that shows ONLY the
chat logs for a specific user.

#### Chat Session

A specific set of questions and answers requested by a user of a chatbot within a specific user interface such as a tab in a web browser.

All questions and answer pairs are kept together for chat history reporting.
There are no limits to the number of chat sessions that a specific user can run concurrently.

#### Concept Relationship

A general term for any type of directed or undirected edge in a graph that represents a relationship between two [Concept](#concept-vertex-type) vertices. These relationships are used to illustrate the semantic connections between different concepts.

#### Concept Vertex Type

A type of vertex in a graph that represents a general idea or category derived from the content of documents. Concept vertices are used to categorize and connect related entities and documents based on shared themes or topics.

Within TigerGraph CoPilot, a Concept Vertex Type has attributes for preferred labels, alternate labels, defintion, and history notes.

#### CoPilot

* See: [TigerGraph CoPilot](#tigergraph-copilot)

#### Data Lineage

The systematic tracking and documentation of the origin, processing, transformation, and movement of data throughout its entire lifecycle, from creation to consumption.

Data lineage involves tracing the history of data, including its sources, transformations, and transformations, to provide transparency, accountability, and trust in the data's accuracy, completeness, and integrity.

One feature that CoPilot can do is provide an "Info" button that shows details of how a question was
answered and if the answer came from a document, how the document traveled in it journey into CoPilot.

* See Also: [Provenance](#provenance)

#### Document Chunk

A segment of a document that has been separated from others based on structure, topic, or other relevant criteria. Chunks are used to simplify processing and enhance the analysis of large documents by focusing on manageable sections.

#### Document Chunker

A tool or process that divides documents into smaller, more manageable pieces or chunks based on predefined rules or algorithms. This facilitates a more detailed and efficient analysis of the content by treating each chunk as a separate unit for processing.

#### Definition

A statement that provides a clear and precise description of a concept or entity as represented in the graph, distinguishing it from related concepts or entities.

#### Document Vertex Type

A type of vertex in a graph representing individual documents. Each document vertex is connected to entity and concept vertices that are mentioned or inferred within the document.

#### DocumentCollection Vertex Type

A type of vertex representing a collection of related documents. This vertex type is used to organize and analyze clusters of documents as a single unit in the graph.

#### Entity Vertex Type

A type of vertex in a graph representing specific, identifiable entities (such as people, places, or organizations) mentioned in documents. These vertices are distinct from concepts as they refer to unique instances rather than general ideas.

Entities each may have a type such as Person, Location, Product, DateTime.
When common entities are discovered they can also become promoted to also become a **Concept**
and Concepts can then be grouped into categories to form Taxonomies.

#### Graph RAG

An architecture for combining graph representations with the RAG pattern to increase the quality of question answering systems over documents.

#### History Notes

Notes that provide historical context or track changes and developments related to a concept or entity in the graph over time.

History Notes are represented as a text attribute associated with a [Concept Vertex Type](#concept-vertex-type)

#### InqueryAI

The TigerGraph tools and frameworks that match questions to certified queries.

#### JSON Solution Kit Metadata

The file format used to store solution kit metadata.

#### JSON Schema

The file that describes the structure and definitions of Solution Kit metadata.

#### MedGraphRAG
I loved the MedGraphRAG paper.  I am promoting it on all my networks.
Junde Wu

#### Named Entity Resolution

The process of identifying, disambiguating, and linking mentions of entities in text to unique identifiers, typically within a predefined set of entity vertices in a graph. This facilitates accurate analysis of relationships and interactions between entities across documents.

#### Narrower Concept Relationship

A type of directed edge in a graph where one concept vertex (the narrower) is encompassed by or is more specific than another concept vertex (the broader). It represents the inverse of a broader concept relationship.

#### Negative Response

A response from a user that a question was not answered by a chatbot or agent.  Negative responses are analyzed by the system, classified and frequency analysis is generated.  This allows developers
to focus their efforts on creating queries that answer the most frequently unanswered questions.

#### Notes

General remarks or observations about a concept, entity, or relationship in the graph that do not fit into the more specific categories of scope or history notes. These can include usage guidelines, examples, or additional clarifications.

#### Preferred Label

The recommended term to be used by default when referring to a concept or entity in a graph. This label is typically the most common or widely accepted name for the concept or entity.

#### Prerequisite Concept Relationship

A type of directed edge in a graph indicates that understanding or knowledge of one concept vertex (the prerequisite) is necessary before another concept vertex can be fully understood.

#### Personas

A detailed representation of a hypothetical user based on user research and real data about similar users. Personas are used in business and software development to guide decisions about product features, navigation, interactions, and visual design by embodying the attributes, behaviors, goals, and motivations of different user segments.

All questions are classified by the persona that might ask this question.

#### POLE Entities

The main proper nouns in a text file.  The acronym POLE stands for Persons, Organizations, Locations and Events.  POLE entities usually don't represent abstract concepts, but they are easier for a large-language model to detect within a text document, so they are often extracted in an early pass of a NLP workflow.

#### Provenance

 Information about entities, activities, and people involved in producing a piece of data or thing, which can be used to form assessments about its quality, reliability or trustworthiness.

 * See also: Data Linage

#### Scope Notes

Notes that clarify the boundaries and context of a concept or entity within the graph, including what is covered and what is excluded from the concept or entity definition.

#### Startup Question

Each persona has a list of startup questions that are displayed when that person starts a chat session.

The metadata for each question has an indicator that is used to show the question is to be displayed.

#### TigerGraph CoPilot

The collective name for the generative AI tools used by TigerGraph to integrate LLMs, vector stores and create conversational AI experiences and enable intelligent agents.

#### Top Level Concept

The most general concept vertices in a graph are not subsumed by any broader concepts. These vertices often serve as primary categories or starting points for navigating the conceptual hierarchy of the graph.

#### Solution Kit

A TigerGraph predefined application designed specifically to showcase features of TigerGraph and CoPilot that differentiate our solution from other architectures.

#### SupportAI

The set of tools and libraries that enable TigerGraph to convert documents into graph format and link concepts into predefined
business terminologies, glossaries, controlled vocabularies and ontologies.

#### QueryAI

The process of using generative AI to generate GSQL code with a focus on adding WHERE clauses to existing queries
to narrow the result set.  Queries generated with these tools still must
pass a rigorous human-centered certification process.  This is a developer tool and is not intended for
non-GSQL staff.

#### Reification

The process of converting abstract concepts, relationships, or interactions into concrete entities within a graph. Reification involves creating new vertices or edges to represent these elements explicitly, allowing for more complex representations and analyses.