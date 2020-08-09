import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pprint
import pandas as pd

#DON'T TOUCH HERE ~Clienet information~
client_id = 'fbffcba3d6e14d73b8283e7dcfa59676'
client_secret = '185a1eed76594a3cadc161a709a790d1'
client_credentials_manager = SpotifyClientCredentials(client_id, client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
#End here

'''
id_list=[] #list for id of each songs
sp_name_list=[]
sp_artist_list=[]
sp_url_list=[]
'''

df=pd.read_csv("ranking2015.csv") #read the ranking.csv
n = len(df.index)

df_gen = pd.DataFrame(columns=['sp_name', 'sp_artist', 'sp_url', 'year', 'acousticness', 'analysis_url', 'danceability', 'duration_ms', 'energy', 'id', 'instrumentalness',
'key', 'liveness', 'loudness', 'mode', 'speechiness', 'tempo', 'time_signature', 'track_href', 'type', 'uri', 'valence'])

c = 0

for i in range(n):
    song_name = df["song"][i]
    artist_name = df["artist"][i]
    year = df["year"][i]

    if "Featuring" in artist_name:
        artist_name = artist_name.split("Featuring")[0]
    elif "feat." in artist_name:
        artist_name = artist_name.split("feat.")[0]

    result = sp.search(q = "track:{0} artist:{1}".format(song_name,artist_name), limit=1, offset=0, type="track", market=None)

    #when there is the no result and also "&" in the artist_name
    if len(result["tracks"]["items"]) == 0:
        artist_name = artist_name.split("&")[0]
        result = sp.search(q = "track:{0} artist:{1}".format(song_name,artist_name), limit=1, offset=0, type="track", market=None)
        if len(result["tracks"]["items"]) == 0:
            artist_name = artist_name.replace(" ", "")
            result = sp.search(q = "track:{0} artist:{1}".format(song_name,artist_name), limit=1, offset=0, type="track", market=None)


    for track in result["tracks"]["items"]:

        sp_name=track["name"]
        sp_artist=track["artists"][0]["name"]
        sp_url=track["external_urls"]["spotify"] #Those "sp_..." are for checking if the each songs is correct or not.
        id=track["id"]
        '''
        id_list.append(id)
        sp_name_list.append(sp_name)
        sp_artist_list.append(sp_artist)
        sp_url_list.append(sp_url)
        '''

        features = sp.audio_features(id)


        if features[0] == "None" or features[0] == None:
            break
        print(sp_artist,sp_name)

        sp_acousticness=features[0]["acousticness"]
        sp_analysis_url=features[0]["analysis_url"]
        sp_danceability=features[0]["danceability"]
        sp_duration_ms=features[0]["duration_ms"]
        sp_energy=features[0]["energy"]
        sp_id=features[0]["id"]
        sp_instrumentalness=features[0]["instrumentalness"]
        sp_key=features[0]["key"]
        sp_liveness=features[0]["liveness"]
        sp_loudness=features[0]["loudness"]
        sp_mode=features[0]["mode"]
        sp_speechiness=features[0]["speechiness"]
        sp_tempo=features[0]["tempo"]
        sp_time_signature=features[0]["time_signature"]
        sp_track_href=features[0]["track_href"]
        sp_type=features[0]["type"]
        sp_uri=features[0]["uri"]
        sp_valence=features[0]["valence"]

        temp_list = pd.Series([sp_name, 
        sp_artist, sp_url, year, sp_acousticness, 
        sp_analysis_url, sp_danceability, sp_duration_ms,
        sp_energy, sp_id, sp_instrumentalness, sp_key,
        sp_liveness, sp_loudness, sp_mode, sp_speechiness,
        sp_tempo, sp_time_signature, sp_track_href,
        sp_type, sp_uri, sp_valence], index=df_gen.columns)
        '''
        df_temp = pd.DataFrame([[sp_name, 
        sp_artist, sp_url, sp_acousticness, 
        sp_analysis_url, sp_danceability, sp_duration_ms,
        sp_energy, sp_id, sp_instrumentalness, sp_key,
        sp_liveness, sp_loudness, sp_mode, sp_speechiness,
        sp_tempo, sp_time_signature, sp_track_href,
        sp_type, sp_uri, sp_valence]], columns=['sp_name', 'sp_artist', 'sp_url', 'acousticness', 'analysis_url', 'danceability', 'duration_ms', 'energy', 'id', 'instrumentalness',
        'key', 'liveness', 'loudness', 'mode', 'speechiness', 'tempo', 'time_signature', 'track_href', 'type', 'uri', 'valence'])
        '''

        df_gen = df_gen.append(temp_list, ignore_index=True)
        print(c)
        c = c+1


df_gen.to_csv("audio_features2015.csv")



'''
sp_acousticness=features[0]["acousticness"]
sp_analysis_url=features[0]["analysis_url"]
sp_danceability=features[0]["danceability"]
sp_duration_ms=features[0]["duration_ms"]
sp_energy=features[0]["energy"]
sp_id=features[0]["id"]
sp_instrumentalness=features[0]["instrumentalness"]
sp_key=features[0]["key"]
sp_liveness=features[0]["liveness"]
sp_loudness=features[0]["loudness"]
sp_mode=features[0]["mode"]
sp_speechiness=features[0]["speechiness"]
sp_tempo=features[0]["tempo"]
sp_time_signature=features[0]["time_signature"]
sp_track_href=features[0]["track_href"]
sp_type=features[0]["type"]
sp_uri=features[0]["uri"]
sp_valence=features[0]["valence"]
'''

'''
pprint.pprint(features[0]['acousticness'])
'''
'''
birdy_uri = 'spotify:artist:2WX2uTcsvV5OnS0inACecP'

results = sp.artist_albums(birdy_uri, album_type='album')
albums = results['items']
while results['next']:
    results = sp.next(results)
    albums.extend(results['items'])

for album in albums:
    print(album['name'])
'''

