import './App.css';
import Map from './components/Map.jsx';
import ForecastData from "./components/ForecastData";
import React, {useEffect, useState} from "react";
import axios from "axios";

require('dotenv').config()

const mapURL = `https://maps.googleapis.com/maps/api/js?v=3.exp&key=${process.env.REACT_APP_MAPS_KEY}`;
function App() {
    const init_state_calification = [{
        sardinero_uno: 0,
        sardinero_dos: 0,
        matalenias: 0,
        caniones: 0,
        rosamunda: 0,
        valdearenas: 0,
        canallave: 0,
        somo: 0,
        langre: 0,
        usgo: 0,
        gerra: 0,
        farolillo: 0,
        brusco: 0,
        santamarina: 0,
        fortaleza: 0,
        laredo: 0
    }]


    const [json_path, getJson] = useState({headers:[],swellDirection:[],swellHeight:[],swellPeriod:[],windSpeed:[],windDirection:[],waterTemperature:[],tide:[],calification:init_state_calification})
    useEffect(() => {
        (async () => {
            await axios
                .get(`${process.env.REACT_APP_CLOUD_FUNCTION}`)
                .then(r => {
                    console.log(r)
                    getJson(r.data)
                })
                .catch(err => {
                    console.log(err)

                })
        })();
    }, [])
  return (
    <div className="App">
      <h1>GForecast</h1>
      <ForecastData
          webjson = {json_path}
      />
          <Map
              googleMapURL={mapURL}
              containerElement= {<div style={{height: '400px'}}/>}
              mapElement ={<div style={{height: '100%'}}/>}
              webjson = {json_path}
              loadingElement ={<p>Cargando</p>}
          />
    </div>
  );
}

export default App;
