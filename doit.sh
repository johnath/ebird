#!/bin/bash
die () {
    echo >&2 "$@"
    exit 1
}
[ "$#" -eq 1 ] || die "usage: $0 <life-list-filename.csv>"

RECENTS="recents/`date +%Y-%m-%d`.json"

# Build aggregate urls from list of hotspots | grab those JSON sighting reports | filter out empty reports ...
# ... | filter out internal ][ resulting from concatenation | dump to a new date-stamped file 
./gather-sightings.py GTA-hotspot-locIDs.txt | xargs curl | sed 's/\[\]//g' | sed 's/\]\[/\,/g' > $RECENTS

# get the report for the specified life list based on the recent sightings. Hybrids are false positives
./neato.py $1 $RECENTS | grep -v 'hybrid' | sort 

