import './App.css';
import Map from './components/Map.jsx';
import credentials from "./credentials";

const mapURL = `https://maps.googleapis.com/maps/api/js?v=3.exp&key=${credentials.mapsKey}`;
function App() {
  return (
    <div className="App">
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
