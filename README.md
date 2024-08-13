# NLP_EX3

# Natural Language Processing – Assignment #3

## Project Description

This assignment focuses on syntactic parsing and linguistic investigation, specifically examining the usage and omission of the word "that" as a subordinate conjunction in informal writing.

## Task Overview

### Task #1: Analysis of "That" as a Subordinate Conjunction

In English, the word "that" can function as a connector between a main clause and a subordinate clause. For example: 

- **Explicit Usage:** "The authors thought **[that]** they should continue working on the project." Here, "that" is used to connect the clauses and is optional.

- **Implicit Usage:** "She hopes **[that]** surgery will help her mental health." In this case, "that" is implied but not explicitly stated.

Your task is to investigate the phenomenon of "that" omission by analyzing sentences collected from Reddit. You need to:

1. **Identify Explicit Sentences:** Locate sentences where "that" explicitly connects a main clause to a subordinate clause.
2. **Identify Implicit Sentences:** Find sentences where "that" could be used but is omitted, following a verb.

### Examples

- **Explicit Usage Examples:**
  - "When someone in the audience asked about it, he explained **that** it was his day job."
  - "Guess it took till now to realize **that** I don't value the org so much as I value the players."
  - "We don't know **that** he actually died though."

- **Implicit Usage Examples:**
  - "She hopes **[that]** surgery will help her mental health..."
  - "Guess **[that]** it took till now to realize that I don't value the org so much as I value the players."
  - "Doesn't seem like he knows **[that]** it's wrong."

Sentences where "that" is not following a verb, or serves other syntactic functions, are out of scope for this task:

- "I hypothetically have never heard of **that** fallacy before."
- "The book **that** my sister recommended was excellent."

### Implementation

You are provided with two files:

- **`config.json`**: Contains input and output file locations.
- **`main.py`**: Contains code that should not be modified.

Your task is to implement the function:

```python
def identify_explicit_and_implicit_that_clauses(filename):
    ...
    return set(), set()
