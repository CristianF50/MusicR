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
    return semillas

class cancion:
    def __init__(self, id , name , artist , albumIMG , preview):
        self.id = id
        self.name = name
        self.artist = artist
        self.albumIMG = albumIMG
        self.preview = preview



def getRecomendaciones(semillas):
    results = sp.recommendations(seed_tracks=semillas, limit=1)
    reco = []
    for idx, item in enumerate(results['tracks']):
        id = item['id']
        name = item['name']
        artist = item['artists'][0]['name']
        albumIMG = item['album']['images'][0]['url']
        preview = item['preview_url']
        song = cancion(id,name,artist,albumIMG,preview)
        reco.append(song)
    return reco

def addToLibrary(trackID):
    id = []
    id.append(trackID)
    sp.current_user_saved_tracks_add(tracks=id)
    check = sp.current_user_saved_tracks(limit=1)
    new = check['items'][0]['track']['id']
    print(new)
    if trackID == new:
        return 'true'
    elif trackID != new:
        return 'false'

def musicr():
    semillas = getSemillas()
    recommendations = getRecomendaciones(semillas)

    for i in recommendations:
        print("La cancion que te recomendamos es: ", i.name, " by ", i.artist)
        op = input('Deseas que la agreguemos a tu libreria ? (S/N/E para salir)')

        if op == "S":
            addToLibrary(str(i.id))
            print("La cancion ha sido agregada")
        elif op == "N":
            print("La cancion ha sido descartada")
        elif op == "E":
            exit()
        return ("La cancion que te recomendamos es: ", i.name, " by ", i.artist)

if __name__ == '__main__':
    musicr()