import pickle, numpy
all_vecs = numpy.asarray(pickle.load(open("./data/vectors.p","rb")))
words = numpy.asarray(pickle.load(open("./data/words.p","rb")), dtype=str)
labels = numpy.asarray(pickle.load(open("./data/labels.p","rb")), dtype=str)
test = numpy.asarray(pickle.load(open("./data/test_idx.p","rb")))
train = numpy.asarray(pickle.load(open("./data/train_idx.p","rb")))

with open("./data/vectors.p","wb") as save:
    pickle.dump(all_vecs,save)

with open("./data/words.p","wb") as save:
    pickle.dump(words,save)

with open("./data/labels.p","wb") as save:
    pickle.dump(labels,save)

with open("./data/test_idx.p","wb") as save:
    pickle.dump(test,save)

with open("./data/train_idx.p","wb") as save:
    pickle.dump(train,save)
