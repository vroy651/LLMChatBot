# LLMChatBot
# ChatBot Application

This repository contains a chatbot application that uses LangChain and a Retrieval-Augmented Generation (RAG) technique to interact with a knowledge database.
The application is built with Flask for the backend and a simple HTML/JavaScript frontend for the user interface.
I use the GROQ LLM model which is free or opensource by XAI company .
also use the opensource embedding model.

## Features

- Interactive chatbot interface
- Contextual question-answering using chat history
- Ability to reset chat sessions
- Uses LangChain for document retrieval and question answering
- Integration with web-based document loaders

## Architecture design
### Indexingpt
   - In this chatbot, I use rag techniques to talk with knowledge database ,where I used embedding technique to store the data in vector database .
     
### Retriver   
   - Then we put an query with also get converted into vector form and retrive the data from the vector database and then augment the prompt and pass this
   - augmented context and query to the LMM model.

### Generation
   - Then it generate the answer based on the context.
   - I also add history about the previous result so that it can generalize the things and connect the things in better way to answer the question and dont 
     hallucinate over query.

## Requirements

- Python 3.7+
- Flask
- Flask-CORS
- LangChain and its dependencies
- BeautifulSoup4
- GROQ API key
- huggingface embeddings

## Installation

# example of chating
  -User: explain decomposition in a simple language?
WARNING:langchain_core.tracers.core:Parent run b8dfd55b-2c6f-4e78-aae6-010fbf2dab3f not found for run 1611523a-55b2-4da9-b578-e806b8d42260. Treating as a root run.
User: What is Task Decomposition?

AI: Task decomposition is the process of breaking down a complex task into smaller, simpler steps.

User: What are common ways of doing it?

AI: I don't know

User: how this technique help us?

AI: Chain of Thought (CoT) is a standard prompting technique that enhances model performance on complex tasks by instructing the model to "think step by step", decomposing hard tasks into smaller and simpler steps.

User: what is chain of thought?

AI: Chain of Thought (CoT) is a prompting technique that guides the model to generate a step-by-step explanation of its thought process, resulting in more accurate and interpretable outputs.

User: explain decomposition in a simple language?

AI: Decomposition is like breaking down a big puzzle into smaller, easier-to-solve puzzles.

User: ok fine . but how to proceed with it?
WARNING:langchain_core.tracers.core:Parent run a1f3e784-01fc-454b-a20b-ea2dc08745dd not found for run 4b221f6a-493f-445f-b54d-f1fd407c81af. Treating as a root run.
User: What is Task Decomposition?

AI: Task decomposition is the process of breaking down a complex task into smaller, simpler steps.

User: What are common ways of doing it?

AI: I don't know

User: how this technique help us?

AI: Chain of Thought (CoT) is a standard prompting technique that enhances model performance on complex tasks by instructing the model to "think step by step", decomposing hard tasks into smaller and simpler steps.

User: what is chain of thought?

AI: Chain of Thought (CoT) is a prompting technique that guides the model to generate a step-by-step explanation of its thought process, resulting in more accurate and interpretable outputs.

User: explain decomposition in a simple language?

AI: Decomposition is like breaking down a big puzzle into smaller, easier-to-solve puzzles.

User: ok fine . but how to proceed with it?

AI: I don't know

User: please try to find how to proceed with it so that i can start my work?
WARNING:langchain_core.tracers.core:Parent run aea7e402-5848-436b-b37a-265d93d65ea8 not found for run ca90dde7-8f0e-4b24-b6f0-34149fe4cb5a. Treating as a root run.
User: What is Task Decomposition?

AI: Task decomposition is the process of breaking down a complex task into smaller, simpler steps.

User: What are common ways of doing it?

AI: I don't know

User: how this technique help us?

AI: Chain of Thought (CoT) is a standard prompting technique that enhances model performance on complex tasks by instructing the model to "think step by step", decomposing hard tasks into smaller and simpler steps.

User: what is chain of thought?

AI: Chain of Thought (CoT) is a prompting technique that guides the model to generate a step-by-step explanation of its thought process, resulting in more accurate and interpretable outputs.

User: explain decomposition in a simple language?

AI: Decomposition is like breaking down a big puzzle into smaller, easier-to-solve puzzles.

User: ok fine . but how to proceed with it?

AI: I don't know

User: please try to find how to proceed with it so that i can start my work?

AI: According to the text, you can proceed with task decomposition by:

1. Using LLM with simple prompting like "Steps for XYZ.\n1." or "What are the subgoals for achieving XYZ?"
2. Using task-specific instructions, such as "Write a story outline." for writing a novel
3. With human inputs

User: exit

1. **Clone the repository:**

```bash
git clone https://github.com/yourusername/ChatBot.git
cd ChatBot
