#!/bin/bash

echo Searching for "$2" in "$1" for export to "$3"...


fasta="$1"; motif="$2"; out="$3"

awk -v M="$motif" -v out="$out" '
/^>/ { name = substr($0,2); next }
{if (match($0, M)) {count += gsub(M, "&")
print name "\t" substr($0, RSTART, RLENGTH) "\t" $0}}
END { print "Total motif matches:", count }

' "$fasta" > "$out"

echo "...Completed"
