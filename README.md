# NLP_Election_2020

In this project I did an analysis of US election tweets scraped during October 2020. I scraped the tweets using Tweepy through the Twitter Developer API over a period of a few days (1 or 2 scrapes of 10000 tweets a night and retweets removed). 

I performed sentiment analysis using the NRC Lexicon, created wordclouds, explored popular hashtags, user creation dates and user locations. 

I also explored whether we could find clusters of tweets with similar characteristics using a variety of techniques. My initial approach was to try applying Agglomerative Clustering, HDBSCAN and OPTICS on document vectors using cosine dissimilarity as a distance metric. These largely proved futile and hence I decided to utilise the equivalence of the distance metric with Euclidean distance for unit vectors and apply MiniBatch KMeans. This proved to produce somewhat interesting segmentations, although due to the general density of the data a significant amount of points still grouped into one cluster. 

