#!/bin/bash

# List of book IDs to download 

BOOK_IDS=("17192" "932" "1064" "1063" "51060" "2148" "2147" "10031" "2151")

BASE_URL="https://www.gutenberg.org/cache/epub"

# Loop through Book_IDs to download texts
for BOOK_ID in "${BOOK_IDS[@]}"; do
	FILE="pg${BOOK_ID}.txt"
	if [ ! -f "$FILE" ]; then 
		 wget "${BASE_URL}/${BOOK_ID}/pg${BOOK_ID}.txt"
	else
		echo "$FILE already exists, skipping download."
	fi
done
