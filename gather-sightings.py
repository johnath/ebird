#!/usr/bin/python

# Fed a list of locIDs on stdin or as filenames, build sightings URLs
import fileinput

stem = "http://ebird.org/ws1.1/data/obs/loc/recent?back=14&detail=simple&fmt=json&r="
def printURL (locList) :
  print stem + "&r=".join(locList);


locations = []
for line in fileinput.input() :
  locations.append(line.rstrip());
  if len(locations) > 9 :
    printURL(locations)
    locations = []
printURL(locations)


