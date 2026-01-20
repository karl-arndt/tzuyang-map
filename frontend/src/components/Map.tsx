import React from 'react';
import { MapContainer, TileLayer } from 'react-leaflet';
import 'leaflet/dist/leaflet.css';
import type { LatLngExpression } from 'leaflet';
import { tzuyangLocations } from '../data/locations';
import { Marker, Popup } from 'react-leaflet';

const seoul: LatLngExpression = [37.5665, 126.9780]; // Seoul coordinates

const Map: React.FC = () => {
    return (
        <div style ={{ height: '100vh', width: '100%'}}>
            <MapContainer
                center={seoul}
                zoom={12}
                style={{ height: '100%', width: '100%' }}
            >
            <TileLayer
                url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
                attribution='&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
            />
            {tzuyangLocations.map((location, index) => (
                <Marker key={index} position={[location.lat, location.lng]}>
                    <Popup>
                        <strong>{location.name}</strong>
                        <br />
                        {location.address}
                        <br />
                        {location.description}
                    </Popup>
                </Marker>
            ))}
            </MapContainer>
        </div>
    );
};

export default Map;