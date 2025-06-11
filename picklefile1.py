import pickle
l=[11,22,33,44,55,66]
with open('picklefile1.txt','wb') as file:
    pickle.dump(l,file)
