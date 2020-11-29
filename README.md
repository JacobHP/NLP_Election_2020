# NLP_Election_2020

# Part 1
In this project I did an analysis of US election tweets scraped during October 2020. I scraped the tweets using Tweepy through the Twitter Developer API over a period of a few days (1 or 2 scrapes of 10000 tweets a night and retweets removed). 

I performed sentiment analysis using the NRC Lexicon, created wordclouds, explored popular hashtags, user creation dates and user locations. 

I also explored whether we could find clusters of tweets with similar characteristics using a variety of techniques. My initial approach was to try applying Agglomerative Clustering, HDBSCAN and OPTICS on document vectors using cosine dissimilarity as a distance metric. 
These largely proved futile and hence (after learning a bit more about NLP) I decided to utilise the equivalence of the cosine dissimilarity distance metric with Euclidean distance for unit vectors and apply MiniBatch KMeans after tfidf vectorisation and stopword removal. This proved to produce somewhat interesting segmentations, although there was still some overlap. 


![alt text](https://github.com/JacobHP/NLP_Election_2020/blob/master/Images_for_readme/Clusters.png?raw=true)
![alt text](https://github.com/JacobHP/NLP_Election_2020/blob/master/Images_for_readme/Cloud.png?raw=true)   
![alt text](https://github.com/JacobHP/NLP_Election_2020/blob/master/Images_for_readme/Sentiment.png?raw=true)


# Part 2
For this part I want to look at whether we can accurately classify pro-biden and pro-trump tweets based on contents alone. I will be labelling based on hashtags. 
