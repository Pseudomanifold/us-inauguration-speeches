#!/usr/bin/env python3
#
#  Performs an analysis of U.S. Presidental Inauguration Speeches based
#  on TF-IDF information. The script performs multiple things:
#
#  1. Extraction of the five most relevant words (according to the
#     TF-IDF weights) of each speech.
#
#  2. Using LDA to obtain 5 different topics present in the corpus
#     of speeches and assigning every document to its model.
#
#  Original author: Bastian Rieck

import numpy
import os
import sys

from sklearn.decomposition           import LatentDirichletAllocation
from sklearn.feature_extraction.text import TfidfVectorizer

num_topics = 5
num_words  = 5

"""
Extracts the top n words from a row in the TF-IDF matrix. This requires
knowledge about the feature names, i.e. the actual words present in the
text.
"""
def get_top_words(row, feature_names, n=5):
  top_ids   = numpy.argsort(row)[:-n-1:-1]
  top_names = [feature_names[i] for i in top_ids]

  return top_names

"""
Gets all topics from a given topic model and describes them using
a number of words.
"""
def get_topics(model, feature_names, n=3):
  topics = []
  for index, topic in enumerate(model.components_):
    words = " ".join( feature_names[i] for i in topic.argsort()[:-n-1:-1] )
    topics.append( words )

  return topics

"""
Extracts a year and a name from a filename.
"""
def get_year_and_name(filename):
  basename = os.path.basename(filename)
  name     = os.path.splitext(basename)[0]
  name     = name.replace("_", " ")
  year     = name[:4]
  name     = name[5:]

  return year, name

"""
main
"""
if __name__ == "__main__":

  # First, some pre-processing to make the output a little bit more
  # shiny and nice.
  filenames        = sys.argv[1:]
  filename_to_name = dict()
  filename_to_year = dict()

  for filename in filenames:
    year, name                 = get_year_and_name(filename)
    filename_to_name[filename] = name
    filename_to_year[filename] = year

  #####################################################################
  # TF-IDF analysis
  #####################################################################

  tf_idf_vectorizer = TfidfVectorizer(input='filename',
                           stop_words='english',
                           max_df=0.95,
                           strip_accents='unicode')

  tf_idf = tf_idf_vectorizer.fit_transform(filenames)

  for index, filename in enumerate(filenames):
    year     = filename_to_year[filename]
    name     = filename_to_name[filename]
    words    = get_top_words( tf_idf[index].toarray().ravel(), tf_idf_vectorizer.get_feature_names(), num_words)

    print("%s (%s): %s" % (year, name, " ".join(words)))

  #####################################################################
  # LDA analysis
  #####################################################################

  lda = LatentDirichletAllocation(n_topics=num_topics,
                                  learning_method="online",
                                  max_iter=20,
                                  random_state=42)
  lda.fit(tf_idf)

  topics = get_topics(lda, tf_idf_vectorizer.get_feature_names())

  for index, topic in enumerate(topics):
    print("Topic %d: %s" % (index, "".join(topic)))

  for index, filename in enumerate(filenames):
    scores = lda.transform(tf_idf[index]).ravel()
    topic  = numpy.argsort(scores)[-2]

    print(topics[topic])
