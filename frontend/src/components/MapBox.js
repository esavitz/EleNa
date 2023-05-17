import React from 'react';
import { MapContainer, TileLayer, Polyline } from 'react-leaflet';
import 'leaflet/dist/leaflet.css';
import L from 'leaflet';
import "./styles/MapBox.css"

function MapBox({ route }) {

  const getRouteCoordinates = async () => {
    const query = `[out:json];(
      node(${route.join(',')});
    );out;`;

    try {
      const response = await fetch(`https://overpass-api.de/api/interpreter?data=${encodeURIComponent(query)}`);
      const data = await response.json();

      const coordinates = data.elements.map((element) => [element.lat, element.lon]);

      return coordinates;
    } catch (error) {
      console.error('Error fetching route coordinates:', error);
      return [];
    }
  };

  const renderRoute = async () => {
    // const coordinates = await getRouteCoordinates();

    // if (coordinates.length > 0) {
    //   const map = L.map('map').setView(coordinates[0], 12);

    //   L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    //     attribution: 'Map data © <a href="https://openstreetmap.org">OpenStreetMap</a> contributors',
    //     maxZoom: 18,
    //   }).addTo(map);

    //   L.polyline(coordinates, { color: 'blue' }).addTo(map);
    // }
  };

  React.useEffect(() => {
    renderRoute();
  }, []);

  return (
    <div className='map-container'>
        <MapContainer
        center={[42.3732, 72.5199]}
        zoom={13}
        style={{ width: '100%', height: '100%' }}
        >
        <TileLayer
            url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
            attribution="Map data © OpenStreetMap contributors"
        />
        </MapContainer>
    </div>
  );
}

export default MapBox;