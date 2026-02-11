import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './components/App'; // This assumes App.js is in src/components
import './components/styles.css';  // This assumes styles.css is in src/components

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(<App />);