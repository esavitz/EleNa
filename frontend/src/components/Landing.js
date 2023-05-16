import React, { useState } from 'react';
import axios from 'axios';
import './styles/Landing.css';

function Landing() {
  const [route, setRoute] = useState(null); // [route, setRoute]
  const [start, setStart] = useState("");
  const [end, setEnd] = useState("");
  const [percentage, setPercentage] = useState(1);
  const [max, setMax] = useState(true);

  const getRoute = async () => {
    const res = await axios.get('http://localhost:5000/get_route');
    setRoute(res.data);
    console.log(res);
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
    <div>
      <div className='welcome-box'>
        <h1>Welcome to EleNa</h1>
        <button onClick={getRoute}>Get Started</button>
        <p>{route}</p>
      </div>
      <div className='left-box'>
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
      </div>
    </div>
  );
}

export default Landing;
