import React from "react";
import "./App.css";
import useAuth from "./useAuth";
import { useState, useEffect } from "react";
import SpotifyWebApi from "spotify-web-api-node";
import TinderCard from "react-tinder-card";
import "./Tarjetas.css";
import ReactAudioPlayer from "react-audio-player";
import { useSnackbar } from "notistack";
import Tarjetas from "./Tarjetas";

const spotifyApi = new SpotifyWebApi({
  clientId: "c176bd9d61984d3f8c4804b03245467a",
});

const code = new URLSearchParams(window.location.search).get("code");

function Interfaz({ code }) {
  const accessToken = useAuth(code);
  const [recomendacion, setRecomendacion] = useState([]);
  

  useEffect(() => {
    let arrSeeds = new Array();
    if (!accessToken) return;
    spotifyApi.setAccessToken(accessToken);
    if (recomendacion.length <= 5) {
      spotifyApi.getMySavedTracks({ limit: 5, offset: 1 }).then((res) => {
        console.log(res.body.items);
        res.body.items.map((track) => {
          arrSeeds.push(track.track.artists[0].id);
        });
        spotifyApi
          .getRecommendations({
            min_energy: 0.4,
            limit: 20,
            seed_artists: arrSeeds,
            min_popularity: 50,
          })
          .then(
            function (data) {
              let recommendations = data.body;
              console.log(recommendations.tracks);
              setRecomendacion(
                ...recomendacion,
                recommendations.tracks.map((tracks) => {
                  return {
                    albumURL: tracks.album.images[0].url,
                    llave: tracks.id,
                    trackName: tracks.name,
                    previewURL: tracks.preview_url,
                  };
                })
              );
            },
            function (err) {
              console.log("Something went wrong!", err);
            }
          );
      });
    }
  }, [accessToken]);

  console.log(recomendacion);

  const { enqueueSnackbar, closeSnackbar } = useSnackbar();

  const onSwipe = (direction, cancionID, index) => {
    let arrSeeds = []
    console.log(index);
    let arrCancion = new Array(cancionID);
    spotifyApi.setAccessToken(accessToken);
    if (direction == "right") {
      enqueueSnackbar("Cancion Agregada a tus me gusta");
      spotifyApi.addToMySavedTracks(arrCancion).then(function (data) {
        console.log("Cancion Agregada");
      });
    }
    if (direction == "left") {
      enqueueSnackbar("Cancion descartada");
    }
    var audio = document.getElementById(cancionID.toString());
    audio.pause();
    console.log(arrCancion);

    if (index <= 5) {
      let reco = [recomendacion[index+1]]
      console.log("son menos de 5")
      spotifyApi.getMySavedTracks({ limit: 5, offset: 1 }).then((res) => {
        console.log("Semillas",res.body.items);
        res.body.items.map((track) => {
          arrSeeds.push(track.track.artists[0].id);
        });
        spotifyApi
          .getRecommendations({
            min_energy: 0.4,
            limit: 20,
            seed_artists: arrSeeds,
            min_popularity: 50,
          })
          .then(
            
            function (data) {
              let recommendations = data.body;
              console.log(reco)
              reco =
                recommendations.tracks.map((tracks) => {
                  return {
                    albumURL: tracks.album.images[0].url,
                    llave: tracks.id,
                    trackName: tracks.name,
                    previewURL: tracks.preview_url,
                  };
                }).concat(recomendacion[index-1])
                
              
              setRecomendacion(reco);
            },
            function (err) {
              console.log("Something went wrong!", err);
            }
          );
          console.log("Array de recomendaciones",recomendacion);
      });
    }
  }

  return (
    <div className="App">
      <div className="header">
        <h1>MusicR</h1>
      </div>

      <div>
        <div className="cards_container">
          {/* {recomendacion.map((cancion, index) => (
            <TinderCard
              className="swipe"
              onSwipe={(dir) => onSwipe(dir, cancion.llave, index)}
              key={cancion.llave}
              preventSwipe={["up", "down"]}
            >
              <div
                style={{ backgroundImage: `url(${cancion.albumURL})` }}
                className="card"
              >
                <h3 size="large">{cancion.trackName}</h3>
              </div>
              <div className="player">
                <ReactAudioPlayer
                  id={cancion.llave.toString()}
                  volume={0.2}
                  loop={true}
                  src={cancion.previewURL}
                  controls
                />
              </div>
            </TinderCard>
          ))} */}

          <Tarjetas recomendacion={recomendacion} onSwipe={onSwipe}/>
        </div>
      </div>
    </div>
  );
}

export default Interfaz;
