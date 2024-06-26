import os
import pandas as pd
import seaborn as sns
from dotenv import load_dotenv

# load the .env file variables
load_dotenv()

import os

client_id = os.environ.get("CLIENT_ID")
client_secret = os.environ.get("CLIENT_SECRET")
client_id = '97fa00076425479db1ae710bc62e2a74'
client_secret = '97fa00076425479db1ae710bc62e2a74'

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pprint


client_id = '97fa00076425479db1ae710bc62e2a74'
client_secret = '4f21edfb889e4e50a7005ef44ca46566'



# Configurando el gestor de autenticación con las credenciales del cliente
auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
spotify = spotipy.Spotify(auth_manager=auth_manager)

# ID del artista de Spotify, por ejemplo, "The Beatles"
artist_id = '6c4WWQ2PYJlgnxtkQKqI5s'  # Este es el ID de Spotify para 'Haze'

# Obtener el top tracks de Haze
top_tracks = spotify.artist_top_tracks(artist_id)

# Filtrar la información deseada: nombre de la canción, popularidad y duración
print("Top 10 canciones:")
for track in top_tracks['tracks'][:10]:  # Limitando a las primeras 10 canciones
    duration_min = track['duration_ms'] / 60000  # Convertir milisegundos a minutos
    print(f"{track['name']} - Popularidad: {track['popularity']} - Duración: {duration_min:.2f} minutos")

# Crear un DataFrame
tracks_data = []
for track in top_tracks['tracks'][:10]:  # Limitando a las primeras 10 canciones
    duration_min = track['duration_ms'] / 60000  # Convertir milisegundos a minutos
    tracks_data.append({
        'Nombre de la Canción': track['name'],
        'Popularidad': track['popularity'],
        'Duración (minutos)': round(duration_min, 2)})

df = pd.DataFrame(tracks_data)
print(df.head(3))

# Ordenar las canciones por popularidad creciente:

df_sorted = df.sort_values(by='Popularidad', ascending=True)

# Mostrar el top 3 resultante de Haze:

print("Top 3 canciones por popularidad creciente:")
print(df_sorted.head(3))

import matplotlib.pyplot as plt

# Graficar el scatter plot y guardar como imagen
plt.figure(figsize=(10, 6))
plt.scatter(df['Duración (minutos)'], df['Popularidad'], color='blue', alpha=0.7)
plt.title('Relación entre Duración y Popularidad de Canciones')
plt.xlabel('Duración (minutos)')
plt.ylabel('Popularidad')
plt.grid(True)
# Guardar la imagen como scatter_plot.png
plt.savefig('scatter_plot.png')  
plt.close()