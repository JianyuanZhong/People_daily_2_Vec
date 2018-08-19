from __future__ import absolute_import, division, print_function
import codecs
import glob
import logging
import multiprocessing
import os
import pprint
import re
import nltk
import gensim.models.word2vec as w2v
import sklearn.manifold
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

#%pylab inline

logging.basicConfig(format=' %(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

f = open("data_txt.txt", 'r+')

line = ''
for i in range(10):
	line = f.readline()
	print(line)