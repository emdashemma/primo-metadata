## this script should be run from a directory that includes:
##	(1) file.csv, an export of Primo record from lib.washington.edu
##	(2) blurb.txt, a paragraph about OMC that will go at the bottom of the file
## and will create a txt file that can be pasted into the Internet Archive
## "description" field.

import csv

csvfile = open('file.csv', newline='')
obj = csv.reader(csvfile)

count = 0
for row in obj:
	if count == 0:
		header = row
	else:
		data = row
	count += 1

full_record = dict(zip(header, data))

# any column from the Primo csv can be listed in this dictionary to be included in the output txt file
to_include = ['Title', 'Language','Format', 'Catalog Title', 'Publisher', 'Publication Date', 'Performer or Participant', 'OCLC Number', 'Permalink']

selected_metadata = {}

for term in to_include:
	if term in full_record:
		selected_metadata[term] = full_record[term]

oclc = selected_metadata.get('OCLC Number')

with open("blurb.txt", "r") as f:
	blurb = f.read()

with open(f"{oclc}.txt", "w") as f:
	for key, value in selected_metadata.items():
		f.write('%s: %s\n\n' % (key, value))
	f.write(f"{blurb}")
