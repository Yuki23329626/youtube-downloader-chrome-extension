// import logo from './logo.svg';
import './App.css';
import React, { Component } from 'react';
import axios from 'axios'; // Import Axios if you're using it

class MyForm extends Component {
  constructor(props) {
    super(props);
    this.state = {
      yt_url: '',
      // format: '',
      responseData: null,
    };
  }

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
      const param_yt_url = this.state.yt_url;
      console.log('click:', this.state);
      // You can add your save logic here

      // Build the URL with parameters
      const apiUrl = `http://localhost:5000/api/file?url=${param_yt_url}&format=bestaudio`; // Replace with your API endpoint and parameters

      // Send a GET request using Axios
      axios
        .get(apiUrl, {
          responseType: 'blob', // This tells Axios to expect binary data (e.g., a file)
        })
        .then((response) => {
          // Create a Blob object from the response data
          const blob = new Blob([response.data], { type: response.headers['content-type'] });

          // Create a temporary URL for the Blob
          const url = window.URL.createObjectURL(blob);

          // Create a link element to trigger the download
          const a = document.createElement('a');
          a.href = url;
          a.click();

          // Clean up by revoking the Blob URL
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

