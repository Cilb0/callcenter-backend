import React, { useState } from "react";

function App() {
  const [messages, setMessages] = useState([]);
  const [newMessage, setNewMessage] = useState("");

  const sendMessage = async () => {
    if (!newMessage.trim()) return;

    // Kullanıcının mesajını ekle
    const updatedMessages = [...messages, { sender: "Sen", text: newMessage }];
    setMessages(updatedMessages);
    setNewMessage("");

    try {
      const response = await fetch("http://127.0.0.1:8000/chat/", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ message: newMessage }),
      });

      const data = await response.json();
      const botReply = data.response || "Bot cevap veremedi.";
      setMessages([...updatedMessages, { sender: "Bot", text: botReply }]);
    } catch (error) {
      setMessages([
        ...updatedMessages,
        { sender: "Bot", text: "Hata oluştu: " + error.message },
      ]);
    }
  };

  return (
    <div style={{ maxWidth: "600px", margin: "20px auto", fontFamily: "Arial" }}>
      <h2>Müşteri Hizmetleri Botu</h2>
      <div
        style={{
          border: "1px solid #ccc",
          padding: "10px",
          height: "300px",
          overflowY: "auto",
          marginBottom: "10px",
        }}
      >
        {messages.map((msg, idx) => (
          <div key={idx}>
            <strong>{msg.sender}: </strong>
            {msg.text}
          </div>
        ))}
      </div>
      <input
        type="text"
        value={newMessage}
        onChange={(e) => setNewMessage(e.target.value)}
        style={{ width: "80%", padding: "5px" }}
      />
      <button onClick={sendMessage} style={{ padding: "5px 10px", marginLeft: "5px" }}>
        Gönder
      </button>
    </div>
  );
}

export default App;
