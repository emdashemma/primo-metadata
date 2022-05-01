### Exporting catalog metadata for Internet Archive

1. Go to [lib.washington.edu](lib.washington.edu) and search for the disc by OCLC number. Open the record and click "Export to Excel," change the file type to "CSV," and click "Download." Rename this file to `file.csv` and move it into the folder with `mapping.py`.

<img width="400" align="left" alt="export" src="https://user-images.githubusercontent.com/75695487/166128204-46056e7c-6d37-470b-a2c9-bebcff1b9d73.png">

2. Open a command prompt, navigate to the folder, and run `mapping.py`. It will generate a text file called `[OCLC number].txt` with a subset of the catalog record's fields, structured with headers. 

3. Copy the contents of this text file into the "Description" field of the Internet Archive upload page. Bold the field headers, hyperlink the links, and fill out the other metadata fields according to the project instructions.
