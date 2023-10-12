import logo from './logo.svg';
import './App.css';
import React, { Component , useState, useEffect } from 'react';

class MyForm extends Component {
  constructor(props) {
    super(props);
    this.state = {
      yt_url: '',
      format: '',
    };
  }

  // Event handler for form input changes
  handleInputChange = (event) => {
    const { name, value } = event.target;
    this.setState({ [name]: value });
  };

  // Event handler for the "Save" button
  clickDownloadAudio = (event) => {
    event.preventDefault();
    // Perform save or submit action
    console.log('click:', this.state);
    // You can add your save logic here
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
      <div className="App">
        <img src={logo} className="App-logo" alt="logo" />

        {/* <h2>Lite YouTube Downloader</h2> */}
        <br/>
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
          <button type="button" onClick={this.clickDownloadVideo}>Download Video</button>
        </form>

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
