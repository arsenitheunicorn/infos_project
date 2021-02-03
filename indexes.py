from db_texter import preProcessing
from sklearn.feature_extraction.text import TfidfVectorizer
from gensim import corpora
from gensim.summarization import bm25
import pandas as pd


tfidfVec = TfidfVectorizer()

df = pd.read_excel('final_db.xlsx')
df.dropna(
    axis=0,
    how='any',
    thresh=None,
    subset=None,
    inplace=True
)

def index_tfidf():
    lemmas = df['lemmas'].tolist()
    x = tfidfVec.fit_transform(lemmas)
    return x.toarray()

def index_bm25():
    lemmas = df['lemmas'].tolist()
    lemmas = [doc.split(' ') for doc in lemmas]
    dictionary = corpora.Dictionary(lemmas)
    corpus = [dictionary.doc2bow(text) for text in lemmas]
    bm25_obj = bm25.BM25(corpus)
    return bm25_obj, dictionary

I_tfidf = index_tfidf()
I_bm25, bm25_dict = index_bm25()
