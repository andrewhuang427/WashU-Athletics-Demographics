import axios from "axios";
import { useEffect, useState } from "react";
import { MapContainer, Marker, Popup, TileLayer } from "react-leaflet";
import "../App.css";
import ConditionalButton from "./shared/ConditionalButton";

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

function DemographicMap() {
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
      <div className="w-full flex flex-row">
        <div className="w-1/3 p-5 ">
          <div>
            <h1 className="text-lg font-medium">
              WashU Student-Athlete Demographics
            </h1>
          </div>
          <br />
          <div className="mb-5">
            <span>{"Total Athletes: " + athletes.length}</span>
          </div>
          <div className="mb-5">
            <div className="mb-2">
              <h1 className="mb-2">Select Years: </h1>
            </div>
            {[...Array(9)].map((e, i) => {
              i += 3;
              const y = "20" + (10 + i) + "-" + (i + 11);
              return (
                <ConditionalButton
                  key={y}
                  text={y}
                  isTrue={selectedYears.has(y)}
                  func={() => {
                    toggleYears(y);
                  }}
                />
              );
            })}
          </div>
          <div className="mb-5">
            <div className="mb-2">
              <h1 className="font-medium">Select Teams: </h1>
            </div>
            {teams.map((t, index) => {
              return (
                <>
                  <ConditionalButton
                    key={index}
                    text={t}
                    isTrue={selectedTeams.has(t)}
                    func={() => {
                      toggleTeams(t);
                    }}
                  />
                </>
              );
            })}
          </div>
        </div>
        <div className="w-full h-full flex-grow">
          <MapContainer
            center={[38.627, -95.1994]}
            zoom={5}
            scrollWheelZoom={false}
          >
            <TileLayer url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png" />
            {athletes.map((athlete, index) => {
              return (
                <Marker
                  key={index}
                  position={[
                    athlete.hometown_latitude,
                    athlete.hometown_longitude,
                  ]}
                >
                  <Popup>
                    <div className="mb-2">
                      <h3 className="font-medium">
                        {athlete.first_name + " " + athlete.last_name}
                      </h3>
                      <div className="mb-2">{athlete.sport}</div>
                    </div>
                    <div className="mb-3">{athlete.highschool + " | " + athlete.hometown}</div>
                    
                    <div className="flex flex-row justify-end">
                      <a href={athlete.link} target="_blank">
                        Player Profile
                      </a>
                    </div>
                  </Popup>
                </Marker>
              );
            })}
          </MapContainer>
        </div>
      </div>
    </>
  );
}

export default DemographicMap;
