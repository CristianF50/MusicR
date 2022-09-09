import React from 'react'
import {useState, useEffect} from 'react'
import SpotifyWebApi from "spotify-web-api-node";
import './Tarjetas.css'
import TinderCard from "react-tinder-card"
import ReactAudioPlayer from "react-audio-player";

const spotifyApi = new SpotifyWebApi({
    clientId: "c176bd9d61984d3f8c4804b03245467a",
  })

export default function Tarjetas(props){

    const recomendacion = props.recomendacion

    console.log(recomendacion)

    const tarjetas  = recomendacion.map((cancion, index) => (
      <TinderCard
        className="swipe"
        onSwipe={(dir) => props.onSwipe(dir, cancion.llave, index)}
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
    ))

    return (
        <div> 
          <div className="cards_container">
            {tarjetas}
          </div>
        </div>
    )

}