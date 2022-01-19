import "./App.css";
import { MapContainer, TileLayer, Marker, Popup } from "react-leaflet";
import { useEffect, useState } from "react";
import axios from "axios";

const center = [51.505, -0.09];

interface Athlete {
  first_name: string;
  last_name: string;
  hometown: string;
  hometown_latitude: number;
  hometown_longitude: number;
}

function App() {
  const [athletes, setAthletes] = useState<Athlete[]>([]);

  useEffect(() => {
    const fetchAthletes = async () => {
      try {
        const url = "http://127.0.0.1:5000/api/athletes";
        const response = await axios.get(url);
        console.log(response.data);
        setAthletes([]);
      } catch (error) {
        console.log(error);
      }
    };
    fetchAthletes();
  });
  return (
    <MapContainer center={[38.627, -90.1994]} zoom={5} scrollWheelZoom={false}>
      <TileLayer
        attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
        url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
      />
      <Marker position={[38.627, -90.1994]}>
        <Popup>
          A pretty CSS3 popup. <br /> Easily customizable.
        </Popup>
      </Marker>
    </MapContainer>
  );
}

export default App;
