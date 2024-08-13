# NLP_EX3
# Natural Language Processing – Assignment #3

## Project Overview

This project is a solution to Assignment #3 for a Natural Language Processing course. The assignment involves syntactic parsing and linguistic investigation, specifically focusing on the usage and omission of the word "that" as a subordinate conjunction in informal writing. 

## Task Description

### Task #1: Analysis of "That" as a Subordinate Conjunction

In English, "that" can serve as a connector between a main clause and a subordinate clause. This project explores the phenomenon of "that" omission in informal writing, using a dataset of sentences from Reddit. The goal is to identify and analyze two types of sentences:

1. **Explicit Sentences:** Sentences where "that" explicitly connects a main clause to a subordinate clause.
2. **Implicit Sentences:** Sentences where "that" could be used but is omitted, especially after a verb.

### Examples

- **Explicit Usage Examples:**
  - "When someone in the audience asked about it, he explained **that** it was his day job."
  - "Guess it took till now to realize **that** I don't value the org so much as I value the players."
  - "We don't know **that** he actually died though."

- **Implicit Usage Examples:**
  - "She hopes **[that]** surgery will help her mental health..."
  - "Guess **[that]** it took till now to realize that I don't value the org so much as I value the players."
  - "Doesn't seem like he knows **[that]** it's wrong."

Sentences where "that" serves other syntactic functions or does not follow a verb are not included in this analysis.

## Implementation

The implementation includes:

- **Function Definition:** The core function `identify_explicit_and_implicit_that_clauses(filename)` identifies and separates explicit and implicit uses of "that" from a given dataset.
- **Syntactic Parsing:** Utilized the [Self-Attentive Parser](https://github.com/nikitakit/self-attentive-parser) with the `benepar_en3` English model to parse sentences and identify relevant patterns.
- **Data Handling:** Processed a dataset of 10,000 sentences to achieve the goal of identifying approximately 1,000 explicit and 1,500 implicit sentences.

### Implementation Details

- **Verb Precedent:** Focused on cases where "that" is preceded by a single-word verb. Phrasal verbs and other complex structures were excluded.
- **Parser Usage:** Employed either spaCy’s integrated version of the parser or NLTK Tree objects based on convenience.
- **Performance Goal:** Achieved identification of explicit and implicit sentences within the runtime constraint of 10 minutes.
- **Exploration:** Used the `SelectKBest` function from a previous assignment to analyze distinguishing words and reflect on usage tendencies of "that."

## Files Included

- **`config.json`**: Configuration file for input and output file locations.
- **`main.py`**: Main script containing the function implementation and execution logic.

## Running the Code

1. **Setup:** Ensure that the required parser and dependencies are installed.
2. **Implementation:** The function `identify_explicit_and_implicit_that_clauses` should be implemented as described.
3. **Execution:** Run the code to process the dataset and generate results.

## Results

The project successfully identifies and categorizes explicit and implicit uses of "that" from the dataset. The results, including detailed analysis and reflections on the findings, are included in the final report.

For any questions or issues, please open an issue in this repository.

---

Feel free to explore the code and adapt it as needed for further analysis or different datasets.
