import pandas as pd
import numpy as np
import pickle

from MATH.math import NeighborSampler

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import TruncatedSVD

from sklearn.neighbors import BallTree

from sklearn.pipeline import make_pipeline

pipepath = "C:\\Users\\Josh\\Repositories\\NaatchiBot-Rewrite\\src\\python\\DATA\\OUT\\pipe.p"

loop = 1 + 1


def ai(user):
    with open(pipepath, 'rb') as fp:
        pipe = pickle.load(fp)

        predict, distribution = pipe.predict([user])
        print("probability: "+str(distribution).replace("array", "")[2:][:-2]+"\n")
    return predict[0]

while loop == 2:
    print('send a message to the ai')
    user = input('>')

    print(ai(user))