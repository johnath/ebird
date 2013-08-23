#!/bin/sh
cat $1 | grep -o 'locID":"L[^"]*"' | sed 's/[^0-9L]//g' | sort | uniq
