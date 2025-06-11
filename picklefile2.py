import pickle
l=[99,88,77,66,55,44,33]
file=open('picklefile2.txt','wb')
pickle.dump(l,file)
file.close()
