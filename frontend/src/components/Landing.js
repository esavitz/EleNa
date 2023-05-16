import React, { useState } from 'react';
import axios from 'axios';
import './styles/Landing.css';

function Landing() {
  const [route, setRoute] = useState(null); // [route, setRoute]
  const [startPosition, setStartPosition] = useState("");
  const [destination, setDestination] = useState("");
  const [multiplier, setMultiplier] = useState(.5);
  const [routeType, setRouteType] = useState(true);

  const getRoute = async () => {
    const res = await axios.get('http://localhost:5000/get_route');
    setRoute(res.data);
    console.log(res);
  };

  return (
    <div>
      <div className='welcome-box'>
        <h1>Welcome to EleNa</h1>
        <button onClick={getRoute}>Get Started</button>
        <p>{route}</p>
      </div>
      <div className='left-box'>
        
      </div>
    </div>
  );
}

export default Landing;
