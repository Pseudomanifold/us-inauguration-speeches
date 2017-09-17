#!/usr/bin/env python3
#
# Calculates sentiment polarity scores over the progression of a speech
# and writes them to STDOUT. The output can be parsed by gnuplot.
#
# Original author: Bastian Rieck

from textblob import TextBlob

import os
import sys

"""
Calculates sentiments over the progression of a given speech. The
results of this function are scaled such that the total *time* of
the speech lies between [0,1].
"""
def make_sentiment_curve(text, title):
  blob       = TextBlob(text)
  n          = len(blob.sentences)
  polarities = []

  print("\"%s\"" % title)

  for index, sentence in enumerate(blob.sentences):
    polarity = sentence.sentiment.polarity
    t        = index / (n-1)

    polarities.append(polarity)

    print(t, polarity)

  # Try to mitigate issues with floating point numbers; I am pretty sure
  # that this should *not* be that relevant here, though.
  sum_polarities = sum( sorted(polarities) )
  mean_polarity  = sum_polarities / n

  print("\n")

  print("\"%s\"" % title)
  print("0.0 %f" % mean_polarity)
  print("1.0 %f" % mean_polarity)
  
  print("\n")


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
  for filename in sys.argv[1:]:
    year, name = get_year_and_name(filename)
    text       = ""
    title      = "%s (%s)" % (name, year)
  
    with open(filename) as f:
      text = f.read()

    make_sentiment_curve(text, title)
