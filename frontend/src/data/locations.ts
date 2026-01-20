export interface Location {
    name: string;
    lat: number;
    lng: number;
    address: string;
    imageUrl?: string;
    videoUrl?: string;
    description?: string;
}

export const tzuyangLocations: Location[] = [
  {
    name: 'Jeonju Food Festival',
    lat: 37.5665,
    lng: 126.9780,
    address: '123 Jeonju St, Jeonju, South Korea',
    description: 'Famous for grilled meats!'
  },
  {
    name: 'Street Food Stall',
    lat: 37.5700,
    lng: 126.9900,
    address: '456 Market Rd, Seoul, South Korea',
    description: 'Try the tteokbokki!'
  },
  {
    name: 'Ramen Restaurant',
    lat: 37.5650,
    lng: 126.9750,
    address: '789 Ramen Ave, Seoul, South Korea',
    description: 'Tzuyang’s favorite ramen!'
  }
];