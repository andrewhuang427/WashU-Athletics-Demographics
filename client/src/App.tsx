import { MapContainer, TileLayer, Marker, Popup } from "react-leaflet";
import { useEffect, useState } from "react";
import axios from "axios";
import "./App.css";

interface Athlete {
  sport: string;
  year: string;
  grade: string;
  first_name: string;
  last_name: string;
  highschool: string;
  hometown: string;
  hometown_latitude: number;
  hometown_longitude: number;
  link: string;
}

const teams = [
  "Baseball",
  "Men's Basketball",
  "Men's Football",
  "Men's Soccer",
  "Men's Tennis",
  "Women's Basketball",
  "Women's Golf",
  "Women's Soccer",
  "Softball",
  "Women's Tennis",
  "Women's Volleyball",
  "Track and Field",
  "Swimming and Diving",
  "Cross Country",
];

function App() {
  const [allAthletes, setAllAthletes] = useState([]);
  const [athletes, setAthletes] = useState<Athlete[]>([]);
  const [selectedYears, setSelectedYears] = useState<Set<string>>(new Set());
  const [selectedTeams, setSelectedTeams] = useState<Set<string>>(new Set());

  const toggleYears = (y: string) => {
    const newSet = new Set(selectedYears);
    if (selectedYears.has(y)) {
      newSet.delete(y);
      setSelectedYears(newSet);
      return;
    }
    newSet.add(y);
    setSelectedYears(newSet);
  };
  const toggleTeams = (t: string) => {
    const newSet = new Set(selectedTeams);
    if (selectedTeams.has(t)) {
      newSet.delete(t);
      setSelectedTeams(newSet);
      return;
    }
    newSet.add(t);
    setSelectedTeams(newSet);
  };

  useEffect(() => {
    const fetchAthletes = async () => {
      const response = await axios.get("/api/athletes");
      const data = response.data;
      setAllAthletes(data);
    };
    fetchAthletes();
  }, []);

  useEffect(() => {
    const filtered = allAthletes.filter(
      (d: any) => selectedYears.has(d.year) && selectedTeams.has(d.sport)
    );
    setAthletes(filtered);
  }, [allAthletes, selectedYears, selectedTeams]);

  return (
    <>
      <div
        style={{
          position: "absolute",
          zIndex: "99999",
          top: 10,
          right: 10,
          background: "white",
          padding: 20,
          borderRadius: 10,
          boxShadow: "5px 5px 5px 5px #888888",
        }}
      >
        <div style={{ marginBottom: 10 }}>
          <span>{"Total Athletes: " + athletes.length}</span>
        </div>
        <div style={{ marginBottom: 10 }}>
          {[...Array(9)].map((e, i) => {
            i += 3;
            return (
              <button
                style={{
                  cursor: "pointer",
                  marginRight: 10,
                  color: selectedYears.has("20" + (10 + i) + "-" + (i + 11))
                    ? "blue"
                    : "",
                  border: selectedYears.has("20" + (10 + i) + "-" + (i + 11))
                    ? "3px solid blue"
                    : "",
                  borderRadius: 5,
                }}
                key={i}
                onClick={() => {
                  toggleYears("20" + (10 + i) + "-" + (i + 11));
                }}
              >
                {"20" + (10 + i) + "-" + (i + 11)}
              </button>
            );
          })}
        </div>
        <div>
          {teams.map((t, index) => {
            return (
              <button
                style={{
                  cursor: "pointer",
                  marginRight: 10,
                  color: selectedTeams.has(t) ? "blue" : "",
                  border: selectedTeams.has(t) ? "3px solid blue" : "",
                  borderRadius: 5,
                }}
                key={t + index}
                onClick={() => {
                  toggleTeams(t);
                }}
              >
                {t}
              </button>
            );
          })}
        </div>
      </div>
      <MapContainer
        style={{ height: "100% !important", width: "100% !important" }}
        center={[38.627, -95.1994]}
        zoom={5}
        scrollWheelZoom={false}
      >
        <TileLayer
          attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
          url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
        />
        {athletes.map((athlete, index) => {
          return (
            <Marker
              key={index}
              position={[athlete.hometown_latitude, athlete.hometown_longitude]}
            >
              <Popup>
                <div>
                  {athlete.first_name +
                    " " +
                    athlete.last_name +
                    " | " +
                    athlete.grade}
                </div>
                <div>{athlete.highschool}</div>
                <div>{athlete.sport}</div>
                <div>{athlete.hometown}</div>
                <div>
                  <a href={athlete.link} target="_blank">
                    Link
                  </a>
                </div>
              </Popup>
            </Marker>
          );
        })}
      </MapContainer>
    </>
  );
}

export default App;
