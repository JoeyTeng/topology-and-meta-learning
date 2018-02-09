
# @Author: Joey Teng
# @Email:  joey.teng.dev@gmail.com
# @Filename: preprocessing.py
# @Last modified by:   Joey Teng
# @Last modified time: 09-Feb-2018

from os import listdir
from sys import argv
import json
import numpy as np

meta_names = [
    'Size versus Number of Clusters',
    'Density distribution over 10 intervals',
    'Number of Clusters']

files = []
for path in argv[1:]:
    files.extend([
        "{0}/{1}".format(path, filepath)
        for filepath in listdir(path) if filepath.endswith('.output.json')])

meta_features_by_dataset = []
for filename in files:
    metas_by_dataset = json.load(open(filename, 'r'))
    meta_features = list(range(5))
    for i in range(len(meta_names) - 1):
        meta_features[i * 2] =\
            metas_by_dataset[meta_names[i]]['_population']['average'] /\
            metas_by_dataset[meta_names[i]]['_population']['range']
        meta_features[i * 2 + 1] =\
            metas_by_dataset[
                meta_names[i]]['_population']['standard deviation'] /\
            metas_by_dataset[meta_names[i]]['_population']['range']
    meta_features[-1] = metas_by_dataset[meta_names[-1]]['_population']
    np.save(
        "{0}".format(filename.strip('.output.json')),
        np.array(meta_features))