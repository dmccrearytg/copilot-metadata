# CoPilot Metadata Glossary of Terms

#### Alternate Label

Secondary or alternative terms used to refer to a concept or entity in a graph. These labels include synonyms, abbreviations, or other variations that are recognized but less preferred than the primary label.

#### Broader Concept Relationship

A type of directed edge in a graph where one concept vertex (the broader) encompasses or is more general than another concept vertex (the narrower). This relationship is used to build hierarchical structures within the graph.

#### Chat History (User)

A collection of all prior questions and answers in a session created by a user.
Our goal is to allow each user to view their prior chat histories.

#### Chat Log

A detailed record of a chat session, capturing the sequence of messages exchanged between participants. Chat logs are essential for auditing, troubleshooting, and understanding the context of a conversation.

#### Document Chunk

A segment of a document that has been separated from others based on structure, topic, or other relevant criteria. Chunks are used to simplify processing and enhance the analysis of large documents by focusing on manageable sections.

#### Document Chunker

A tool or process that divides documents into smaller, more manageable pieces or chunks based on predefined rules or algorithms. This facilitates more detailed and efficient analysis of the content by treating each chunk as a separate unit for processing.

#### ConceptRelationship

A general term for any type of directed or undirected edge in a graph that represents a relationship between two concept vertices. These relationships are used to illustrate the semantic connections between different concepts.

#### Concept Vertex Type

A type of vertex in a graph that represents a general idea or category derived from the content of documents. Concept vertices are used to categorize and connect related entities and documents based on shared themes or topics.

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

#### History Notes

Notes that provide historical context or track changes and developments related to a concept or entity in the graph over time.

#### InqueryAI

The TigerGraph tools and frameworks that match questions to certified queries.

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

#### Scope Notes

Notes that clarify the boundaries and context of a concept or entity within the graph, including what is covered and what is excluded from the concept or entity definition.

## TigerGraph CoPilot

The collective name for the generative AI tools used by TigerGraph to create conversational AI experiences and
enable intelligent agents.

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