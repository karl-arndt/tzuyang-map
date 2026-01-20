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
    lat: 37.51995190496975,
    lng: 127.02608583727064,
    address: '26 Nonhyeon-ro 151-gil, Gangnam District, Seoul, South Korea',
    videoUrl: 'https://www.youtube.com/watch?v=PcwjmL-aJxg',
    description: 'Tonkatsu'
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