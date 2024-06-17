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

## Requirements

- Python 3.7+
- Flask
- Flask-CORS
- LangChain and its dependencies
- BeautifulSoup4
- GROQ API key
- huggingface embeddings

## Installation

1. **Clone the repository:**

```bash
git clone https://github.com/yourusername/ChatBot.git
cd ChatBot
