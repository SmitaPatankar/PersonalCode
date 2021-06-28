import pickle

# write - small
# https://www.youtube.com/watch?v=2Tw39kZIbhs
d = {1:1, 2:2, 3:3}
with open("C:/REPOSITORIES/MyRepo/.trash/output.pickle", "wb") as p:
    pickle.dump(d, p)

# read - small
# https://www.youtube.com/watch?v=2Tw39kZIbhs
with open("C:/REPOSITORIES/MyRepo/.trash/output.pickle", "rb") as p:
    d = pickle.load(p)
    print(d)
