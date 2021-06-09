import './App.css';
import Map from './components/Map.jsx';
import ForecastData from "./components/ForecastData";
import Loading from "./components/Loading";
import React, {useEffect, useState} from "react";
import axios from "axios";

require('dotenv').config()

const mapURL = `https://maps.googleapis.com/maps/api/js?v=3.exp&key=${process.env.REACT_APP_MAPS_KEY}`;
function App() {
    const init_state_calification = [{
        sardinero_uno: "",
        sardinero_dos: "",
        matalenias: "",
        caniones: "",
        rosamunda: "",
        valdearenas: "",
        canallave: "",
        somo: "",
        langre: "",
        usgo: "",
        gerra: "",
        farolillo: "",
        brusco: "",
        santamarina: "",
        fortaleza: "",
        laredo: ""
    }]


    const [json_path, getJson] = useState({headers:[],swellDirection:[],swellHeight:[],swellPeriod:[],windSpeed:[],windDirection:[],waterTemperature:[],tide:[],calification:init_state_calification})
    const [dataloaded,setLoading] = useState(false)
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
                setLoading(true)
        })();
    }, [])
  return (
    <div className="App">
      <h1>TFG-Forecast</h1>
      {dataloaded ? (
      <ForecastData
          webjson = {json_path}
      />
      ):(<Loading/>)}
      <Map
          googleMapURL={mapURL}
          containerElement= {<div style={{height: '400px'}}/>}
          mapElement ={<div style={{height: '100%'}}/>}
          webjson = {json_path}
          loadingElement = {<Loading/>}
        />
        
      
   
    </div>
  );
}

export default App;
