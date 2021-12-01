import spotipy
from spotipy.oauth2 import SpotifyOAuth

scope= "streaming user-read-private user-library-read user-library-modify user-modify-playback-state user-read-recently-played"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id='c176bd9d61984d3f8c4804b03245467a', client_secret='dc5f5ff3398b421fa6716f1e5cdd443c', redirect_uri='http://example.com/redirect', scope=scope))

def getSemillas():
    results = sp.current_user_saved_tracks(limit=5, offset=2)
    semillas = []
    for idx, item in enumerate(results['items']):
        track = item['track']['id']
        semillas.append(track)
    print (semillas)

class cancion:
    id = ""
    name = ""
    albumIMG = ""
    preview = ""



def getRecomendaciones(semillas):
    results = sp.recommendations(seseed_tracks=semillas, limit=100)
    reco = []
    temp = cancion()
    for idx, item in enumerate(results['items']):
        track = item['track']['id']
        semillas.append(track)
    print (semillas)

    



# results = sp.current_user_recently_played()

#print(results['items'][0]['track'])

# for idx, item in enumerate(results['items']):
#     track = item['track']
#     print(idx, track['artists'][0]['name'], " – ", track['name'])

if __name__ == '__main__':
    getSemillas()