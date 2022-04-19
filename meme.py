import pickle
v = pickle.load(open('./og_data/vectors.p', 'rb'))
print(len(v[0][1]))
