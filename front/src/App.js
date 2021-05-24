import './App.css';
import Map from './components/Map.jsx';
import NavBar from  './components/NavBar.jsx';
import Container from './components/Container.jsx'

import credentials from "./credentials";
import ForecastData from "./components/ForecastData";
import React from "react";

const mapURL = `https://maps.googleapis.com/maps/api/js?v=3.exp&key=${credentials.mapsKey}`;
function App() {
  return (
    <div className="App">
      <h1>Aplicacion del TFG</h1>
      <ForecastData />
          <Map
              googleMapURL={mapURL}
              containerElement= {<div style={{height: '400px'}}/>}
              mapElement ={<div style={{height: '100%'}}/>}
              loadingElement ={<p>Cargando</p>}
          />
    </div>
  );
}

export default App;
