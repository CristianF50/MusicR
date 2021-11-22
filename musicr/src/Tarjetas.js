import React from 'react'
import {useState, useEffect} from 'react'
import SpotifyWebApi from "spotify-web-api-node";
import './Tarjetas.css'
import TinderCard from "react-tinder-card"

const spotifyApi = new SpotifyWebApi({
    clientId: "c176bd9d61984d3f8c4804b03245467a",
  })

export default function Tarjetas({accessToken}){
    const [recomendacion,setRecomendacion] = useState([])
    
    useEffect(() => {
        let arrSeeds = new Array();
    
    if (!accessToken) return
    spotifyApi.setAccessToken(accessToken)
    
    if (recomendacion.length <= 5) {
        spotifyApi.getMySavedTracks({limit: 5, offset: 1}).then(res => {
          res.body.items.map(track => {
              arrSeeds.push(track.track.artists[0].id)
              console.log(arrSeeds)
          })

          for(var i = 0; i < 5; i++){
            spotifyApi.getRecommendations({min_energy: 0.4, seed_artists: arrSeeds, min_popularity: 50}).then(function(data) {
              let recommendations = data.body;
              console.log(recommendations.tracks);
              setRecomendacion(...recomendacion, recommendations.tracks.map(tracks => {
                return {
                  albumURL: tracks.album.images[0].url,
                  llave: tracks.id,
                  trackName: tracks.name,
                  previewURL: tracks.preview_url
                }
              }))
            }, function(err) {
              console.log("Something went wrong!", err);
            });
          }
          

      });
      }
    },[recomendacion])


    return (
        <div> 
          <div className="cards_container">
          {recomendacion.map(cancion => (
            <TinderCard className="swipe" key={cancion.llave} preventSwipe={['up','down']}>
              <div style = {{ backgroundImage: `url(${cancion.albumURL})` }} className="card"> 
              </div>
              <h3 size="large">{cancion.trackName}</h3>

            </TinderCard>
          ))} 

          </div>
        </div>
    )

}