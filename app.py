from dotenv import load_dotenv
from vectorDB import retriever
import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from langchain import hub
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.prompts import ChatPromptTemplate
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.chat_history import BaseChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain.chains import create_history_aware_retriever
from langchain_core.prompts import MessagesPlaceholder

# Load environment variables from .env file
load_dotenv()
print(os.getenv("GROQ_API_KEY"))

# Set environment variables
os.environ["USER_AGENT"] = os.getenv("USER_AGENT", "your_custom_user_agent")
os.environ["TOKENIZERS_PARALLELISM"] = "false"

# intialization of LLM models
from langchain_groq import ChatGroq

llm = ChatGroq(model="llama3-8b-8192")

# intialize a flask application
app = Flask(__name__)
CORS(app)

# 2. Incorporate the retriever into a question-answering chain.
system_prompt = (
    "You are an assistant for question-answering tasks. "
    "Use the following pieces of retrieved context to answer "
    "the question. If you don't know the answer, say that you "
    "don't know. Use three sentences maximum and keep the "
    "answer concise."
    "\n\n"
    "{context}"
)

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system_prompt),
        ("human", "{input}"),
    ]
)

question_answer_chain = create_stuff_documents_chain(llm, prompt)
rag_chain = create_retrieval_chain(retriever, question_answer_chain)

# response = rag_chain.invoke({"input": "What is Task Decomposition?"})
# print(response["answer"])
# Statefully manage chat history
# Contextualize question
contextualize_q_system_prompt = (
    "Given a chat history and the latest user question "
    "which might reference context in the chat history, "
    "formulate a standalone question which can be understood "
    "without the chat history. Do NOT answer the question, "
    "just reformulate it if needed and otherwise return it as is."
)
contextualize_q_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", contextualize_q_system_prompt),
        MessagesPlaceholder("chat_history"),
        ("human", "{input}"),
    ]
)
history_aware_retriever = create_history_aware_retriever(
    llm, retriever, contextualize_q_prompt
)

# Answer question
system_prompt = (
    "You are an assistant for question-answering tasks. "
    "Use the following pieces of retrieved context to answer "
    "the question. If you don't know the answer, say that you "
    "don't know. Use three sentences maximum and keep the "
    "answer concise."
    "\n\n"
    "{context}"
)
qa_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system_prompt),
        MessagesPlaceholder("chat_history"),
        ("human", "{input}"),
    ]
)
question_answer_chain = create_stuff_documents_chain(llm, qa_prompt)

rag_chain = create_retrieval_chain(history_aware_retriever, question_answer_chain)

# Statefully manage chat history
store = {}

def get_session_history(session_id: str) -> BaseChatMessageHistory:
    if session_id not in store:
        store[session_id] = ChatMessageHistory()
    return store[session_id]


conversational_rag_chain = RunnableWithMessageHistory(
    rag_chain,
    get_session_history,
    input_messages_key="input",
    history_messages_key="chat_history",
    output_messages_key="answer",
)

@app.route("/")
def index():
    return "<h1>Welcome to the Chatbot!</h1>"


@app.route("/chat", methods=["POST"])
def chat():
    print(request.headers)
    print(request.data)
    if request.is_json:
        data = request.get_json()
        session_id = data["session_id"]
        user_input = data["message"]
        chat_history = get_session_history(session_id)
        # conversational_rag_chain(
        #     {"input": user_input, "chat_history": chat_history.messages}
        # )
        response = conversational_rag_chain.invoke(
            {"input": user_input},
            config={
                "configurable": {"session_id": session_id}
            },  # constructs a key "abc123" in `store`.
        )

        return jsonify({"response": response['answer']})
    else:
        return jsonify({"error": "Unsupported Media Type"}), 415


@app.route("/reset", methods=["POST"])
def reset():
    session_id = request.get_json().get("session_id")
    store.pop(session_id, None)
    return jsonify({"message": "Session reset successfully"})


if __name__ == "__main__":
    app.run(debug=True)
