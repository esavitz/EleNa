import React, { useEffect, useState } from 'react';
import axios from 'axios';
import './styles/Landing.css';
import MapBox from './MapBox.js'
import { MapContainer, TileLayer, Polyline } from 'react-leaflet';
import 'leaflet/dist/leaflet.css';
import L from 'leaflet';
import { ClipLoader } from 'react-spinners';

function Landing() {
  const [route, setRoute] = useState(null);
  const [start, setStart] = useState("");
  const [end, setEnd] = useState("");
  const [percentage, setPercentage] = useState(1);
  const [max, setMax] = useState(true);
  const [loading, setLoading] = useState(false);
  const [request, setRequest] = useState(null);

  // Function to make API request and retrieve route
  const getRoute = async () => {
    setLoading(true);

    // Create a cancel token using axios
    const cancelToken = axios.CancelToken;
    const source = cancelToken.source();

    // Store the cancel token in the state
    setRequest(source);

    try {
      // Make the API call with the cancel token as an option
      const res = await axios.post(
        'http://localhost:5000/get_route',
        {
          start: start,
          end: end,
          percentage: percentage,
          max: max,
        },
        { cancelToken: source.token }
      );
      setRoute(res.data);
      setLoading(false);
      console.log(res);
    } catch (error) {
      // Handle the cancellation and other errors
      if (axios.isCancel(error)) {
        console.log('Request canceled:', error.message);
      } else {
        console.error(error);
      }
      setLoading(false);
    }
  };

  // Event handler for start location input
  const handleStart = (event) => {
    setStart(event.target.value);
    console.log(start);
  };

  // Event handler for end location input
  const handleEnd = (event) => {
    setEnd(event.target.value);
    console.log(end);
  };

  // Event handler for percentage range input
  const handlePercentage = (event) => {
    setPercentage(event.target.value);
    console.log(percentage);
  };

  // Event handler for toggling max state
  const handleMax = () => {
    setMax(!max);
    console.log(max);
  };

  // Event handler for cancel button
  const handleCancel = () => {
    if (request) {
      // Cancel the ongoing request and set loading to false
      request.cancel('Request canceled');
      setLoading(false);
    }
  };

  return (
    <div className='landing-container'>
      <div className='options-box'>
        <h1 className='title'>EleNa</h1>
        <h1>Start Location</h1>
        <form>
          <input
            type='text'
            id='start'
            start='start'
            placeholder='Enter your start location'
            value={start}
            onChange={handleStart}
            required
          ></input>
        </form>
        <h1>End Location</h1>
        <form>
          <input
            type='text'
            id='end'
            start='end'
            placeholder='Enter your end location'
            value={end}
            onChange={handleEnd}
            required
          ></input>
        </form>
        
          <p>Selected Percentage: {percentage * 100}%</p>
          <input
            type='range'
            step={0.01}
            min='1'
            max='2'
            value={percentage}
            onChange={handlePercentage}
          />
        
        
        <button onClick={handleMax}>{max ? 'MIN' : 'MAX'}</button>
        <p>Toggle state: {max ? 'MIN' : 'MAX'}</p>
        
        <button onClick={getRoute}>Submit</button>
        {loading && (
          <div className='spinner-container'>
            Loading...
            <ClipLoader type='TailSpin' color='#00BFFF' height={70} width={70} />
            <button onClick={handleCancel}>Cancel</button>
          </div>
        )}
      </div>
      <div className='map-box'>
        <MapContainer
          center={[42.374821, -72.518915]}
          zoom={13}
          style={{ width: '100%', height: '100%' }}
        >
          <TileLayer
            url='https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png'
            attribution='Map data © OpenStreetMap contributors'
          />
          {route && (
            <Polyline positions={route} color='red' weight={3} />
          )}
        </MapContainer>
      </div>
    </div>
  );
}

export default Landing;
