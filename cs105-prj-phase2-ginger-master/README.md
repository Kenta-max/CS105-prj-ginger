# cs105-prj-phase2-ginger

Ginger_proj_phase2.ipynb -> The main files to analysis the billboard top100 songs' audio features from 1956-2019.

*Other files are used just for adding missing data in main dataset, so we do not use them.

## The dataset 

I used the "audio_features_new.csv" which has the audio features of all the top100 songs from 1956-2019. However, there are some missing data in certain years, such as 2015, 1959, so I concatenate those datasets("audio_features1959.csv", "audio_features2105.csv""). 

## The documentation

sp_name -> Song's name

sp_artist -> Artist's name

year -> year

acousticness -> how acoustic

danceability -> how suitable for dancing based on a combination of tempo,rythm stability,beat strength and overall regularity.

duration_ms -> the duration of the track in milliseconds.

energy -> Measure of intensity and activity. Energetic tracks feel fast,loud and noisy.

instrumentalness -> whether contains vocal or not. Rap or spoken word tracks are "vocal".

key -> The estimated overall key of the track. E.g. 0 = C, 1 = C♯/D♭, 2 = D, and so on. If no key was detected, the value is -1.

liveness -> Detect the presence of an audience in the recording. A value above 0.8 provides strong likelihood that the track is live.

loudness -> The overall loundness of a track in decibels(dB). Loudness is the quality of a sound that is the primary psychological correlate of physical strength (amplitude). Typically range from -60 to 0db.

mode -> Modality(major or minor) of a track. Major=1, Minor=0.

speechiness -> The presence of spoken words.The more speech-like tracks(e.g. talk show, audio book, poetry), the closer to 1.0. Values below 0.33 most likely represent music and other non-speech-like tracks.

tempo -> The tempo of a track in beats per minuite(BPM).

time_signature -> how many beats are in each bar.

valence -> The musical positiveness. High valence means more positive(happy,cheerful,euphoric), while low means more negative(sad,depressed,angry).

## Summary
I tried to get the how the each features are related, what kind of characteristics or trend the top100 songs have in each year. The below is the documentaion of what each feature means.

I plot the histgram, bar graph, box plot, scatter plot, calculate the correlation values and so on for seeing the skewed data and so on.

There are mainly 2 findings. Firstly, from the bargraph of mean of each features value in each year, I could find some trends or change as year goes on(such as acousticness decreaing year by year). 

Secondly, it seems that most of the energy and loudness have the positive correlation. That is reasonable because tjhe more energy the songs become, the louder the songs would be. Also, there can be seen the some positive correlation between the valence and the danceability. This is also understandable because more positive the songs be, the more danceable the songs would be. Unfortunatelly, there are not much findings from other elements. Duration_ms seems not so relevant to other elements such as loudness, energy, danceability and so on.
In total, I can see some postive correlation such as between energy and loudness, danceability, but these are something obvious because the louder the song is, the more energetic the songs would be. Also, the duration of the songs really does not relate to the songs' atmosphere(energy, danceability, valence...).

Other than that, there are no so many interesting findings from those data, though I plot several graphs. I tried to find other findings such by seeing "energy", "danceability" and so on in each "mode", but there is no interesting findings.

