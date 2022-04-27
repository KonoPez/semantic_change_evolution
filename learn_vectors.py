from gensim.models import Word2Vec
import pickle, random
import numpy as np

words = set()
key_vecs = []
for year in range(2010,2022):
    data = f"./nyt_text/{year}data.txt"
    model = Word2Vec(corpus_file=data,sg=1,negative=10)

    vecs = model.wv
    words.update(vecs.index_to_key)

    key_vecs.append(vecs)

v_def = [0 for i in range(100)]
words = list(words)
n = len(words)
all_vecs = []
for word in words:
    vecs_t = []
    for year in range(len(key_vecs)):
        try:
            vecs_t.append(key_vecs[year].get_vector(word))
        except KeyError:
            vecs_t.append(v_def)
    all_vecs.append(vecs_t)

all_vecs = np.asarray(all_vecs)
del key_vecs

labels = np.asarray(["change" for w in words], dtype=str)
with open("./data/vectors.p","wb") as save:
    pickle.dump(all_vecs,save)
del all_vecs

words = np.asarray(words, dtype=str)
with open("./data/words.p","wb") as save:
    pickle.dump(words,save)
del words

with open("./data/labels.p","wb") as save:
    pickle.dump(labels,save)

indx = [i for i in range(n)]
random.shuffle(indx)

test = np.asarray(indx[:n//5])
train = np.asarray(indx[n//5:])

with open("./data/test_idx.p","wb") as save:
    pickle.dump(test,save)

with open("./data/train_idx.p","wb") as save:
    pickle.dump(train,save)





