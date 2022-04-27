import pickle, numpy
r = open("./results/results_procr_star/12.p","rb")
words = pickle.load(open("./data/words.p","rb"))
res = pickle.load(r)
print(len(res))
print(len(words))
ranks = numpy.argsort(res)
print(words[ranks][len])