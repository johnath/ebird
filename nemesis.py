#!/usr/bin/python

import json
import csv
import sys
import os
import subprocess

if len(sys.argv) is not 4 :
  print "Usage: " + sys.argv[0] + " <lat> <long> <sciname>"
  exit(0)

LAT = sys.argv[1] 
LNG = sys.argv[2]
NEMESIS = sys.argv[3]


DEBUG = False 
def debug (s) :
  if (DEBUG) : 
    print(s)

def readrecents (f) :
  recents = json.loads(f);
  
  # We only care about some fields
  def filter (s) :
    return {'obsDt' : s['obsDt'], 'locName' : s['locName'], 'howMany' : s['howMany']}

  return map(filter, recents)

recentsUrl = 'http://ebird.org/ws1.1/data/obs/geo_spp/recent?lng=' + str(LNG) + '&lat=' + str(LAT) + '&sci=' + str(NEMESIS) + '&fmt=json';

debug("*** loading URL: " + recentsUrl);

## Read the recent sightings (-s for silent mode curl)
## Sadface: check_output is python 2.7, and people.mozilla.org only has 2.6
## output = subprocess.check_output(["curl", "-s", recentsUrl])
output = subprocess.Popen(["curl", "-s", recentsUrl], stdout=subprocess.PIPE).communicate()[0]
debug("** curl output **")
debug(output);

#recents = readrecents(os.popen('curl ' + recentsUrl).read())
recents = readrecents(output)
debug("** Found {0} recent sightings".format(len(recents)))

for bird in recents :
  print("{obsDt} - {locName} ({howMany})".format(**bird))


