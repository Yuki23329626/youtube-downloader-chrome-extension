import logo from './logo.svg';
import './App.css';
import React, { Component, useState, useEffect } from 'react';
import MyForm from './MyForm';
import axios from 'axios'; // Import Axios if you're using it

function App() {

  // const [data, setData] = useState(null);

  // axios.get(apiUrl, { responseType: 'blob' })
  //   .then(response => {
  //     // Extract the filename from the response headers
  //     const filename = response.headers['content-disposition']
  //       .split(';')
  //       .find(param => param.trim().startsWith('filename='))
  //       .split('=')[1];

  //     // Create a Blob from the response data
  //     const blob = new Blob([response.data]);

  //     // Create an object URL for the Blob
  //     const url = window.URL.createObjectURL(blob);

  //     // Create a temporary anchor element to trigger the download
  //     const a = document.createElement('a');
  //     a.href = url;
  //     a.download = filename; // Set the filename

  //     // Trigger a click event on the anchor to initiate the download
  //     a.click();

  //     // Revoke the object URL to free up resources
  //     window.URL.revokeObjectURL(url);
  //   })
  //   .catch(error => {
  //     console.error('Error:', error);
  //   });

  return (
    <div className="App">
      <img src={logo} className="App-logo" alt="logo" />
      <br />

      <div style={{maxHeight: '100%'}}>
        <MyForm></MyForm>
      </div>

      <footer id="footer">
        <div class="contact_informations">
        </div>
        <div class="copyright">
          &copy; 2023 LiteYTD All right reserved
        </div>
      </footer>

    </div>
  );
}
export default App;
