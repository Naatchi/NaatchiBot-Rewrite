import pandas as pd
import numpy as np
import pickle

from MATH.math import NeighborSampler

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import TruncatedSVD

from sklearn.neighbors import BallTree

from sklearn.pipeline import make_pipeline

csvpath = "C:\\Users\\Josh\\Repositories\\NaatchiBot-Rewrite\\src\\python\\DATA\\OUT\\data.csv"
pipepath = "C:\\Users\\Josh\\Repositories\\NaatchiBot-Rewrite\\src\\python\\DATA\\OUT\\pipe.p"

ns = NeighborSampler()
data = pd.read_csv(csvpath)
data.info()
vectorizer = TfidfVectorizer()
svd = TruncatedSVD(n_components=350, algorithm='arpack')

prompt = input("select: Train or load")

if prompt == ("train"):
    vectorizer.fit(data.context)
    matrixBig = vectorizer.transform(data.context)
    svd.fit(matrixBig)
    
    matrixSmall = svd.transform(matrixBig)

    ns.fit(matrixSmall, data.reply)

    pipe = make_pipeline(vectorizer, svd, ns)
    
    with open(pipepath, 'wb') as pickle_file:
        pickle.dump(pipe, pickle_file, protocol=4)

# this is here because it cries if i dont have it here.