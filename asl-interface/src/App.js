import React from 'react';
import Webcam from "react-webcam";
import './logoCenter.css';
import './camPlacement.css'
import logo from './assets/Logo.png';

function setBodyColor({color}) {
  document.documentElement.style.setProperty('--bodyColor', color)
}

function Logo() {
  return (
    <div className="container">
      <img src={logo} alt="Logo" className="centered-image" />
    </div>
  );
}

function Camera() {
  return (
    <div className="webcam-container">
      <p className="overlay-text">Camera</p>
      <Webcam 
        audio={false}
      />
    </div>
  );
}

export default function App() {
  setBodyColor({color: "#F5E6E8"})
  return (
    <div>
      <Logo/>
      <Camera/>
    </div>
  );
}
