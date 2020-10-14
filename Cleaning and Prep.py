import pandas as pd
import re
import numpy as np
from ast import literal_eval
import datetime
import spacy


date=str(datetime.datetime.today().date()) 

df=pd.read_csv('Election_tweets_'+date+'.csv', index_col=0)


#retweets
def check_rt(text):
    if text[0:2]=='RT':
        return 1
    else:
        return 0
df['rt_flag']=df['contents'].apply(check_rt)
print('No. Retweets: ', df[df['rt_flag']==1].shape[0])
df=df[df['rt_flag']==0].reset_index(drop=True)
df.drop('rt_flag', axis=1, inplace=True)

#check null - shouldnt be any apart from location
missing_values=df.isnull().sum()
missing_values.sort_values(ascending=False,inplace=True)
print(missing_values)

#text clean - also removes emojis
def clean_text(text):
    text=str(text).lower()
    text = re.sub('(https?:\/\/)(www\.)?\S+', '', text)
    text=re.sub('(pic\.)\S+','',text)
    text=re.sub(r'\@(\s)?\S+','', text) #removes mentions
    text=re.sub(r'\#\S+','',text) #removes hashtags
    text=re.sub(r'[^\w\s]',' ',text)  #remove punctuation (adds a space)
    text=re.sub(r'\s+', ' ', text)   #removes doublespace
    return text
    
df['contents']=df['contents'].apply(clean_text)
df['username']=df['username'].apply(clean_text)

#hashtags
df['hashtag']=df['hashtag'].apply(literal_eval)
def get_hashtags(hashtag_dict_list):
    hashtags=[]
    for dic in hashtag_dict_list:
        hashtags.append(clean_text(dic['text']))
    return hashtags
df['hashtag']=df['hashtag'].apply(get_hashtags)

#mentions
df['mentions']=df['mentions'].apply(literal_eval)
def get_mentions(mention_dict_list):
    mentions=[]
    for dic in mention_dict_list:
        temp={}
        temp['screen_name']=dic['screen_name']
        temp['name']=dic['name']
        temp['id']=dic['id']
        mentions.append(temp)
    return mentions
df['mentions']=df['mentions'].apply(get_mentions)

#append cleaned to master
master=pd.read_csv('Election_Tweets_Master.csv',index_col=0)
master=master.append(df,ignore_index=True)
master.to_csv('Election_Tweets_Master.csv')
print('Main data appended.')

#word vectors df
df_wv=pd.DataFrame(df['contents'].copy(), columns=['contents'])
nlp=spacy.load("en_core_web_lg")
print('Starting vectors')
with nlp.disable_pipes():
    tweet_vectors=np.array([nlp(tweet.contents).vector for idx, tweet in df_wv.iterrows()])
tweet_vectors=pd.DataFrame(tweet_vectors, columns=['Component-'+str(i) for i in range(1,301)])
df_wv=df_wv.join(tweet_vectors)
print('Vectors complete.')
print(df_wv.head())

#append vectors data to master
master_word_vec=pd.read_csv('Master_word_vectors.csv',index_col=0)
master_word_vec=master_word_vec.append(df_wv, ignore_index=True)
master_word_vec.to_csv('Master_word_vectors.csv')
print('Vectors data appended.')