#### Name: Kenta Kawajiri
#### ID: 862189492

# cs105-prj-phase3-ginger

#### __Ignore the folder "cs105-prj-phase2-ginger @ 052bd02" and "cs105-prj-phase1-ginger-master/ranking/billboard2016/billboard2016/sp". I have no idea how to delete these 2 files, so please ignore them__

cs105-prj-phase1-ginger @ 53048a4 -> Phase1 

cs105-prj-phase2-ginger-master -> Phase2

## Files
Machine Learning.ipynb -> The main file in this project. All the codes about the machine learning are here. 

learning data set.ipynb -> This is the file to create the dataset used for training and testing the model. The created file("t.csv") is used in Machine Learning.ipynb.

milion_song.ipynb -> This is the file to create the dataset used for picking up the 10000 songs from the million songs. The created file("msongs.csv")(length=10000) is used in learning data set.ipynb.

audio_features_for_milions_data.py -> This is the file to get the audio features of the songs in "msongs.csv" by using spotipy(Spotify API). The created file(audio_features_msongs.csv) is used in learning data set.ipynb.

audio_features.py -> This is the file to get the audio features of the songs in "ranking.csv" by using spotipy. The created file(audio_features.csv) is used in learning data set.ipynb.

## The description about dataset and problem
In the Machine Learning.ipynb, I used the dataset of "t.csv" which has the 9290 random songs audio features. Also, I used the dataset of "ranking.csv",which has the top100 billboard songs information from 1956-2019, to create a new column in DataFrame. The problem here is to predict if the each random song from "t.csv" is in top100 billboard ranking or not. To make it more simple, I tried to build the ML model to predict if "bbd"(The column which means if it's in top100 in billboard ranking or not) = 1 or 0.

## Summary in phase3
#### For running entire codes, it will take around 7-10 minutes, please be patient.

In this phase, I applied some sampling method, grid search, cross-validation, machine learning algorithm, RFE and so on. The biggest method that influence in good way is Oversampling(SMOTE) and undersampling. SMOTE works for increasing the number of minor class because the dataset was prettu imbalanced before applying. Before applying those, the f-1 score was much lower such as 0.3 and so on. But by applying those, there are some better error rate that I could get(around0.6), not desiable though. Also, I applied SMOTEENN which oversample the minor class and undersample the major class concurrently, but it does not show the results as I expected. In bothe SMOTE and SMOTEENN, I applied RFE(Recursive Feature Elimination) which works pretty good as well because I can get the features which perform the best. RFE are applied only in Logistic Regression and Random Forest, but it improves error. Also, I applied grid search which can be done with cross-validation method to find the desiable parameter in KNN. However, even I got desiable parameter by that, the performance did not improve not much. Also, adding new features "ever_bbd"(1 if the artist made the song in top100 before, 0 if the artist did not make it) improves the performance as well. In total, it seems like Random Forest perfoms the best out of all the 5 models when using SMOTE. In contrast, the KNN performs worst out of all the models.　In conclusion, I can get around 0.6 f1_score in general. This is not the perfect score, but it does improve exceedingly. 
