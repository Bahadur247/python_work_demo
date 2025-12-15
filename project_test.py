# import the libraries and real the data.
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv(r"C:\Users\vecto\OneDrive\Documents\Office_work\Popular_Spotify_Songs (1).csv", encoding='latin1')
df.to_excel('dataset006.xlsx', index=True)
file = pd.read_excel("dataset006.xlsx")

# clean the data
print(df.isnull().sum())
file.fillna({"in_shazam_charts": "NA"}, inplace=True)
file.fillna({"key": "NA"}, inplace=True)
file.to_excel("dataset008.xlsx")

# making pie chart of highest number of song producing artist.
artist_count = file['artist(s)_name'].value_counts().head(100)
plt.bar(artist_count.index, artist_count.values, color="Orange")
plt.title("number of songs by various artists")
plt.xlabel("Artists")
plt.ylabel("number of songs")
plt.xticks(rotation=90, fontsize=4)
plt.tight_layout()      # was not looking good.
plt.savefig('Top_100_singers_on_spotify.svg')
plt.show()

# making a pie chart of the major or minor songs by artists.
artist_count = file['mode'].value_counts()
plt.pie(artist_count, labels=artist_count.index, autopct='%1.1f%%')
plt.title('major or minor songs comparision')
plt.show()

# filtering only particular singer
indian_artist = file[(file['artist(s)_name'] == 'Stromae') & (file['mode'] == 'Major')]
print(indian_artist)
US_artist = file[(file['artist(s)_name']=='Taylor Swift')]
print(US_artist)
Taylor_Swift = pd.DataFrame(US_artist)
Taylor_Swift.to_excel('Taylor_Swift_songs.xlsx')
Taylor_file = pd.read_excel('Taylor_Swift_songs.xlsx')

Taylor_Swift = Taylor_file['mode'].value_counts()
plt.bar(Taylor_Swift.index, Taylor_Swift.values, color='Green')
plt.xlabel('Mode')
plt.ylabel('number of songs')
plt.savefig('Major_Minor_Songs_by_Taylor_Swift.svg')
plt.show()
year_of_release = Taylor_file['released_year'].value_counts()
plt.hist(year_of_release.index, bins=8, color='aqua', edgecolor='black')
plt.xlabel('year')
plt.ylabel('number of songs')
plt.savefig('Tylor_song_years.svg')
plt.show()