#!/bin/bash

# List of book IDs to download 

BOOK_IDS=("17192" "932" "1063" "10031" "14082")

BASE_URL="https://www.gutenberg.org/cache/epub"

mkdir -p books
# Loop through Book_IDs to download texts
for BOOK_ID in "${BOOK_IDS[@]}"; do
	FILE="books/pg${BOOK_ID}.txt"
	if [ ! -f "$FILE" ]; then 
		 wget -O "$FILE" "${BASE_URL}/${BOOK_ID}/pg${BOOK_ID}.txt"
	else
		echo "$FILE already exists, skipping download."
	fi
done
