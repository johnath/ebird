#!/usr/bin/python

import json
import csv
import sys

if len(sys.argv) is not 3 :
  print "Usage: " + sys.argv[0] + " <ebird sightings list csv> <ebird recent reports json>"
  exit(0)

BIRDS_FILE = sys.argv[1] 
RECENTS_FILE = sys.argv[2]

DEBUG = False
def debug (s) :
  if (DEBUG) : 
    print(s)

def readbirds (f) :
  csvreader = csv.reader(f)
  birds = []
  for row in csvreader :
    # We just want the latin species names from this list, second field, after the hyphen
    name = row[1]
    if (len(name.split('-')) > 1) :
      birds.append(name.split('-')[-1].strip())
      debug(birds)
  return birds

def readrecents (f) :
  recents = json.load(f);
  
  # We only care about some fields
  def filter (s) :
    return {'comName' : s['comName'], 'locName' : s['locName'], 'sciName' : s['sciName']}

  return map(filter, recents)

## Read the life list
birdsFile = open(BIRDS_FILE)
birds = readbirds(birdsFile)
debug("* Found {0} birds from life list".format(len(birds)))


## Read the recent sightings
recentsFile = open(RECENTS_FILE)
recents = readrecents(recentsFile)
debug("** Found {0} recent sightings, before filtering".format(len(recents)))

# Drop birds we've already seen
recents = filter(lambda x : (x['sciName'] not in birds and not x['sciName'].endswith('sp.')), recents)
debug("*** Found {0} interesting recents after filtering".format(len(recents)))

for bird in recents :
  print("{locName} - {comName} ({sciName})".format(**bird))


