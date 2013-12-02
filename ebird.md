(Hastily scribbled notes and API endpoints - not to be confused with helpful documentation)

Recent Sightings API
https://confluence.cornell.edu/display/CLOISAPI/eBird-1.1-RecentNearbyObservations

Toronto-center-ish (richmond+peter): 43.6475, -79.393
http://ebird.org/ws1.1/data/obs/geo/recent?lng=-79.39&lat=43.65&fmt=json&back=14

===

Hotspots in CA-ON-TO: http://ebird.org/ws1.1/ref/hotspot/region?rtype=subnational2&r=CA-ON-TO&back=7&fmt=json
Peel CA-ON-PL: http://ebird.org/ws1.1/ref/hotspot/region?rtype=subnational2&r=CA-ON-PL&back=7&fmt=json
York CA-ON-YO: http://ebird.org/ws1.1/ref/hotspot/region?rtype=subnational2&r=CA-ON-YO&back=7&fmt=json

To extract locIDs (see loc.sh):
grep -o 'locID":"L[^"]*"' | sed 's/[^0-9L]//g' | sort | uniq

multi-loc fetch stem (append &r=…)
http://ebird.org/ws1.1/data/obs/loc/recent?back=7detail=simple&fmt=json&r=

GATHER THE OMNIBUS:
cat aug-23-locations GTA-hotspot-locIDs.txt | sort | uniq | ./gather-sightings.py | xargs curl | sed 's/\]\[/\,/g' > aug-23-omnibus