// import logo from './logo.svg';
import './App.css';
import React, { Component, useState, useEffect } from 'react';
import axios from 'axios'; // Import Axios if you're using it

class MyForm extends Component {
  constructor(props) {
    super(props);
    this.state = {
      yt_url: '',
      full_request_url: '',
      // format: '',
      responseData: null,
    };
  }

  getFullReqeustUrl() {
    // Access the component's state or calculate the value
    return this.state.full_request_url; // Example: accessing a value from the state
  };

  // Event handler for form input changes
  handleInputChange = (event) => {
    const { name, value } = event.target;
    this.setState({ [name]: value });
  };

  // Event handler for the "Save" button
  clickDownloadAudio = async (event) => {
    event.preventDefault();
    // Perform save or submit action
    try {
      const yt_url = this.state.yt_url;
      // Create a URL object
      const src_url = new URL(yt_url);
      // Use URLSearchParams to access the parameters
      const params = new URLSearchParams(src_url.search);
      // Get specific parameter values
      const v = params.get("v");
      console.log('click:', this.state);
      // You can add your save logic here

      // Build the URL with parameters
      const apiUrl = `http://localhost:5000/api/file?v=${v}&format=bestaudio`; // Replace with your API endpoint and parameters
      this.setState({ full_request_url: apiUrl });

      axios.get(apiUrl, { responseType: 'blob' })
        .then(response => {
          // Extract the filename from the response headers
          const filename = response.headers['content-disposition']
            .split(';')
            .find(param => param.trim().startsWith('filename='))
            .split('=')[1];

          // Create a Blob from the response data
          const blob = new Blob([response.data]);

          // Create an object URL for the Blob
          const url = window.URL.createObjectURL(blob);

          // Create a temporary anchor element to trigger the download
          const a = document.createElement('a');
          a.href = url;
          a.download = filename; // Set the filename

          // Trigger a click event on the anchor to initiate the download
          a.click();

          // Revoke the object URL to free up resources
          window.URL.revokeObjectURL(url);
        })

    } catch (error) {
      console.error('Error downloading file:', error);
    }
  };

  // Event handler for the "Clear" button
  clickDownloadVideo = () => {
    // Clear the form fields
    console.log('click:', this.state);
  };

  componentDidMount() {
    // Access the clipboard and set the form fields with the clipboard data
    navigator.clipboard.readText().then((clipboardText) => {
      this.setState({ yt_url: clipboardText });
    }).catch((error) => {
      console.error('Error reading clipboard content:', error);
    });
  }

  render() {
    return (
      <form>
        <h2>YouTube URL:</h2>
        <label>
          <input
            type="text"
            name="yt_url"
            value={this.state.yt_url}
            onChange={this.handleInputChange}
          />
        </label>
        <br />
        <button onClick={this.clickDownloadAudio}>Download Audio</button>
        <button onClick={this.clickDownloadVideo}>Download Video</button>
      </form>
    );
  }
}


// function App() {
//   return (
//     <div className="App">
//       <header className="App-header">
//         <img src={logo} className="App-logo" alt="logo" />
//         <p>
//           Edit <code>src/App.js</code> and save to reload.
//         </p>

//         <a
//           className="App-link"
//           href="https://reactjs.org"
//           target="_blank"
//           rel="noopener noreferrer"
//         >
//           Learn React
//         </a>

//       </header>
//     </div>
//   );
// }

export default MyForm;

