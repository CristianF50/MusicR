import SpotifyWebApi from "spotify-web-api-node";
import {useState, useEffect} from 'react'

const spotifyApi = new SpotifyWebApi({
    clientId: "c176bd9d61984d3f8c4804b03245467a",
  })

export default function useRecomendations(arrSeeds,accessToken) {
    const [recomendacion,setRecomendacion] = useState([])
    spotifyApi.setAccessToken(accessToken)
    spotifyApi.getRecommendations({min_energy: 0.4, seed_artists: arrSeeds, min_popularity: 50}).then(function(data) {
        let recommendations = data.body;
        console.log(recommendations.tracks);
        setRecomendacion(recommendations.tracks.map(tracks => {
          return {
            albumURL:tracks.album.images[0].url
          }
    
        }))
      }, function(err) {
        console.log("Something went wrong!", err);
      });

    return recomendacion

}