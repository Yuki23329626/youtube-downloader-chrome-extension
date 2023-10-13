import logo from './logo.svg';
import './App.css';
import React, { Component, useState, useEffect } from 'react';
import MyForm from './MyForm';
import axios from 'axios'; // Import Axios if you're using it

function App() {

  return (
    <div className="App">
      <img src={logo} className="App-logo" alt="logo" />
      <br />
      <MyForm></MyForm>

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
