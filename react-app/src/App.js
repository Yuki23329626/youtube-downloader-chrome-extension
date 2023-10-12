import logo from './logo.svg';
import './App.css';
import React, { Component, useState, useEffect } from 'react';
import MyForm from './MyForm';

function App() {
  const [data, setData] = useState([]);
  const [loading, setLoading] = useState(true);
  
  useEffect(() => {
    // URL and parameters
    const apiUrl = 'https://api.example.com/data'; // Replace with your API endpoint
    const params = { url: '', format: '' };
    const url = new URL(apiUrl);

    // Add parameters to the URL
    Object.keys(params).forEach(key => url.searchParams.append(key, params[key]));

    // Send a GET request
    fetch(url)
      .then(response => response.json())
      .then(data => {
        setData(data);
        setLoading(false);
      })
      .catch(error => {
        console.error('Error:', error);
        setLoading(false);
      });
  }, []);

  if (loading) {
    return <p>Loading...</p>;
  }

  return (
    <div className="App">
      <MyForm /> {
        /* Use the imported component here */
      }
    </div>
  );
}
export default App;
