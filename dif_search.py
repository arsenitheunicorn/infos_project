from indexes import tfidfVec, df, I_bm25, I_tfidf, bm25_dict
from sklearn.metrics.pairwise import linear_kernel
from db_texter import preProcessing


# query in all funcs is already preprocessed
def tfidf_search(query):
    vec = tfidfVec.transform([query]).toarray()
    cos = linear_kernel(vec, I_tfidf).flatten()
    most_related = cos.argsort()[:-5:-1][0]
    answer = df.iloc[most_related]['Текст ответа']
    return answer

def bm25_search(query):
    lquery = query.split(' ')
    query_doc = bm25_dict.doc2bow(lquery)
    scores = I_bm25.get_scores(query_doc)
    best_doc = sorted(range(len(scores)),
        key=lambda i: scores[i]
    )[-1]
    answer = df.iloc[best_doc]['Текст ответа']
    return answer

def main(raw_query, method_name):
    query = preProcessing(raw_query)
    if method_name == "bm25":
        answer = bm25_search(query)
    elif method_name == "tfidf":
        answer = tfidf_search(query)
    else:
        answer = tfidf_search(query)
    return answer