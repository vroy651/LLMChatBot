// src/ChatBot.js
import React, { useState, useEffect } from "react";
import "bootstrap/dist/css/bootstrap.min.css";

const ChatBot = () => {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState("");
  const [sessionId, setSessionId] = useState("123");

  useEffect(() => {
    // Reset session on initial load
    fetch("http://127.0.0.1:5000/reset", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ session_id: sessionId }),
    });
  }, [sessionId]);

  const handleSendMessage = async () => {
    if (!input.trim()) return;

    setMessages([...messages, { text: input, sender: "user" }]);

    const response = await fetch("http://127.0.0.1:5000/chat", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ session_id: sessionId, message: input }),
    });

    const data = await response.json();
    setMessages([
      ...messages,
      { text: input, sender: "user" },
      { text: data.response, sender: "bot" },
    ]);
    setInput("");
  };

  return (
    <div className="container mt-5">
      <div className="card">
        <div className="card-header">ChatBot</div>
        <div className="card-body">
          <div
            className="chat-window"
            style={{ height: "300px", overflowY: "scroll" }}
          >
            {messages.map((msg, index) => (
              <div key={index} className={`message ${msg.sender}`}>
                <strong>{msg.sender === "user" ? "You" : "Bot"}: </strong>
                {msg.text}
              </div>
            ))}
          </div>
        </div>
        <div className="card-footer">
          <div className="input-group">
            <input
              type="text"
              className="form-control"
              value={input}
              onChange={(e) => setInput(e.target.value)}
              onKeyPress={(e) => e.key === "Enter" && handleSendMessage()}
            />
            <button className="btn btn-primary" onClick={handleSendMessage}>
              Send
            </button>
          </div>
        </div>
      </div>
    </div>
  );
};

export default ChatBot;
