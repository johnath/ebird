#!/bin/sh

# Build aggregate urls from list of hotspots | grab those JSON sighting reports | filter out empty reports ...
# ... | filter out internal ][ resulting from concatenation | dump to a new date-stamped file 
./gather-sightings.py GTA-hotspot-locIDs.txt | xargs curl | sed 's/\[\]//g' | sed 's/\]\[/\,/g' > `date +%Y-%m-%d`.json

# get the report for johnath based on the recent sightings
./neato.py johnath.csv `date +%Y-%m-%d`.json | sort 

