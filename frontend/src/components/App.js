import React, { useState, useEffect, useRef } from 'react';
import './styles.css';

function App() {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState('');
  const [status, setStatus] = useState('Connecting to AI...'); 
  const socket = useRef(null);
  const messagesEndRef = useRef(null);

  // Magic Scroll: Automatically moves to the latest message
  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  };

  useEffect(() => {
    scrollToBottom();
  }, [messages, status]);

  useEffect(() => {
    // Connect to Django ASGI server
    socket.current = new WebSocket('ws://127.0.0.1:8000/ws/chat/');

    socket.current.onopen = () => {
      console.log("WebSocket Connected ✅");
      setStatus(null); 
    };

    socket.current.onmessage = (e) => {
      const data = JSON.parse(e.data);
      if (data.status === 'typing') {
        // Dynamic status based on which agent is thinking
        setStatus(`${data.agent} is checking records...`);
      } else {
        setStatus(null);
        setMessages(prev => [...prev, { 
          role: data.agent, 
          content: data.message,
          time: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })
        }]);
      }
    };

    socket.current.onerror = (err) => {
      console.error("WebSocket Error ❌", err);
      setStatus("Connection Error. Is the backend running?");
    };

    socket.current.onclose = () => {
      console.log("WebSocket Disconnected ⚠️");
    };

    return () => socket.current.close();
  }, []);

  const send = () => {
    if (!input.trim()) return;
    if (socket.current.readyState !== WebSocket.OPEN) {
      alert("Establishing connection... please wait.");
      return;
    }

    // Add user message to UI immediately
    setMessages(prev => [...prev, { 
      role: 'User', 
      content: input,
      time: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })
    }]);

    socket.current.send(JSON.stringify({ message: input }));
    setInput('');
  };

  return (
    <div className="chat-window">
      <div className="header">
        <h2>Swades AI Support</h2>
        <div className={`connection-dot ${status ? 'connecting' : 'online'}`}>
           {status ? status : '● Online'}
        </div>
      </div>

      <div className="messages">
        {messages.length === 0 && (
          <div className="welcome-msg">
            👋 Hi! Ask me about <b>ORD101</b> or <b>INV-5001</b>.
          </div>
        )}
        
        {messages.map((m, i) => (
          <div key={i} className={`msg ${m.role === 'User' ? 'user' : 'bot'}`}>
            <small>{m.role}</small>
            <p>{m.content}</p>
            <span className="timestamp">{m.time}</span>
          </div>
        ))}

        {/* This empty div is the anchor for auto-scroll */}
        <div ref={messagesEndRef} />
      </div>

      {status && status.includes('checking') && (
        <div className="typing-indicator">{status}</div>
      )}

      <div className="input-area">
        <input 
          value={input} 
          placeholder="Type your message..."
          onChange={e => setInput(e.target.value)} 
          onKeyPress={e => e.key === 'Enter' && send()} 
        />
        <button onClick={send}>
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
            <path d="M22 2L11 13M22 2l-7 20-4-9-9-4 20-7z" />
          </svg>
        </button>
      </div>
    </div>
  );
}

export default App;