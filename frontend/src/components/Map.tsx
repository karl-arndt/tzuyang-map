import React from 'react';
import { MapContainer, TileLayer, Marker } from 'react-leaflet';
import 'leaflet/dist/leaflet.css';
import type { LatLngExpression } from 'leaflet';
import { tzuyangLocations } from '../data/locations';

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
                <Marker 
                    key={index} 
                    position={[location.lat, location.lng]}
                    eventHandlers = {{
                        click: () => {
                            console.log(`Marker for ${location.name} clicked`); 
                        }
                    }}
                />
            ))}
            </MapContainer>
        </div>
    );
};

export default Map;