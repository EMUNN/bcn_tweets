import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns

import spacy
from spacy.tokenizer import Tokenizer
from spacy.lang.en import English

### YOU WILL HAVE TO INSTALL SEABORN AND spaCy


df = pd.read_csv('bcn_tweets_sample.csv')

### loading Natural Language Processor
nlp = spacy.load("es_core_news_sm")

### creating new column doc of tokenized tweets"
df['doc'] = [nlp(text) for text in df.text]


### printing every entity of every tweet

for i in df.doc:
    for token in i:
        print(token.pos_)


### all i want is a new column 'pos', that has all of that tweets parts of speech

#### id_unico |    text    |      doc      |       pos
#### ---------------------------------------------------------
####     0    | I love it  | (I, love, it) | (PRN, VERB, PRN)






# list={}
#
# for i in df.doc:
#     for token in i.ents:
#         list[str(token)]={token.label_}
#     print()
#
# print(df)
