import string, re
from nltk.corpus import stopwords
from pymorphy2 import MorphAnalyzer as Mystem
import pandas as pd

m = Mystem()
STOPWORDS = stopwords.words('russian')

def remove_chars(text, chars):
    text = ''.join([ch if ch not in chars else ' ' for ch in text])
    return re.sub('  +', ' ', text).strip()

def cleaningText(text):
    text = text.lower()
    spec_chars = string.punctuation + '\n\xa0«»\t—…'
    text = remove_chars(text, spec_chars)
    return text

def preProcessing(text, STOPWORDS=STOPWORDS, m=m):
    if type(text) == str and text != '':
        text = cleaningText(text)
        tokens = text.split(' ')
        lemmas = [m.parse(t)[0].normal_form for t in tokens]
        lemmas = [word for word in lemmas if word not in STOPWORDS]
        return ' '.join(lemmas)
    else:
        return ''

def get_db(fname='db_default\\queries_base.xlsx'):
    df_q = pd.read_excel(fname)
    df_q['lemmas'] = df_q['Текст вопроса'].apply(preProcessing)
    df_q.to_excel('test_queries.xlsx')

def main():
    get_db()

if __name__ == "__main__":
    main()