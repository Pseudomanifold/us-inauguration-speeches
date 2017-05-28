#!/usr/bin/env python3

import glob
import nltk
import os

from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize

from nltk.stem.wordnet import WordNetLemmatizer

"""
Maps a tag from the Treebank tagger to a WordNet tag. If no match is
found, the function returns None.
"""
def get_wordnet_tag(tag):
  if tag.startswith('JJ'):
    return 'a'
  elif tag.startswith('RB') or tag == "WRB":
    return 'r'
  elif tag.startswith('NN') or tag.startswith("WP"):
    return 'n'
  elif tag.startswith('VB'):
    return 'v'
  else:
    return None

speeches = dict()
for filename in glob.glob("Data/*.txt"):
  basename = os.path.basename(filename)
  name     = os.path.splitext(basename)[0]
  name     = name.replace("_", " ")
  year     = name[:4]
  name     = year+"-"+name[5:]
  with open(filename) as f:
    speech         = f.read()
    speeches[name] = speech

lemmatizer = WordNetLemmatizer()

num_sentences     = dict()
num_words         = dict()
avg_sentence_len  = dict()
num_unique_lemmas = dict() 
num_unique_words  = dict()

print("# YYYY name num_sentences num_words avg_sentence_len num_unique_words num_unique_lemmas")

for president in sorted(speeches.keys()):
  speech    = speeches[president]
  sentences = sent_tokenize(speech)
  words     = word_tokenize(speech)

  avg_sentence_len[president]  = 0.0
  for sentence in sentences:
    avg_sentence_len[president] += len(word_tokenize(sentence))
  avg_sentence_len[president] /= len(sentences)

  num_sentences[president]    = len(sentences)
  num_words[president]        = len(words)
  num_unique_words[president] = len(set(words))

  tagged = nltk.pos_tag(words)
  lemmas  = set()

  for word,tag in tagged:
    pos = get_wordnet_tag(tag)
    if pos:
      lemmas.add(lemmatizer.lemmatize(word, pos=pos))
    else:
      lemmas.add(word)

  year = int(president[:4])
  name = president[5:]

  num_unique_lemmas[president] = len(lemmas)
  print('%d "%s" %d %d %f %d %d' % (year, name, num_sentences[president], num_words[president], avg_sentence_len[president], num_unique_words[president], num_unique_lemmas[president] ) )
