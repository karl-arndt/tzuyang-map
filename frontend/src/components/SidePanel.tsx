import React from 'react';
import { tzuyangLocations } from '../data/locations';

let location = tzuyangLocations[0].name; // Example: using the first location for demonstration

function SidePanel() {
    return (
        <h2>{location}</h2>
    );
}

export default SidePanel;