import React, { useEffect, useState } from 'react';
import axios from 'axios';
import './styles/Landing.css';
import MapBox from './MapBox.js'
import { MapContainer, TileLayer, Polyline } from 'react-leaflet';
import 'leaflet/dist/leaflet.css';
import L from 'leaflet';


function Landing() {
  const [route, setRoute] = useState(null); // [route, setRoute]
  const [start, setStart] = useState("");
  const [end, setEnd] = useState("");
  const [percentage, setPercentage] = useState(1);
  const [max, setMax] = useState(true);

  // useEffect(() => {
  //   if(route) {
  //     console.log(route);

  const requestData = {
      "start": start,
      "end": end,
      "percentage": percentage,
      "max": max
  };
    

  const config = {
  headers: {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods':'GET,PUT,POST,DELETE,PATCH,OPTIONS',  
    },
  };

  const getRoute = async () => {
  try {
    const res = await axios.post('http://127.0.0.1:5000/get_route', requestData, config);
    setRoute(res.data);
    console.log(res);
  } catch (error) {
    console.error('Error:', error);
  }
};


  const handleStart = (event) => {
    setStart(event.target.value);
    console.log(start)
  };

  const handleEnd = (event) => {
    setEnd(event.target.value);
    console.log(end)
  };

  const handlePercentage = (event) => {
    setPercentage(event.target.value);
    console.log(percentage)
  };

  const handleMax = () => {
    setMax(!max);
    console.log(max)
  };

  

  return (
    <div className='landing-container'>
      <div className='options-box'>
        <h1 className='title'>EleNa</h1>
        <h1>Start Location</h1>
        <form>
          <input type="text" id="start" start="start" placeholder="Enter your start location" value={start} onChange={handleStart} required></input>
        </form>
        <h1>End Location</h1>
        <form>
          <input type="text" id="end" start="end" placeholder="Enter your end location" value={end} onChange={handleEnd} required></input>
        </form>
        <div>
          <p>Selected Percentage: {percentage * 100}%</p>
          <input
            type="range"
            step={.01}
            min="1"
            max="2"
            value={percentage}
            onChange={handlePercentage}
          />
        </div>
        <div>
          <button onClick={handleMax}>{max ? 'MIN' : 'MAX'}</button>
          <p>Toggle state: {max ? 'MIN' : 'MAX'}</p>
        </div>
        <button onClick={getRoute}>Submit</button>
      </div>
      <div className='map-box'>
        <MapContainer
        center={[42.374821, -72.518915]}
        zoom={13}
        style={{ width: '100%', height: '100%' }}
        >
        <TileLayer
            url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
            attribution="Map data © OpenStreetMap contributors"
        />
        {route && (
            <Polyline
              positions={route}
              color="red"
              weight={3}
            />
          )}
        </MapContainer>
      </div>
    </div>
  );
}

export default Landing;
