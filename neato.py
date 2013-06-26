#!/usr/bin/python

import json
import csv

BIRDS_FILE = "johnath.csv"
RECENTS_FILE = "sample.json"


def readbirds (f) :
  csvreader = csv.reader(f)
  birds = []
  for row in csvreader :
    # We just want the latin species names from this list, second field, after the hyphen
    name = row[1]
    if (len(name.split('-')) > 1) :
      birds.append(name.split('-')[-1].strip())
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

## Read the recent sightings
recentsFile = open(RECENTS_FILE)
recents = readrecents(recentsFile)

# Drop birds we've already seen
recents = filter(lambda x : (x['sciName'] not in birds and not x['sciName'].endswith('sp.')), recents)

for bird in recents :
  print("{locName} - {comName} ({sciName})".format(**bird))
print(len(recents))


