import pandas as pd
import spacy
from nltk.tokenize import word_tokenize
mast=pd.read_csv('Election_Tweets_Master.csv', index_col=0)

nlp=spacy.load('en_core_web_lg')
all_stopwords = nlp.Defaults.stop_words
list_stopwords=["election","new","amp","tv","bbc","news" "rep", 
                "surveymonkey", "twitter","ipsos","ll","poll",'ve','don', 't','one','way','day','need',
               'give', 'better','let','time','take','part','know','make','even','said','re','many','say',
               'help','today','join','see','via','think','year','going','people','still','come','tell','thought','us','will'
               'want','happen','sure','thank','you','week','weeks','day','days','try','lot','thing','things','doesn','got','look',
               'use','matter','users','updates','live','news','cbs','cnn','fox','nbc','follow','oct','october','want']
for word in list_stopwords:
    all_stopwords.add(word)

mast['contents_tokenised']=mast['contents'].apply(lambda x: word_tokenize(x))

def sw_fn(text_tokens):
    tokens_without_sw=[word for word in text_tokens if not word in all_stopwords]
    return (" ").join(tokens_without_sw)

mast['cleaned_contents']=mast['contents_tokenised'].apply(sw_fn)
mast['cleaned_contents'].head()

mast.drop('contents_tokenised',axis=1,inplace=True)
mast.to_csv('master_stopwords_removed.csv', index=False)


